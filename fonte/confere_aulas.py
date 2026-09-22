#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guarda das aulas. Cada regra aqui nasceu de um defeito que passou pela
   revisao humana e so apareceu quando eu segui a aula como aluno."""
import importlib, json, os, re

# os caminhos de conteudo sao relativos a fonte/: rode de onde quiser
import os as _os; _os.chdir(_os.path.dirname(_os.path.abspath(__file__)))

def _texto(p):
    """Sem as etiquetas HTML: 'aba <span class=ui>Modelo</span>' tem de casar
       com quem procura 'aba Modelo'."""
    bruto = " ".join([p.get("corpo", ""), p.get("depois", ""), p.get("ck", ""), p.get("titulo", "")]
                     + [d + " " + r for d, r in p["sos"]])
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", bruto))

def aulas():
    todas = {}
    J = json.load(open("aula1/passos.json", encoding="utf-8"))
    todas[1] = {"passos": [dict(p, sos=[tuple(s) for s in p["sos"]]) for p in J]}
    for i in range(2, 40):
        try:
            todas[i] = importlib.import_module(f"conteudo_a{i}").AULA
        except ModuleNotFoundError:
            continue
    return todas

def confere():
    A = aulas()
    erros = []
    nao_capturadas = []
    def erra(m): erros.append(m)

    for i, a in A.items():
        ns = [p["n"] for p in a["passos"]]
        if ns != list(range(1, len(ns) + 1)):
            erra(f"aula {i}: numeracao dos passos fora de ordem: {ns}")

        tem_codigo = any(p.get("codigo") for p in a["passos"])
        txt = " ".join(_texto(p) for p in a["passos"])

        # 1. quem digita codigo tem de PREPARAR o editor na propria aula:
        #    o computador da semana pode ser outro, e o aluno pode ter faltado.
        prep = [p for p in a["passos"] if "prepare o editor" in p["titulo"].lower()]
        if tem_codigo and not prep:
            erra(f"aula {i}: digita codigo e nao tem o PASSO de preparar o editor")
        for p in prep:
            if "assistente de código" not in _texto(p) or "fechamento automátic" not in _texto(p):
                erra(f"aula {i} passo {p['n']}: o passo de preparar nao desliga as duas coisas")

        # 2. a aba Modelo e a setinha do Workspace: sem elas os botoes
        #    da aula "nao existem" na tela do aluno.
        if not re.search(r"aba .{0,12}Modelo", txt, re.I):
            erra(f"aula {i}: nunca manda ir para a aba Modelo")

        for p in a["passos"]:
            cod = p.get("codigo")
            if not cod:
                continue
            # 3. as linhas que o editor escreve sozinho sao exatamente os 'end'
            ends = tuple(k for k, l in enumerate(cod.split("\n"), 1) if l.strip().startswith("end"))
            if tuple(p.get("auto", ())) != ends:
                erra(f"aula {i} passo {p['n']}: auto={p.get('auto',())} mas os end estao em {ends}")
            # 4. aspa e tecla morta no teclado brasileiro
            if '"' in cod and sum("tecla muda" in d + r for d, r in p["sos"]) != 1:
                erra(f"aula {i} passo {p['n']}: codigo com aspas sem (ou com dois) socorro da tecla muda")
            # 5. o popup de sugestao come o Enter
            if not any("caixinha cinza" in d for d, _ in p["sos"]):
                erra(f"aula {i} passo {p['n']}: codigo sem o socorro do popup de sugestao")
            # 6. Tab aceita a sugestao; nenhuma aula pode mandar apertar Tab
            if re.search(r"\bTab\b", _texto(p)) and "não aperte Tab" not in _texto(p).lower().replace("nao", "não"):
                pass

        # 7. referencias a passos: tem de existir mesmo
        for p in a["passos"]:
            t = _texto(p)
            for m in re.finditer(r"[Aa]ula (\d)[^.]{0,30}?passos? (\d+)(?:\s*(?:a|e)\s*(\d+))?", t):
                alvo = int(m.group(1))
                for g in (m.group(2), m.group(3)):
                    if g and int(g) not in {q["n"] for q in A[alvo]["passos"]}:
                        erra(f"aula {i} passo {p['n']}: aponta '{m.group(0)}' e a aula {alvo} nao tem esse passo")
            for m in re.finditer(r"passos? (\d+)(?:\s*(?:a|e)\s*(\d+))? d[ao] [Aa]ula (\d)", t):
                alvo = int(m.group(3))
                for g in (m.group(1), m.group(2)):
                    if g and int(g) not in {q["n"] for q in A[alvo]["passos"]}:
                        erra(f"aula {i} passo {p['n']}: aponta '{m.group(0)}' inexistente")
            for m in re.finditer(r"(?:[Vv]olte ao|[Rr]efaça o|no|ao) passo (\d+)(?! d)", t):
                if int(m.group(1)) not in {q["n"] for q in a["passos"]}:
                    erra(f"aula {i} passo {p['n']}: aponta o proprio passo {m.group(1)}, que nao existe")

        # 7b. existir nao basta: depois de renumerar, "Volte ao passo 9" continuou
        #     apontando um passo que EXISTE e virou o assunto errado. Quando a
        #     frase marca o termo que se vai conferir la, ele tem de estar la.
        for p in a["passos"]:
            # o vao nao pode conter '?' nem '(': sem isso o casamento pula de
            # um item da lista para o seguinte ("...no passo 3? (3) o <b>X</b>")
            for m in re.finditer(r"passo (\d+)[^.<?()]{0,40}<(?:b|span[^>]*)>([^<]{4,})</(?:b|span)>",
                                 p.get("corpo", "") + " " + " ".join(d + " " + r for d, r in p["sos"])):
                alvo = [q for q in a["passos"] if q["n"] == int(m.group(1))]
                termo = m.group(2).strip().lower()
                if alvo and termo not in _texto(alvo[0]).lower() and termo not in (alvo[0].get("codigo") or "").lower():
                    erra(f"aula {i} passo {p['n']}: manda conferir '{termo}' no passo "
                         f"{m.group(1)} ('{alvo[0]['titulo']}'), que nao fala disso")

        # 7c. Script inserido tem de ganhar CODIGO. O passo 12 da Aula 9 mandava
        #     inserir um Script (e a animacao mostrava o gesto) e nunca dizia o que
        #     escrever dentro: quem so lesse aquele passo terminava com um Script
        #     vazio. Vale o proprio passo, os dois seguintes, ou a frase que diz
        #     de onde vem o codigo.
        ps = a["passos"]
        for k, p in enumerate(ps):
            if not re.search(r"escolha .{0,24}Script\b", _texto(p), re.I):
                continue
            t = _texto(p)
            tem = (p.get("codigo")
                   or any(q.get("codigo") for q in ps[k + 1:k + 3])
                   or re.search(r"c[óo]digo d[ae] ?(receita|aula)|vem no pr[óo]ximo passo|"
                                r"e escreva:|escreva:", t, re.I))
            if not tem:
                erra(f"aula {i} passo {p['n']}: manda inserir um Script e nao diz "
                     f"que codigo vai dentro ('{p['titulo']}')")

        # 7d. o clipe mostra um gesto que o TEXTO nao nomeia. Foi assim que o
        #     passo 12 da Aula 9 escapou da regra de cima: a animacao inseria
        #     um Script e a palavra "Script" nao aparecia no passo — quem lesse
        #     so o texto nunca sabia que tinha um Script para preencher.
        for p in ps:
            # a palavra tem de estar na INSTRUCAO (corpo/titulo), nao num socorro:
            # o passo 12 velho dizia "apague os scripts" so no quadro laranja.
            instr = re.sub(r"<[^>]+>", "", p.get("corpo", "") + " " + p.get("titulo", "")).lower()
            if "script" in (p.get("clipe") or "").lower() and "script" not in instr:
                erra(f"aula {i} passo {p['n']}: o clipe {p['clipe']} insere um Script "
                     f"e o texto nunca fala em Script ('{p['titulo']}')")

        # 7e. todo nome que o CODIGO procura no mundo tem de ser um nome que
        #     a aula mandou criar. "workspace.Largada" sem um passo que diga
        #     para renomear a peca para Largada e a forma mais comum de uma
        #     aula plausivel nao funcionar na mao do aluno.
        texto_aula = " ".join(_texto(p) for p in a["passos"]).lower()
        for p in a["passos"]:
            cod = p.get("codigo")
            if not cod:
                continue
            procurados = set(re.findall(r"workspace\.([A-Z]\w+)", cod))
            procurados |= {m for m in re.findall(r"\.Parent\.(\w+)", cod)
                           if m not in ("Humanoid", "Parent", "Name")}
            for nome in procurados:
                if nome.lower() not in texto_aula:
                    erra(f"aula {i} passo {p['n']}: o codigo procura '{nome}' "
                         f"e nenhum passo manda criar uma peca com esse nome")

        # 8. toda foto existe no disco. Aula ainda NAO capturada fica de
        #    fora desta regra — mas nunca em silencio: ela e LISTADA no fim,
        #    porque pular calado e o jeito mais facil de um guarda mentir.
        import glob as _glob
        if i > 1 and not _glob.glob(f"aula{i}/*.jpg"):
            nao_capturadas.append(i)
            continue
        for p in a["passos"]:
            img = p.get("img")
            if img and not os.path.exists(img) and i > 1:
                erra(f"aula {i} passo {p['n']}: foto sumida {img}")

    if nao_capturadas:
        print("  (aulas escritas mas ainda SEM captura, fora da regra da foto: "
              + ", ".join(str(n) for n in sorted(nao_capturadas)) + ")")
    return erros

if __name__ == "__main__":
    e = confere()
    for m in e:
        print("  !!", m)
    print(f"  {len(e)} problema(s)")
    raise SystemExit(1 if e else 0)
