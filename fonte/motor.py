#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Motor de captura das aulas com script. Recebe uma receita e produz as
   fotos, os pares para os clipes e o alvos.json — conferindo cada passo."""
import time, json, os, rs, monta, estudio as E
from PIL import Image
import numpy as np


class Aula:
    def __init__(self, pasta):
        self.D = pasta
        os.makedirs(pasta, exist_ok=True)
        self.ALVOS = f"{pasta}/alvos.json"
        self.J = None

    # ── base ────────────────────────────────────────────────────────────
    def liga(self):
        self.J = E.liga()
        return self.J

    def cap(self, n):
        rs.captura(monta.JAN["id"], f"{self.D}/{n}.png")
        return f"{n}.png"

    def reg(self, nome, **kw):
        A = json.load(open(self.ALVOS)) if os.path.exists(self.ALVOS) else {}
        A[nome] = {k: (list(v) if isinstance(v, tuple) else v) for k, v in kw.items()}
        json.dump(A, open(self.ALVOS, "w"), indent=1, ensure_ascii=False)
        print(f"  ok {nome}")

    def projeto_novo(self):
        rs.ativa(); time.sleep(0.8)
        rs.menu(["Arquivo", "Novo"]); time.sleep(13.0)
        self.liga()
        E.limpa_popups(self.J)
        E.expande_workspace(self.J)
        return True

    # ── passos reutilizaveis ────────────────────────────────────────────
    def aba_modelo(self, tag="s_aba"):
        a = self.cap(tag + "_a"); E.aba(self.J, "Modelo"); self.cap(tag + "_b")
        self.reg("aba_modelo", antes=tag + "_a.png", depois=tag + "_b.png", alvo=[1639, 36])

    def cria_peca(self, tag="s_criar"):
        a = self.cap(tag + "_a"); p = E.botao_faixa(self.J, "Parte")
        E.nova_peca(self.J); self.cap(tag + "_b")
        self.reg("criar", antes=tag + "_a.png", depois=tag + "_b.png", alvo=p)

    def enquadra(self, nome="Part", atras=7, foto="p_camera"):
        E.enquadra(self.J, nome, atras=atras)
        self.cap(foto)

    def ancora(self, alvo="Part", tag="s_ancora"):
        E.seleciona(self.J, alvo)
        a = self.cap(tag + "_a"); p = E.botao_faixa(self.J, "Âncora")
        E.ancora(self.J); self.cap(tag + "_b")
        self.reg("ancorar", antes=tag + "_a.png", depois=tag + "_b.png", alvo=p)

    def pinta(self, cor, espera, alvo="Part", tag="s_cor"):
        J = self.J
        E.limpa_popups(J); E.seleciona(J, alvo)
        self.cap(tag + "_a")
        pc = E.pontos_cor(J)
        if not E.paleta_aberta(J):
            rs.confere(); rs.clique_img(pc["seta"][0], pc["seta"][1], escala=2.0, janela=J)
            time.sleep(2.0)
        assert E.paleta_aberta(J), "a paleta de cores nao abriu"
        pal = E.paleta_aberta(J)[0]
        ox, oy = int((pal["x"] - J["x"]) * 2), int((pal["y"] - J["y"]) * 2)
        comp = Image.open(rs.captura(J["id"], "/tmp/_m.png")[0]).convert("RGB")
        rs.captura(pal["id"], "/tmp/_p.png")
        comp.paste(Image.open("/tmp/_p.png").convert("RGB"), (ox, oy))
        comp.save(f"{self.D}/{tag}_b.png")
        rs.confere(); rs.clique_tela(pal["x"] + E.HEX[cor][0] / 2,
                                     pal["y"] + E.HEX[cor][1] / 2); time.sleep(1.5)
        self.cap(tag + "_c")
        rs.confere(); rs.clique_img(pc["aplicar"][0], pc["aplicar"][1], escala=2.0, janela=J)
        time.sleep(2.0)
        self.cap(tag + "_d")
        bc = E.linha_prop(J, "BrickColor")
        assert espera.lower() in bc.lower(), f"BrickColor ficou '{bc}', esperava {espera}"
        rs.tecla(E.ESC); time.sleep(1.0); self.cap(tag + "_e")
        self.reg("cor", antes=tag + "_a.png", paleta=tag + "_b.png", armada=tag + "_c.png",
                 depois=tag + "_d.png", limpo=tag + "_e.png", alvo_seta=list(pc["seta"]),
                 alvo_hex=[ox + E.HEX[cor][0], oy + E.HEX[cor][1]],
                 alvo_aplicar=list(pc["aplicar"]))

    def material(self, nome_mat, alvo="Part", tag="s_mat"):
        J = self.J
        E.limpa_popups(J); E.seleciona(J, alvo)
        self.cap(tag + "_a")
        pm = E.pontos_material(J)
        rs.confere(); rs.clique_img(pm["seta"][0], pm["seta"][1], escala=2.0, janela=J)
        time.sleep(2.2)
        mp = [j for j in rs.janelas() if j.get("nome") == "MaterialPicker"]
        assert mp, "o seletor de materiais nao abriu"
        p = mp[0]; ox, oy = int((p["x"] - J["x"]) * 2), int((p["y"] - J["y"]) * 2)

        def comp2(saida):
            b = Image.open(rs.captura(J["id"], "/tmp/_m2.png")[0]).convert("RGB")
            rs.captura(p["id"], "/tmp/_p2.png")
            b.paste(Image.open("/tmp/_p2.png").convert("RGB"), (ox, oy)); b.save(f"{self.D}/{saida}")

        rs.confere(); rs.clique_tela(p["x"] + 528 / 2, p["y"] + 40 / 2); time.sleep(1.0)
        comp2(tag + "_b.png")
        for _ in range(3):
            rs.confere(); rs.clique_tela(p["x"] + 280 / 2, p["y"] + 40 / 2); time.sleep(1.0)
            rs.captura(p["id"], "/tmp/_bf.png")
            q = np.asarray(Image.open("/tmp/_bf.png").convert("RGB"), dtype=int)[14:70, 10:550]
            if ((q[:, :, 2] > 150) & (q[:, :, 2] - q[:, :, 0] > 50)).sum() > 300:
                break
        rs.digita_teclas(nome_mat.lower()); time.sleep(1.8)
        comp2(tag + "_c.png")
        rs.confere(); rs.clique_tela(p["x"] + 88 / 2, p["y"] + 228 / 2); time.sleep(2.4)
        self.cap(tag + "_d")
        m = E.linha_prop(J, "Material")
        assert nome_mat.lower() in m.lower(), f"Material ficou '{m}'"
        rs.tecla(E.ESC); time.sleep(1.0); self.cap(tag + "_e")
        self.reg("material", antes=tag + "_a.png", picker=tag + "_b.png", busca=tag + "_c.png",
                 depois=tag + "_d.png", limpo=tag + "_e.png", alvo_seta=list(pm["seta"]),
                 alvo_busca=[ox + 280, oy + 40], alvo_neon=[ox + 88, oy + 228])

    def renomeia(self, de, para, tag="s_nome"):
        E.limpa_popups(self.J)
        l = E.acha_linha(self.J, de)
        self.cap(tag + "_a")
        E.renomeia(self.J, de, para)
        self.cap(tag + "_b")
        self.reg("renomear", antes=tag + "_a.png", depois=tag + "_b.png", alvo=[l[0], l[1]])

    def insere_script(self, dono, tag="s_script"):
        J = self.J
        E.limpa_popups(J); E.aba(J, "Modelo")
        l = E.seleciona(J, dono)
        self.cap(tag + "_a")
        # o '+' fica logo depois do nome, mas o OCR as vezes o engole: varrer
        mm = None; usado = None
        for dx in (30, -15, 60, 5):
            ids = {j["id"] for j in rs.janelas()}
            rs.confere(); rs.clique_img(l[2] + dx, l[1], escala=2.0, janela=J); time.sleep(2.2)
            achados = [j for j in rs.janelas()
                       if j["id"] not in ids and j["w"] > 150 and j["h"] > 150]
            if achados:
                mm = achados[0]; usado = l[2] + dx; break
            rs.tecla(E.ESC); time.sleep(0.5)
        assert mm, "o menu do + nao abriu"
        mo_x, mo_y = int((mm["x"] - J["x"]) * 2), int((mm["y"] - J["y"]) * 2)
        comp = Image.open(rs.captura(J["id"], "/tmp/_mm.png")[0]).convert("RGB")
        rs.captura(mm["id"], "/tmp/_mp.png")
        comp.paste(Image.open("/tmp/_mp.png").convert("RGB"), (mo_x, mo_y))
        comp.save(f"{self.D}/{tag}_b.png")
        alvo = E.item_do_menu(mm, "Script")
        assert alvo, "nao achei Script no menu do +"
        rs.confere(); rs.clique_tela(*alvo); time.sleep(3.0)
        self.cap(tag + "_c")
        assert E.linha_prop(J, "Parent").strip().lower() == dono.lower(), \
            f"o Script nao entrou em {dono}"
        self.reg("inserir_script", antes=tag + "_a.png", menu=tag + "_b.png", depois=tag + "_c.png",
                 alvo_mais=[l[2] + 30, l[1]],
                 alvo_item=[int((alvo[0] - mm["x"]) * 2) + mo_x, int((alvo[1] - mm["y"]) * 2) + mo_y])

    def codigo(self, l1, completo, tem):
        E.abre_editor(self.J)
        self.cap("p_editor_nasce")
        rs.escreve_codigo(self.J, l1, tem=(l1.split()[1],), nao_tem=("Hello",))
        self.cap("p_linha1")
        rs.escreve_codigo(self.J, completo, tem=tem)
        self.cap("p_codigo_pronto")
        self.reg("codigo", nasce="p_editor_nasce.png", linha1="p_linha1.png",
                 pronto="p_codigo_pronto.png")

    def volta(self, tag="s_volta"):
        a = self.cap(tag + "_a")
        E.volta_ao_mundo(self.J)
        self.cap(tag + "_b")
        self.reg("voltar", antes=tag + "_a.png", depois=tag + "_b.png", alvo=[70, 213])

    def joga(self, foco="Part", atras=9, tag="s_jogar", andar=2):
        E.enquadra(self.J, foco, atras=atras)
        a = self.cap(tag + "_a")
        E.joga(self.J, espera=10.0); time.sleep(1.5)
        self.cap(tag + "_b"); time.sleep(2.0); self.cap(tag + "_c")
        self.reg("jogar", antes=tag + "_a.png", depois=tag + "_b.png",
                 quadros=[tag + "_b.png", tag + "_c.png"], alvo=[225, 28])
        if andar:
            rs.confere(); rs.clique_img(1200, 900, escala=2.0, janela=self.J); time.sleep(0.8)
            for _ in range(andar):
                rs.segura_tecla(13, 1.2); time.sleep(0.5)
            self.cap("p_no_jogo")

    def para(self, tag="s_parar"):
        a = self.cap(tag + "_a")
        E.para(self.J)
        self.cap(tag + "_b")
        self.reg("parar", antes=tag + "_a.png", depois=tag + "_b.png", alvo=[377, 28])

    def tamanho(self, alvo, valor, tag="s_tam"):
        """Passo que ensina a caixa de filtro das Propriedades."""
        E.limpa_popups(self.J)
        E.escreve_no_filtro(self.J, "size")
        E.seleciona(self.J, alvo)
        self.cap(tag + "_a")
        E.escreve_no_filtro(self.J, "")
        E.poe_prop(self.J, alvo, "Size", valor)
        E.enquadra(self.J, alvo, atras=9)
        self.cap(tag + "_b")
        self.reg("tamanho", antes=tag + "_a.png", depois=tag + "_b.png", valor=valor)

    def fecha_saida_se_aberta(self):
        J = self.J
        a, _ = rs.captura(J["id"], "/tmp/_ts.png")
        aberta = any(t.strip().lower().startswith("sa") and len(t.strip()) <= 6
                     for t, *_ in rs.ocr(a, regiao=(0, 0.55, 1, 0.72), psm="6", escala=2))
        if not aberta:
            return False
        E.aba(J, "Script")
        b, _ = rs.captura(J["id"], "/tmp/_sc.png")
        for t, x, y, w, h in rs.ocr("/tmp/_sc.png", regiao=(0, 0.055, 1, 0.115), psm="11"):
            if t.strip().lower().startswith("sa") and len(t.strip()) <= 6:
                rs.confere(); rs.clique_img(x + w // 2, 118, escala=2.0, janela=J); time.sleep(1.8)
                break
        E.aba(J, "Modelo")
        return True

    def insere_script_em(self, dono, tag, regiao_exp=(0.855, 0.13, 1, 0.75)):
        return E.tentar(lambda: self._insere_script_em(dono, tag), n=4,
                        o_que=f"inserir Script em {dono}")

    def _insere_script_em(self, dono, tag):
        """Igual ao insere_script, mas para um servico do Explorador
        (ServerScriptService, por exemplo), que fica mais abaixo na lista."""
        J = self.J
        E.limpa_popups(J); E.aba(J, "Modelo")
        l = E.acha_linha(J, dono)
        if not l:
            raise RuntimeError(f"nao achei '{dono}' no Explorador")
        rs.confere(); rs.clique_img(l[0], l[1], escala=2.0, janela=J); time.sleep(1.0)
        self.cap(tag + "_a")
        # o '+' fica logo depois do nome, mas o OCR as vezes o engole: varrer
        mm = None; usado = None
        for dx in (30, -15, 60, 5):
            ids = {j["id"] for j in rs.janelas()}
            rs.confere(); rs.clique_img(l[2] + dx, l[1], escala=2.0, janela=J); time.sleep(2.2)
            achados = [j for j in rs.janelas()
                       if j["id"] not in ids and j["w"] > 150 and j["h"] > 150]
            if achados:
                mm = achados[0]; usado = l[2] + dx; break
            rs.tecla(E.ESC); time.sleep(0.5)
        assert mm, "o menu do + nao abriu"
        mo_x, mo_y = int((mm["x"] - J["x"]) * 2), int((mm["y"] - J["y"]) * 2)
        comp = Image.open(rs.captura(J["id"], "/tmp/_mm.png")[0]).convert("RGB")
        rs.captura(mm["id"], "/tmp/_mp.png")
        comp.paste(Image.open("/tmp/_mp.png").convert("RGB"), (mo_x, mo_y))
        comp.save(f"{self.D}/{tag}_b.png")
        alvo = E.item_do_menu(mm, "Script")
        assert alvo, "nao achei Script no menu do +"
        rs.confere(); rs.clique_tela(*alvo); time.sleep(3.0)
        self.cap(tag + "_c")
        # o painel TRUNCA nomes longos ("ServerScripts..") — comparar por prefixo
        pai = "".join(c for c in E.linha_prop(J, "Parent").lower() if c.isalnum())
        alvo_pai = dono.lower()
        assert pai and (alvo_pai.startswith(pai[:10]) or pai.startswith(alvo_pai[:10])), \
            f"o Script foi para '{pai}', nao para {dono}"
        self.reg("script_" + tag, antes=tag + "_a.png", menu=tag + "_b.png", depois=tag + "_c.png",
                 alvo_mais=[usado, l[1]],
                 alvo_item=[int((alvo[0] - mm["x"]) * 2) + mo_x, int((alvo[1] - mm["y"]) * 2) + mo_y])


def projeto_novo_confiavel():
    """Reiniciar o Studio e escolher Baseplate na tela inicial e o unico
       caminho que sempre funciona: o Arquivo -> Novo falha de vez em quando
       e deixa o projeto anterior aberto, contaminando as capturas."""
    import subprocess
    subprocess.run(["pkill", "-9", "-x", "RobloxStudio"])
    time.sleep(6)
    subprocess.run(["open", "/Applications/RobloxStudio.app"])
    time.sleep(45)
    rs.ativa(); time.sleep(2.0)
    d = [j for j in rs.janelas() if j.get("nome") == "Recuperação automática"]
    if d:
        rs.clique_tela(d[0]["x"] + 681 / 2, d[0]["y"] + 776 / 2); time.sleep(3.0)
    J = rs.principal()
    # ir pela barra lateral -> Modelos. A pagina Inicio muda de altura quando
    # ha experiencias recentes e empurra os modelos para fora da tela.
    a, _ = rs.captura(J["id"], "/tmp/_lat.png")
    for t, x, y, w, h in rs.ocr(a, regiao=(0, 0.05, 0.2, 0.6), psm="6", escala=2):
        if t.strip().lower() == "modelos":
            rs.clique_img(x + w // 2, y + h // 2, escala=2.0, janela=J); time.sleep(4.0); break
    a, _ = rs.captura(J["id"], "/tmp/_home.png")
    alvo = None
    for t, x, y, w, h in rs.ocr(a, regiao=(0.1, 0.1, 1, 1.0), psm="6", escala=2):
        if t.strip().lower() == "baseplate":
            alvo = (x + w // 2, y - 120); break
    if not alvo:
        raise RuntimeError("nao achei o modelo Baseplate na tela inicial")
    rs.clique_img(alvo[0], alvo[1], escala=2.0, janela=J); time.sleep(22.0)
    J2 = E.liga()
    E.expande_workspace(J2)
    linhas = [t.lower() for t, *_ in E.explorador(J2)]
    if not any("baseplate" in t for t in linhas):
        raise RuntimeError("o projeto novo nao abriu direito")
    return J2
