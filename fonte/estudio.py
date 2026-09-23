#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rotinas do Studio usadas por todas as aulas. Cada uma CONFERE o proprio
   resultado — nada aqui devolve sucesso sem prova."""
import re, time, rs, monta, reenc
from PIL import Image, ImageChops
import numpy as np

ESC, DEL, ENTER = 53, 51, 36
VIEW = (624, 200, 2550, 1700)

# o menu do "+" muda de conteudo conforme o objeto selecionado:
# nada de coordenada fixa aqui, tudo se acha pelo texto


def tentar(f, n=3, espera=1.5, o_que=""):
    """O Studio e intermitente: menu que nao abre, clique que nao pega.
       Repetir com conferencia e mais honesto do que fingir que foi."""
    erro = None
    for k in range(n):
        try:
            return f()
        except Exception as e:
            erro = e
            print(f"   (tentativa {k+1} de {o_que or 'acao'}: {e})")
            time.sleep(espera)
    raise erro


def liga():
    reenc.prep()
    rs.ativa(); time.sleep(0.6)
    return monta.JAN


def explorador(J, regiao=(0.855, 0.13, 1, 0.60)):
    """Devolve [(nome, x, y, largura, altura)] das linhas do Explorador."""
    a = monta.cap("_exp")
    return [(t.strip(), x, y, w, h) for t, x, y, w, h in
            rs.ocr(a, regiao=regiao, psm="6", escala=2) if t.strip()]


def acha_linha(J, nome, n=0, tentativas=3):
    """Acha uma linha do Explorador. O OCR falha de vez em quando na linha
       realcada — repetir a leitura resolve quase sempre."""
    def limpo(t):
        # o OCR gruda o '+' da linha selecionada no nome ("Piso®") e troca caixa
        return "".join(c for c in t.lower() if c.isalnum())
    alvo = limpo(nome)
    for k in range(tentativas):
        linhas = explorador(J)
        achados = [l for l in linhas if limpo(l[0]) == alvo]
        if not achados:
            # o OCR gruda o '+' no nome e as vezes corta a ultima letra:
            # aceitar nos dois sentidos
            achados = [l for l in linhas
                       if (limpo(l[0]).startswith(alvo) and len(limpo(l[0])) <= len(alvo) + 2)
                       or (len(limpo(l[0])) >= 6 and alvo.startswith(limpo(l[0])))]
        if len(achados) > n:
            _, x, y, w, h = achados[n]
            return (x + w // 2, y + h // 2, x + w, y + h // 2)
        time.sleep(0.6)
    return None


def seleciona(J, nome, n=0):
    l = acha_linha(J, nome, n)
    if not l:
        raise RuntimeError(f"nao achei '{nome}' no Explorador")
    rs.confere(); rs.clique_img(l[0], l[1], escala=2.0, janela=J); time.sleep(1.0)
    return l


def insere_em(J, pai, objeto, n=0):
    """Seleciona o pai, clica no '+' da linha e escolhe o objeto.
       Confere que o filho apareceu."""
    antes = [t for t, *_ in explorador(J)]
    l = seleciona(J, pai, n)
    mais_x = l[2] + 30                      # o '+' vem logo depois do nome
    ids = {j["id"] for j in rs.janelas()}
    rs.confere(); rs.clique_img(mais_x, l[1], escala=2.0, janela=J); time.sleep(2.0)
    menu = [j for j in rs.janelas() if j["id"] not in ids and j["w"] > 150 and j["h"] > 150]
    if not menu:
        raise RuntimeError("o menu do '+' nao abriu")
    m = menu[0]
    # o menu do '+' muda conforme o objeto selecionado — achar PELO TEXTO
    clica_item(J, m, objeto, 2.6)
    depois = [t for t, *_ in explorador(J)]
    if depois.count(objeto) <= antes.count(objeto):
        raise RuntimeError(f"'{objeto}' nao apareceu no Explorador")
    return True


def botao_faixa(J, nome):
    p = monta.acha_botao(nome)
    if not p:
        raise RuntimeError(f"nao achei o botao '{nome}' na faixa")
    return p


def aba(J, nome):
    """Troca de aba da faixa. Acha pelo texto: a linha das abas desce quando a
       janela ganha barra de titulo."""
    def _faz():
        a, _ = rs.captura(J["id"], "/tmp/_abas.png")
        from PIL import Image as _I
        L, A = _I.open("/tmp/_abas.png").size
        for t, x, y, w, h in rs.ocr("/tmp/_abas.png", regiao=(0, 0, 1, 130 / A), psm="6", escala=2):
            alvo = "".join(c for c in t.strip().lower() if c.isalnum())
            if alvo == "".join(c for c in nome.lower() if c.isalnum()):
                rs.confere(); rs.clique_img(x + w // 2, y + h // 2, escala=2.0, janela=J)
                time.sleep(1.5)
                return True
        raise RuntimeError(f"nao achei a aba '{nome}'")
    return tentar(_faz, o_que=f"aba {nome}")


def linha_das_abas(J):
    """Devolve o y da barra de abas de documento (Place1 / Script)."""
    a, _ = rs.captura(J["id"], "/tmp/_lab.png")
    from PIL import Image as _I
    L, A = _I.open("/tmp/_lab.png").size
    for t, x, y, w, h in rs.ocr("/tmp/_lab.png", regiao=(0, 150 / A, 0.5, 340 / A),
                                psm="6", escala=3):
        alvo = t.strip().lower()
        if alvo.startswith("place") or alvo.startswith("script"):
            return (x + w // 2, y + h // 2)
    return None


def clica_faixa(J, nome, espera=1.8):
    p = botao_faixa(J, nome)
    rs.confere(); rs.clique_img(p[0], p[1], escala=2.0, janela=J); time.sleep(espera)
    return p


def nova_peca(J):
    """Cria uma Parte pela faixa e confere que nasceu."""
    antes = [t for t, *_ in explorador(J)]
    p = clica_faixa(J, "Parte", 2.4)
    depois = [t for t, *_ in explorador(J)]
    if depois.count("Part") <= antes.count("Part"):
        raise RuntimeError("a peca nao foi criada")
    return p


def limpa_popups(J):
    """Popup orfao (paleta, seletor de material, menu) engole o proximo clique.
       Duas escapadas e um clique no vazio devolvem o Studio ao normal."""
    rs.tecla(ESC); time.sleep(0.4)
    rs.tecla(ESC); time.sleep(0.4)
    rs.confere(); rs.clique_img(1000, 1600, escala=2.0, janela=J); time.sleep(0.6)
    rs.tecla(ESC); time.sleep(0.3)


def menu_contexto(J, x, y, tentativas=5):
    """Abre o menu do botao direito e devolve a janela dele. Tenta de novo:
       as vezes o primeiro clique so tira o foco de outro painel."""
    limpa_popups(J)
    for k in range(tentativas):
        ids = {j["id"] for j in rs.janelas()}
        rs.confere(); rs.clique_img(x, y, escala=2.0, janela=J); time.sleep(0.6)
        rs.confere(); rs.clique_direito_img(x, y, janela=J); time.sleep(2.2)
        m = [j for j in rs.janelas() if j["id"] not in ids and j["w"] > 120 and j["h"] > 120]
        if m:
            return m[0]
        rs.tecla(ESC); time.sleep(1.0)
    return None


def item_do_menu(m, rotulo, arquivo="/tmp/_menu.png"):
    """Acha um item do menu PELO TEXTO. O OCR devolve palavra por palavra,
       entao junto as palavras da MESMA LINHA antes de comparar."""
    rs.captura(m["id"], arquivo)
    itens = [(t.strip(), x, y, w, h) for t, x, y, w, h in
             rs.ocr(arquivo, psm="6", escala=2) if t.strip()]
    linhas = {}
    for t, x, y, w, h in itens:
        chave = round((y + h / 2) / 22)
        linhas.setdefault(chave, []).append((x, t, y, w, h))
    alvo = rotulo.lower()
    for chave, palavras in sorted(linhas.items()):
        palavras.sort()
        texto = " ".join(p[1] for p in palavras).lower()
        if texto.startswith(alvo) or alvo in texto:
            x, t, y, w, h = palavras[0]
            return (m["x"] + (x + w // 2) / 2, m["y"] + (y + h // 2) / 2)
    return None


def clica_item(J, m, rotulo, espera=1.6):
    p = item_do_menu(m, rotulo)
    if not p:
        raise RuntimeError(f"nao achei '{rotulo}' no menu")
    rs.confere(); rs.clique_tela(p[0], p[1]); time.sleep(espera)
    return p


def _renomeia1(J, de, para, n=0):
    """Renomeia pelo menu do botao direito do Explorador, e confere."""
    l = acha_linha(J, de, n)
    if not l:
        raise RuntimeError(f"nao achei '{de}' para renomear")
    rs.confere(); rs.clique_img(l[0], l[1], escala=2.0, janela=J); time.sleep(0.9)
    m = menu_contexto(J, l[0], l[1])
    if not m:
        raise RuntimeError("o menu do botao direito nao abriu")
    clica_item(J, m, "Renomear", 1.5)
    rs.digita_teclas(para)
    rs.tecla(ENTER); time.sleep(1.2)
    # o Enter nem sempre fecha a caixinha de edicao: clicar fora confirma
    ws = acha_linha(J, "Workspace")
    if ws:
        rs.confere(); rs.clique_img(ws[0], ws[1], escala=2.0, janela=J); time.sleep(0.9)
    l2 = acha_linha(J, para)
    if not l2:
        raise RuntimeError(f"nao virou '{para}' no Explorador")
    rs.confere(); rs.clique_img(l2[0], l2[1], escala=2.0, janela=J); time.sleep(0.9)
    # a caixinha de edicao some ao clicar fora; se o nome sobreviveu a isso, colou
    if not acha_linha(J, para):
        raise RuntimeError(f"'{para}' sumiu depois de clicar fora — a edicao nao confirmou")
    return True


def _enquadra1(J, nome, atras=6, n=0):
    """Poe a camera na peca (menu do botao direito -> Definir zoom em) e afasta.
       Sem isso a camera fica colada e a captura nao serve para aula."""
    l = acha_linha(J, nome, n)
    if not l:
        raise RuntimeError(f"nao achei '{nome}' para enquadrar")
    rs.confere(); rs.clique_img(l[0], l[1], escala=2.0, janela=J); time.sleep(0.9)
    m = menu_contexto(J, l[0], l[1])
    if not m:
        raise RuntimeError("o menu nao abriu para enquadrar")
    clica_item(J, m, "Definir zoom", 2.2)
    rs.confere(); rs.clique_img(1400, 1000, escala=2.0, janela=J); time.sleep(0.8)  # foco na viewport
    for _ in range(atras):
        rs.tecla(1); time.sleep(0.05)      # S = afasta
    time.sleep(1.0)
    return True


# ── cor e material ──────────────────────────────────────────────────────────
def pontos_cor(J):
    """Onde clicar para a cor: o ICONE aplica, a SETINHA ao lado abre a paleta.
       Tudo derivado do botao achado por texto — nada de coordenada fixa."""
    p = botao_faixa(J, "Cor")
    return {"aplicar": (p[0], p[1]), "seta": (p[0] + 44, p[1])}


def pontos_material(J):
    p = botao_faixa(J, "Material")
    return {"seta": (p[0] + 44, p[1])}


HEX = {"vermelho": (646, 332), "azul": (520, 119), "verde": (212, 190),
       "amarelo": (90, 332), "branco": (672, 679), "preto": (55, 679)}

# A COR de cada BrickColor que a aula pede. O hexagono se acha por ESTA cor,
# nao pela posicao: a posicao entregou 'EE Grime' no lugar de 'Bright green'
# numa captura da Aula 10 — o vizinho do verde na grade e um verde-oliva.
CORES = {
    "vermelho": ("Bright red",    (196,  40,  28)),
    "verde":    ("Bright green",  ( 75, 151,  75)),
    "azul":     ("Bright blue",   ( 13, 105, 172)),
    "amarelo":  ("Bright yellow", (245, 205,  48)),
    "branco":   ("White",         (242, 243, 243)),
    "preto":    ("Really black",  ( 27,  42,  53)),
}


def parece_nome(lido, esperado, minimo=0.75):
    """O painel diz o nome esperado? Comparo PALAVRA A PALAVRA com tolerancia,
       porque quem le e o OCR: 'Bright green' voltou como 'EB Bright greer' e
       um `in` exato reprovou uma pintura CERTA. A tolerancia e por palavra de
       proposito — 'Medium green' e 'Dark green' continuam sendo reprovados,
       porque a primeira palavra nao se parece com 'Bright'."""
    import difflib
    limpa = lambda t: "".join(c if c.isalpha() or c.isspace() else " " for c in t.lower()).split()
    palavras = limpa(lido)
    for alvo in limpa(esperado):
        if not any(difflib.SequenceMatcher(None, alvo, p).ratio() >= minimo for p in palavras):
            return False
    return True


def acha_hexagono(pal, cor, arquivo="/tmp/_hex.png"):
    """Onde, DENTRO da paleta, esta o hexagono da cor pedida. Devolve (x, y)
       em pixels da captura da paleta, ou None.

       Mede em vez de decorar: procuro os pixels da cor exata do BrickColor,
       fico com o aglomerado mais denso e devolvo o centro dele. A grade da
       paleta muda de lugar com o tamanho da janela; a cor nao muda."""
    import numpy as _np
    rs.captura(pal["id"], arquivo)
    im = _np.asarray(Image.open(arquivo).convert("RGB"), dtype=int)
    alvo = _np.array(CORES[cor][1])
    A, L = im.shape[0], im.shape[1]
    # a grade vai ate ~90% da altura; embaixo ficam o interruptor e os botoes
    corpo = im[: int(A * 0.88), :, :]
    for tol in (10, 18, 28, 40):
        mask = (_np.abs(corpo - alvo) <= tol).all(axis=2)
        if mask.sum() < 60:
            continue
        ys, xs = _np.nonzero(mask)
        # o hexagono e um bloco compacto: fico com o maior grupo em x e em y
        for _ in range(3):
            cx, cy = _np.median(xs), _np.median(ys)
            perto = (_np.abs(xs - cx) < 40) & (_np.abs(ys - cy) < 40)
            if perto.sum() < 40:
                break
            xs, ys = xs[perto], ys[perto]
        if len(xs) >= 40:
            return int(_np.median(xs)), int(_np.median(ys))
    return None


def paleta_aberta(J):
    return [j for j in rs.janelas() if j["w"] == 368 and j["h"] == 400]


def pinta(J, cor, espera_nome=None):
    """Setinha do Cor abre a paleta -> hexagono ARMA -> botao Cor APLICA.
       O interruptor 'clique no objeto' tem de ficar DESLIGADO."""
    def _faz():
        if not paleta_aberta(J):
            rs.confere(); rs.clique_img(1990, 118, escala=2.0, janela=J); time.sleep(2.0)
        p = paleta_aberta(J)
        if not p:
            raise RuntimeError("a paleta de cores nao abriu")
        p = p[0]
        rs.captura(p["id"], "/tmp/_tg.png")
        q = np.asarray(Image.open("/tmp/_tg.png").convert("RGB"), dtype=int)[730:780, 630:710]
        ligado = ((q[:, :, 1] > 120) & (q[:, :, 1] - q[:, :, 0] > 40) & (q[:, :, 1] - q[:, :, 2] > 40)).sum() > 200
        if ligado:
            rs.confere(); rs.clique_lento(p["x"] + 665 / 2, p["y"] + 755 / 2); time.sleep(1.2)
        hx = acha_hexagono(p, cor) or HEX[cor]
        rs.confere(); rs.clique_tela(p["x"] + hx[0] / 2, p["y"] + hx[1] / 2); time.sleep(1.5)
        rs.confere(); rs.clique_img(1946, 118, escala=2.0, janela=J); time.sleep(2.0)
        bc = linha_prop(J, "BrickColor")
        if espera_nome and not parece_nome(bc, espera_nome):
            raise RuntimeError(f"BrickColor ficou '{bc}', esperava {espera_nome}")
        return bc
    return tentar(_faz, o_que=f"pintar de {cor}")


def _painel_propriedades(J, arquivo="/tmp/_prop.png"):
    """Le o painel Propriedades ACHANDO o cabecalho dele. Regiao fixa nao serve:
       abrir a Saida encolhe o painel e empurra tudo para cima."""
    rs.captura(J["id"], arquivo)
    itens = [(t.strip(), x, y, w, h) for t, x, y, w, h in
             rs.ocr(arquivo, regiao=(0.855, 0.13, 1, 1.0), psm="6", escala=3) if t.strip()]
    topo = [i for i in itens if i[0].lower().startswith("propriedade")]
    y0 = min((i[2] for i in topo), default=0)
    return [i for i in itens if i[2] > y0]


def linha_prop(J, rotulo):
    """Le uma linha do painel Propriedades PELO ROTULO. O realce da selecao
       lava a cor na captura, entao a propriedade e a fonte de verdade.

       Le duas vezes: a varredura do painel inteiro e um recorte ESTREITO da
       celula, ampliado e binarizado. A varredura larga perde o fim do valor —
       'Bright yellow' voltava como 'Bright' e reprovava uma pintura certa,
       o mesmo defeito do OCR do editor."""
    itens = _painel_propriedades(J)
    alvo = [i for i in itens if i[0].lower().rstrip(".") == rotulo.lower()]
    if not alvo:
        return ""
    _, ax, ay, aw, ah = alvo[0]
    largo = " ".join(t for t, x, y, w, h in itens
                     if abs((y + h // 2) - (ay + ah // 2)) < ah and x > ax + aw)
    estreito = _celula_ampliada(J, ax + aw, ay, ah)
    return estreito if len(estreito) > len(largo) else largo


def _celula_ampliada(J, x0, y, h, arquivo="/tmp/_celamp.png"):
    """A celula de valor, so ela, ampliada 4x e binarizada."""
    from PIL import Image as _I
    try:
        a, _ = rs.captura(J["id"], arquivo)
        im = _I.open(a).convert("L").crop((x0, max(0, y - 12), 2940, y + h + 12))
        if im.width < 40 or im.height < 10:
            return ""
        im = im.resize((im.width * 4, im.height * 4), _I.LANCZOS)
        im.save("/tmp/_celamp_big.png")
        lido = [t.strip() for t, *_ in rs.ocr("/tmp/_celamp_big.png", psm="7",
                                              escala=1, limiar=90) if t.strip()]
        return " ".join(lido)
    except Exception:
        return ""


def ponto_da_prop2(J, rotulo):
    itens = _painel_propriedades(J)
    alvo = [i for i in itens if i[0].lower().rstrip(".") == rotulo.lower()]
    if not alvo:
        return None
    _, ax, ay, aw, ah = alvo[0]
    return (ax + aw + 190, ay + ah // 2)


def fecha_saida(J):
    """Fecha o painel Saida — ele encolhe as Propriedades e suja as fotos."""
    aba(J, "Script")
    a, _ = rs.captura(J["id"], "/tmp/_sa.png")
    for t, x, y, w, h in rs.ocr("/tmp/_sa.png", regiao=(0, 0.055, 1, 0.115), psm="11"):
        if t.strip().lower().startswith("sa") and len(t.strip()) <= 6:
            rs.confere(); rs.clique_img(x + w // 2, 118, escala=2.0, janela=J); time.sleep(1.6)
            break
    aba(J, "Modelo")
    return True


def material(J, nome):
    """Seletor de materiais: limpa a busca (ela guarda o texto), digita,
       confere o foco antes, e aplica."""
    def _faz():
        rs.confere(); rs.clique_img(1885, 118, escala=2.0, janela=J); time.sleep(2.2)
        mp = [j for j in rs.janelas() if j.get("nome") == "MaterialPicker"]
        if not mp:
            raise RuntimeError("o seletor de materiais nao abriu")
        p = mp[0]
        rs.confere(); rs.clique_tela(p["x"] + 528 / 2, p["y"] + 40 / 2); time.sleep(1.0)  # limpa
        for _ in range(3):
            rs.confere(); rs.clique_tela(p["x"] + 280 / 2, p["y"] + 40 / 2); time.sleep(1.0)
            rs.captura(p["id"], "/tmp/_bf.png")
            a = np.asarray(Image.open("/tmp/_bf.png").convert("RGB"), dtype=int)[14:70, 10:550]
            if ((a[:, :, 2] > 150) & (a[:, :, 2] - a[:, :, 0] > 50)).sum() > 300:
                break
        else:
            raise RuntimeError("a caixa de busca do material nao pegou o foco")
        rs.digita_teclas(nome.lower()); time.sleep(1.8)
        rs.confere(); rs.clique_tela(p["x"] + 88 / 2, p["y"] + 228 / 2); time.sleep(2.4)
        m = linha_prop(J, "Material")
        if nome.lower() not in m.lower():
            raise RuntimeError(f"Material ficou '{m}', esperava {nome}")
        return m
    return tentar(_faz, o_que=f"material {nome}")


def ancora(J):
    p = clica_faixa(J, "Âncora", 1.8)
    return p


# ── script ──────────────────────────────────────────────────────────────────
def insere_script(J, pai):
    """Insere um Script dentro da peca pelo '+' do Explorador."""
    tentar(lambda: insere_em(J, pai, "Script"), o_que="inserir Script")
    time.sleep(1.5)
    return True


def escreve(J, codigo, tem=()):
    return tentar(lambda: rs.escreve_codigo(J, codigo, tem=tem), o_que="escrever o codigo")


# ── jogar ───────────────────────────────────────────────────────────────────
def botoes_jogo(J):
    """O ▶ e o ■ ficam na barra de cima, a direita da palavra 'Teste'.
       A barra desce quando a janela ganha barra de titulo, entao a linha se
       descobre pela propria palavra."""
    a, _ = rs.captura(J["id"], "/tmp/_bj.png")
    from PIL import Image as _I
    L, A = _I.open("/tmp/_bj.png").size
    for t, x, y, w, h in rs.ocr("/tmp/_bj.png", regiao=(0, 0, 0.3, 160 / A), psm="6", escala=2):
        if t.strip().lower().startswith("teste"):
            cy = y + h // 2
            return {"play": (x + 165, cy), "stop": (x + 317, cy)}
    return {"play": (225, 28), "stop": (377, 28)}


def em_teste(J):
    """Esta rodando? Em modo de teste aparece NetworkClient no Explorador."""
    a = monta.cap("_play")
    from PIL import Image as _I
    L, A = _I.open(a).size
    return any("NetworkClient" in t for t, *_ in
               rs.ocr(a, regiao=(0.855, 150 / A, 1, 1100 / A), psm="6", escala=2))


def joga(J, espera=7.5):
    """O ▶ fica na barra de cima. A coluna varia um pouco entre versoes e
       layouts, entao tento algumas e confirmo pelo NetworkClient."""
    b = botoes_jogo(J)
    cy = b["play"][1]
    for cx in (b["play"][0], 225, 250, 200, 275):
        rs.confere(); rs.clique_img(cx, cy, escala=2.0, janela=J); time.sleep(espera)
        if em_teste(J):
            return True
        time.sleep(1.0)
    raise RuntimeError("nao entrou em modo de teste")


def para(J, espera=6.0):
    """O ■ tambem muda de coluna entre layouts: tento algumas e confirmo."""
    b = botoes_jogo(J)
    cy = b["stop"][1]
    for cx in (b["stop"][0], 377, 400, 349):
        rs.confere(); rs.clique_img(cx, cy, escala=2.0, janela=J); time.sleep(espera)
        if not em_teste(J):
            return True
    return False


def enquadra(J, nome, atras=6, n=0):
    return tentar(lambda: _enquadra1(J, nome, atras, n), n=4, o_que=f"enquadrar {nome}")


def renomeia(J, de, para, n=0):
    return tentar(lambda: _renomeia1(J, de, para, n), n=4, o_que=f"renomear {de}")


def ponto_da_prop(J, rotulo):
    """Devolve o ponto do CAMPO DE VALOR de uma linha do painel Propriedades."""
    rs.captura(J["id"], "/tmp/_pp.png")
    itens = [(t.strip(), x, y, w, h) for t, x, y, w, h in
             rs.ocr("/tmp/_pp.png", regiao=(0.855, 0.55, 1, 1.0), psm="6", escala=3) if t.strip()]
    alvo = [i for i in itens if i[0].lower().rstrip(".") == rotulo.lower()]
    if not alvo:
        return None
    _, ax, ay, aw, ah = alvo[0]
    return (ax + aw + 190, ay + ah // 2)      # coluna da direita, na mesma linha


def poe_propriedade(J, rotulo, valor, confere=True):
    """Escreve um valor numa propriedade. Duplo clique abre a edicao;
       o campo ja vem selecionado, entao digitar troca."""
    def _faz():
        p = ponto_da_prop(J, rotulo)
        if not p:
            raise RuntimeError(f"nao achei a propriedade '{rotulo}'")
        rs.confere(); rs.clique_img(p[0], p[1], escala=2.0, janela=J, duplo=True); time.sleep(0.9)
        rs.digita_teclas(str(valor))
        rs.tecla(ENTER); time.sleep(1.2)
        if confere:
            lido = linha_prop(J, rotulo)
            primeiro = str(valor).split(",")[0].strip()
            if primeiro not in lido.replace(" ", ""):
                raise RuntimeError(f"{rotulo} ficou '{lido}', esperava {valor}")
        return True
    return tentar(_faz, o_que=f"propriedade {rotulo}")


def abre_editor(J, nome="Script"):
    """Clica na ABA do editor. Selecionar o Script no Explorador NAO traz o
       editor para a frente — os cliques iam parar no mundo 3D."""
    def _faz():
        a, _ = rs.captura(J["id"], "/tmp/_tabs.png")
        from PIL import Image as _I
        L, A = _I.open("/tmp/_tabs.png").size
        for t, x, y, w, h in rs.ocr("/tmp/_tabs.png", regiao=(0, 150 / A, 0.5, 340 / A),
                                    psm="6", escala=3):
            if t.strip().lower().startswith(nome.lower()[:5]):
                rs.confere(); rs.clique_img(x + w // 2, y + h // 2, escala=2.0, janela=J)
                time.sleep(1.6)
                if "print" in rs.texto_do_editor(J).lower() or "local" in rs.texto_do_editor(J).lower():
                    return True
                return True
        raise RuntimeError(f"nao achei a aba '{nome}'")
    return tentar(_faz, o_que="abrir a aba do editor")


def mostrando_mundo(J):
    """O mundo 3D esta a vista? Antes eu media o brilho do ceu, mas isso falha
       com a camera apontada para o chao. Agora pergunto ao proprio editor:
       se da para ler codigo na tela, e porque o editor esta na frente."""
    txt = rs.texto_do_editor(J).lower()
    marcas = ("local ", "game.", "script.parent", "function(", "end)", "print(")
    return not any(m in txt for m in marcas)


def volta_ao_mundo(J):
    """Volta para a aba do lugar. A primeira aba fica sempre na esquerda;
       OCR nessa tira e pouco confiavel, entao confiro pelo CEU aparecer."""
    def _faz():
        a, _ = rs.captura(J["id"], "/tmp/_lab2.png")
        from PIL import Image as _I
        L, A = _I.open("/tmp/_lab2.png").size
        alvos = [(x + w // 2, y + h // 2) for t, x, y, w, h in
                 rs.ocr("/tmp/_lab2.png", regiao=(0, 150 / A, 0.5, 340 / A), psm="6", escala=3)
                 if t.strip().lower().startswith("place")]
        for pt in alvos + [(70, 213), (70, 277)]:
            rs.confere(); rs.clique_img(pt[0], pt[1], escala=2.0, janela=J); time.sleep(1.5)
            if mostrando_mundo(J):
                return True
        raise RuntimeError("nao consegui voltar para o mundo 3D")
    return tentar(_faz, o_que="voltar ao mundo")


FILTRO_PROP = (2700, 879)      # caixa "Propriedades de filtro"


def nada_selecionado(J):
    """Tira a selecao. Regra de ouro deste arquivo: so aperto Delete perto de
       um campo de texto DEPOIS de esvaziar a selecao — se o foco escapar,
       o Delete nao tem o que apagar."""
    rs.tecla(ESC); time.sleep(0.4)
    rs.confere(); rs.clique_img(1000, 1650, escala=2.0, janela=J); time.sleep(0.5)
    rs.tecla(ESC); time.sleep(0.4)


def acha_filtro(J):
    """Onde fica a caixa 'Propriedades de filtro'.
       Com o rotulo a vista, ele E a caixa. Quando ha texto digitado o rotulo
       some, e ai a referencia passa a ser o CABECALHO do painel + uma linha."""
    a, _ = rs.captura(J["id"], "/tmp/_fl.png")
    itens = [(t.strip(), x, y, w, h) for t, x, y, w, h in
             rs.ocr("/tmp/_fl.png", regiao=(0.855, 0.13, 1, 1.0), psm="6", escala=3) if t.strip()]
    for t, x, y, w, h in itens:
        if "filtro" in t.lower():
            return (x + 120, y + h // 2)
    cab = [i for i in itens if i[0].lower().startswith("propriedade")]
    if cab:
        cab.sort(key=lambda i: i[2])
        _, cx, cy, cw, ch = cab[0]
        return (cx + 120, cy + ch + 30)
    return FILTRO_PROP


def escreve_no_filtro(J, texto):
    """Troca o texto do filtro. NUNCA usa Cmd+A: no Studio isso seleciona os
       OBJETOS da cena, e o Delete seguinte apaga tudo (ja aconteceu aqui).
       Clique triplo seleciona so o texto do campo."""
    nada_selecionado(J)
    fx, fy = acha_filtro(J)
    rs.confere(); rs.clique_img(fx, fy, escala=2.0, janela=J); time.sleep(0.5)
    rs.confere(); rs.clique_img(fx, fy, escala=2.0, janela=J, duplo=True); time.sleep(0.5)
    rs.tecla(DEL); time.sleep(0.4)          # seguro: nada selecionado na cena
    for _ in range(14):
        rs.tecla_rapida(DEL) if hasattr(rs, "tecla_rapida") else rs.tecla(DEL)
    time.sleep(0.3)
    if texto:
        rs.digita_teclas(texto)
    time.sleep(1.5)
    return True


def limpa_filtro(J):
    return escreve_no_filtro(J, "")


def divisor(J, para_y):
    """Move a divisoria entre Explorador e Propriedades. Os dois nunca cabem
       grandes ao mesmo tempo: seleciono com o Explorador alto e edito com o
       painel de Propriedades alto."""
    f = acha_filtro(J)
    if abs(f[1] - 70 - para_y) < 40:
        return f
    rs.confere(); rs.arrasta_img(2740, f[1] - 70, 2740, para_y, escala=2.0, janela=J)
    time.sleep(1.4)
    return acha_filtro(J)


def poe_prop_filtrada(J, alvo_nome, propriedade, valor):
    """Escreve numa propriedade que so aparece com filtro (Size, Position).
       Ordem importa: filtro com nada selecionado (Delete seguro), depois
       seleciona, depois cresce o painel, edita, e devolve o tamanho."""
    def _faz():
        divisor(J, 830)
        escreve_no_filtro(J, propriedade.lower())
        seleciona(J, alvo_nome)
        divisor(J, 380)
        itens = _painel_propriedades(J)
        y_filtro = acha_filtro(J)[1]
        itens = [i for i in itens if i[2] > y_filtro + 25]
        pref = propriedade.lower()[:4]
        alvo = None
        for t, x, y, w, h in itens:
            rot = t.strip().lower().rstrip(".")
            if rot.startswith(pref) and len(rot) <= len(propriedade) + 1:
                alvo = (x + w + 160, y + h // 2); break
        if not alvo:
            for t, x, y, w, h in itens:
                if re.fullmatch(r"-?[\d.]+\s*,\s*-?[\d.]+\s*,\s*-?[\d.]+", t.strip()):
                    alvo = (x + w // 2 + 40, y + h // 2); break
        if not alvo:
            raise RuntimeError(f"o filtro nao mostrou '{propriedade}' "
                               f"(li: {[i[0] for i in itens][:8]})")
        rs.confere(); rs.clique_img(alvo[0], alvo[1], escala=2.0, janela=J, duplo=True); time.sleep(0.9)
        rs.confere(); rs.clique_img(alvo[0], alvo[1], escala=2.0, janela=J, duplo=True); time.sleep(0.6)
        rs.digita_teclas(str(valor)); time.sleep(0.3)
        rs.tecla(ENTER); time.sleep(1.6)
        alvo_txt = str(valor).replace(" ", "").replace(",", "")
        ok = False
        for k in range(3):
            lido = " ".join(t for t, *_ in _painel_propriedades(J))
            if alvo_txt in lido.replace(" ", "").replace(",", ""):
                ok = True; break
            time.sleep(1.0)
        if not ok:
            raise RuntimeError(f"{propriedade} nao ficou {valor}")
        return True
    try:
        return tentar(_faz, o_que=f"{propriedade}={valor}")
    finally:
        divisor(J, 830)
        escreve_no_filtro(J, "")


def expande_workspace(J):
    """Abre a arvore do Workspace. Em projeto novo ela vem fechada, e sem isso
       o Explorador nao mostra Baseplate nem SpawnLocation."""
    for k in range(3):
        if acha_linha(J, "Baseplate", tentativas=1):
            return True
        l = acha_linha(J, "Workspace", tentativas=2)
        if not l:
            raise RuntimeError("nao achei Workspace no Explorador")
        rs.confere(); rs.clique_img(l[0] - 130, l[1], escala=2.0, janela=J); time.sleep(1.4)
    return bool(acha_linha(J, "Baseplate", tentativas=2))


def le_celula(J, y, arquivo="/tmp/_cel.png"):
    """Le a celula de valor de uma linha do painel, num recorte pequeno e
       ampliado. O OCR da linha inteira perde texto perto da borda de baixo."""
    from PIL import Image as _I
    a, _ = rs.captura(J["id"], arquivo)
    im = _I.open(a).convert("L").crop((2680, max(0, y - 20), 2940, y + 20))
    im = im.resize((im.width * 5, im.height * 5), _I.LANCZOS)
    im.save("/tmp/_cel_big.png")
    return " ".join(t.strip() for t, *_ in rs.ocr("/tmp/_cel_big.png", psm="7", escala=1))


def poe_prop(J, alvo_nome, propriedade, valor, n=0):
    """Escreve uma propriedade usando a caixa de filtro, SEM mexer em divisoria
       (mexer nela ja quebrou o layout uma vez). Ordem: filtro com nada
       selecionado (Delete seguro), depois seleciona, depois edita."""
    def _faz():
        escreve_no_filtro(J, propriedade.lower())
        seleciona(J, alvo_nome, n)
        y_filtro = acha_filtro(J)[1]
        itens = [i for i in _painel_propriedades(J) if i[2] > y_filtro + 25]
        pref = propriedade.lower()[:4]
        alvo = None
        for t, x, y, w, h in itens:
            rot = t.strip().lower().rstrip(".")
            if rot.startswith(pref) and len(rot) <= len(propriedade) + 1:
                alvo = (x + w + 160, y + h // 2); break
        if not alvo:
            for t, x, y, w, h in itens:
                if re.fullmatch(r"-?[\d.]+\s*,\s*-?[\d.]+\s*,\s*-?[\d.]+", t.strip()):
                    alvo = (x + w // 2 + 40, y + h // 2); break
        if not alvo:
            raise RuntimeError(f"o filtro nao mostrou '{propriedade}' "
                               f"(li {[i[0] for i in itens][:8]})")
        antes_img = rs.captura(J["id"], "/tmp/_pv_a.png")[0]
        rs.confere(); rs.clique_img(alvo[0], alvo[1], escala=2.0, janela=J, duplo=True); time.sleep(0.9)
        # Cmd+A aqui pega o texto do campo. E seguro porque logo depois eu
        # DIGITO (que substitui) — nunca um Delete, que apagaria a cena.
        rs.tecla(0, cmd=True); time.sleep(0.25)
        rs.digita_teclas(str(valor)); time.sleep(0.3)
        rs.tecla(ENTER); time.sleep(1.6)
        # depois do Enter a selecao costuma se perder e o painel esvazia:
        # reselecionar antes de reler, senao eu reprovo uma edicao que deu certo
        # o OCR do painel falha perto da borda de baixo. A prova boa e a PECA:
        # mudar Size ou Position muda a imagem do mundo 3D.
        alvo_txt = str(valor).replace(" ", "").replace(",", "")
        for k in range(3):
            time.sleep(0.8)
            lido = " ".join(t for t, *_ in _painel_propriedades(J))
            if alvo_txt in lido.replace(" ", "").replace(",", "").replace(".", ""):
                return True
        # leitura apertada da celula de valor: o OCR da linha inteira falha
        # perto da borda do painel, mas num recorte pequeno e ampliado ele le
        cel = le_celula(J, alvo[1]).replace(" ", "").replace(",", "").replace(".", "")
        # o OCR do recorte as vezes perde o primeiro numero ("12,14,1" -> "14,1"):
        # aceitar quando o que foi lido e o FIM do valor que eu escrevi
        if cel and (alvo_txt in cel or (len(cel) >= 3 and alvo_txt.endswith(cel))):
            return True
        import monta
        depois_img = rs.captura(J["id"], "/tmp/_pv_b.png")[0]
        m = monta.mudou(antes_img, depois_img, regiao=VIEW, passo=4)
        if m and (m[4] - m[2]) > 25:
            return True
        raise RuntimeError(f"{propriedade} nao ficou {valor} — celula lida: {cel!r}")
    try:
        return tentar(_faz, o_que=f"{propriedade}={valor}")
    finally:
        escreve_no_filtro(J, "")


def sem_acento(t):
    for a, b in zip("aaaaeeiooouuc", "áàâãéêíóôõúüç"):
        t = t.replace(b, a)
    return t


def texto_na_tela(J, palavra, regiao=(0.02, 0.12, 0.78, 0.55)):
    """A palavra esta escrita no mundo 3D? Serve para provar em JOGO o que o
       aluno vai ver — o letreiro, o aviso, o cronometro. Le com e sem
       binarizacao: o letreiro e claro sobre o ceu claro numa hora e escuro
       sobre a lava noutra, e um limiar so perde metade dos casos."""
    a, _ = rs.captura(J["id"], "/tmp/_tela.png")
    lido = []
    for lim in (None, 90, 150):
        lido += [t for t, *_ in rs.ocr(a, regiao=regiao, psm="6", escala=2, limiar=lim)]
    j = sem_acento(" ".join(lido).lower())
    return sem_acento(palavra.lower()) in j


def marca_prop(J, alvo_nome, propriedade, caminho_lua, quero=True):
    """Marca (ou desmarca) uma caixinha de propriedade — TextScaled, Enabled,
       Neutral. O painel nao diz por OCR se a caixa esta marcada; quem responde
       e a propria propriedade, lida pela barra de comando. Por isso o
       caminho_lua e obrigatorio: e o invariante, o pixel seria proxy."""
    def _faz():
        escreve_no_filtro(J, propriedade.lower())
        seleciona(J, alvo_nome)
        y_filtro = acha_filtro(J)[1]
        itens = [i for i in _painel_propriedades(J) if i[2] > y_filtro + 25]
        pref = propriedade.lower()[:6]
        alvo = None
        for t, x, y, w, h in itens:
            rot = t.strip().lower().rstrip(".")
            if rot.startswith(pref):
                alvo = (x + w + 60, y + h // 2); break
        if not alvo:
            raise RuntimeError(f"o filtro nao mostrou '{propriedade}' "
                               f"(li {[i[0] for i in itens][:8]})")
        if le_bool(J, caminho_lua) != quero:
            rs.confere(); rs.clique_img(alvo[0], alvo[1], escala=2.0, janela=J)
            time.sleep(1.2)
        lido = le_bool(J, caminho_lua)
        if lido != quero:
            raise RuntimeError(f"{propriedade} ficou {lido}, eu queria {quero}")
        return True
    try:
        return tentar(_faz, o_que=f"marcar {propriedade}")
    finally:
        escreve_no_filtro(J, "")


def le_bool(J, caminho_lua):
    """Le uma propriedade booleana pela barra de comando. Devolve True/False.
       Imprime um SELO junto do valor: sem ele, uma saida velha na janela
       responderia pela nova (a saida so cresce, ninguem a limpa)."""
    selo = f"SELO{int(time.time() * 1000) % 100000}"
    rs.comando_lua(J, f'print("{selo}", tostring({caminho_lua}))', espera=1.6)
    linha = rs.linha_da_saida(J, selo)
    if linha is None:
        raise RuntimeError(f"a barra de comando nao respondeu sobre {caminho_lua}")
    b = linha.lower()
    if "true" in b:
        return True
    if "false" in b:
        return False
    raise RuntimeError(f"nao entendi a resposta sobre {caminho_lua}: {linha!r}")


def janela_de_verdade(nome_janela, J):
    """A lista do sistema guarda janelas FANTASMA (fechadas mas ainda listadas).
       Clicar nelas manda o clique para a janela de tras — ja me enganou.
       Confiro comparando a captura da tela inteira com a da janela principal."""
    import subprocess, tempfile
    cand = [j for j in rs.janelas() if j.get("nome") == nome_janela]
    if not cand:
        return None
    p = cand[0]
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
        tela = f.name
    subprocess.run(["screencapture", "-x", tela], check=True)
    t = Image.open(tela).convert("RGB")
    m = Image.open(rs.captura(J["id"], "/tmp/_jprin.png")[0]).convert("RGB")
    # regiao onde a janela diz estar, nas duas imagens
    cx, cy = int((p["x"] + p["w"] / 2) * 2), int((p["y"] + p["h"] / 2) * 2)
    a = np.asarray(t.crop((cx - 120, cy - 60, cx + 120, cy + 60)), dtype=int)
    mx, my = cx, cy - int(J["y"] * 2)
    b = np.asarray(m.crop((mx - 120, my - 60, mx + 120, my + 60)), dtype=int)
    if a.shape != b.shape:
        return p
    difere = float(np.abs(a - b).mean())
    return p if difere > 6 else None


def expande(J, nome):
    """Abre a arvore de um item do Explorador clicando no triangulo."""
    l = acha_linha(J, nome, tentativas=2)
    if not l:
        return False
    rs.confere(); rs.clique_img(l[0] - (l[2] - l[0]) - 60, l[1], escala=2.0, janela=J)
    time.sleep(1.2)
    return True


def script_de(J, dono):
    """Acha a linha do Script que mora dentro de 'dono'. Confere pelo campo
       Parent — ha varios itens chamados 'Script' na arvore."""
    expande(J, dono)
    for t, x, y, w, h in explorador(J, regiao=(0.855, 0.13, 1, 0.92)):
        if "".join(c for c in t.lower() if c.isalnum()) != "script":
            continue
        rs.confere(); rs.clique_img(x + w // 2, y + h // 2, escala=2.0, janela=J); time.sleep(1.1)
        pai = "".join(c for c in linha_prop(J, "Parent").lower() if c.isalnum())
        if pai and (dono.lower().startswith(pai[:10]) or pai.startswith(dono.lower()[:10])):
            return (x + w // 2, y + h // 2)
    return None


def busca_explorador(J, texto):
    """Filtra o Explorador. Resolve dois problemas de uma vez: a lista rolada
       para fora da vista e itens com o mesmo nome em lugares diferentes."""
    a, _ = rs.captura(J["id"], "/tmp/_be.png")
    cx = cy = None
    for t, x, y, w, h in rs.ocr("/tmp/_be.png", regiao=(0.855, 0.10, 1, 0.30), psm="6", escala=2):
        if t.strip().lower().startswith("pesquis"):
            cx, cy = x + w + 40, y + h // 2; break
    if cx is None:
        cx, cy = 2640, 250
    rs.confere(); rs.clique_img(cx, cy, escala=2.0, janela=J); time.sleep(0.8)
    rs.tecla(0, cmd=True); time.sleep(0.2)
    if texto:
        rs.digita_teclas(texto)
    else:
        rs.tecla(DEL)
    time.sleep(1.8)
    return True


def fecha_abas_de_script(J, limite=8):
    """Fecha as abas de editor abertas. Com varias abas 'Script' abertas eu
       escrevia na aba errada e o script novo ficava com o codigo padrao —
       foi o que estragou a Aula 5 duas vezes."""
    for k in range(limite):
        a, _ = rs.captura(J["id"], "/tmp/_tabs.png")
        alvo = None
        from PIL import Image as _I
        L, A = _I.open("/tmp/_tabs.png").size
        for t, x, y, w, h in rs.ocr("/tmp/_tabs.png", regiao=(0, 150 / A, 0.6, 340 / A),
                                    psm="6", escala=3):
            if t.strip().lower().startswith("script"):
                alvo = (x + w + 26, y + h // 2); break
        if not alvo:
            return True
        rs.confere(); rs.clique_img(alvo[0], alvo[1], escala=2.0, janela=J); time.sleep(1.2)
    return False


def abas_abertas(J):
    a, _ = rs.captura(J["id"], "/tmp/_tabs2.png")
    return [t.strip() for t, *_ in rs.ocr("/tmp/_tabs2.png", regiao=(0, 0.100, 0.55, 0.128),
                                          psm="6", escala=3) if t.strip()]


def limpa_saida(J):
    """Esvazia o painel Saida. Sem isso eu lia mensagens de execucoes ANTIGAS
       e concluia que o script atual tinha rodado — ou nao tinha."""
    for k in range(3):
        rs.confere(); rs.clique_img(2847, 1397, escala=2.0, janela=J); time.sleep(1.4)
        a, _ = rs.captura(J["id"], "/tmp/_so.png")
        sobrou = [t for t, *_ in rs.ocr("/tmp/_so.png", regiao=(0, 0.78, 0.6, 0.95),
                                        psm="6", escala=2) if len(t.strip()) > 3]
        if not sobrou:
            return True
    return False

def menu_do_mais(J, pai, n=0):
    """Abre o menu do '+' de uma linha do Explorador e devolve (linha, janela).
       O '+' fica logo depois do nome, mas o OCR as vezes o engole: varrer."""
    l = seleciona(J, pai, n)
    for dx in (30, -15, 60, 5):
        ids = {j["id"] for j in rs.janelas()}
        rs.confere(); rs.clique_img(l[2] + dx, l[1], escala=2.0, janela=J); time.sleep(2.2)
        achados = [j for j in rs.janelas()
                   if j["id"] not in ids and j["w"] > 150 and j["h"] > 150]
        if achados:
            return l, achados[0], l[2] + dx
        rs.tecla(ESC); time.sleep(0.5)
    raise RuntimeError(f"o menu do '+' de {pai} nao abriu")


def insere_buscando(J, pai, objeto, n=0):
    """Insere um objeto que NAO esta na lista curta do '+': escreve o nome na
       caixa 'Pesquisar objeto' do menu e clica no resultado. E assim que o
       aluno acha o SpawnLocation."""
    antes = [t for t, *_ in explorador(J)]
    l, m, usado = menu_do_mais(J, pai, n)
    # a caixa de busca e a primeira linha do menu
    rs.confere(); rs.clique_tela(m["x"] + m["w"] / 2, m["y"] + 14); time.sleep(0.8)
    rs.digita_teclas(objeto.lower()[:9]); time.sleep(1.6)
    alvo = item_do_menu(m, objeto)
    if not alvo:
        raise RuntimeError(f"a busca do menu nao achou '{objeto}'")
    rs.confere(); rs.clique_tela(*alvo); time.sleep(2.6)
    depois = [t for t, *_ in explorador(J)]
    if depois.count(objeto) <= antes.count(objeto):
        raise RuntimeError(f"'{objeto}' nao apareceu no Explorador")
    return True
