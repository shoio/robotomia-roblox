#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 2 — A LAVA QUE MATA. Projeto novo, passada linear, tudo conferido.
   Sem mexer em divisoria de painel e sem Size/Position: o aluno estica e
   arrasta com as ferramentas que ja aprendeu na Aula 1."""
import time, json, os, rs, monta, estudio as E
from PIL import Image

D = "aula2"; os.makedirs(D, exist_ok=True)
ALVOS = f"{D}/alvos.json"

L1 = "local lava = script.Parent"
CODIGO = '''local lava = script.Parent

lava.Touched:Connect(function(parte)
\tlocal humano = parte.Parent:FindFirstChild("Humanoid")
\tif humano then
\t\thumano.Health = 0
\tend
end)'''


def reg(nome, **kw):
    A = json.load(open(ALVOS)) if os.path.exists(ALVOS) else {}
    A[nome] = {k: (list(v) if isinstance(v, tuple) else v) for k, v in kw.items()}
    json.dump(A, open(ALVOS, "w"), indent=1, ensure_ascii=False)
    print(f"  ok {nome}")


def cap(n):
    rs.captura(monta.JAN["id"], f"{D}/{n}.png")
    return f"{n}.png"


def tudo(J):
    # 1 — explorador aberto
    E.limpa_popups(J)
    cap("p01_projeto_novo")
    E.expande_workspace(J)
    cap("p02_workspace_aberto")

    # 2 — aba Modelo
    a = cap("s03_a")
    E.aba(J, "Modelo")
    cap("s03_b")
    reg("aba_modelo", antes="s03_a.png", depois="s03_b.png", alvo=[1639, 36])

    # 3 — criar a peca
    a = cap("s04_a"); p = E.botao_faixa(J, "Parte")
    E.nova_peca(J); cap("s04_b")
    reg("criar", antes="s04_a.png", depois="s04_b.png", alvo=p)

    # 4 — camera na peca
    E.enquadra(J, "Part", atras=7)
    cap("p05_camera")

    # 5 — ancorar
    E.seleciona(J, "Part")
    a = cap("s06_a"); p = E.botao_faixa(J, "Âncora")
    E.ancora(J); cap("s06_b")
    reg("ancorar", antes="s06_a.png", depois="s06_b.png", alvo=p)

    # 6 — pintar de vermelho
    E.seleciona(J, "Part")
    cap("s07_a")
    if not E.paleta_aberta(J):
        rs.confere(); rs.clique_img(1990, 118, escala=2.0, janela=J); time.sleep(2.0)
    pal = E.paleta_aberta(J)[0]
    ox, oy = int((pal["x"] - J["x"]) * 2), int((pal["y"] - J["y"]) * 2)
    comp = Image.open(rs.captura(J["id"], "/tmp/_m.png")[0]).convert("RGB")
    rs.captura(pal["id"], "/tmp/_p.png")
    comp.paste(Image.open("/tmp/_p.png").convert("RGB"), (ox, oy)); comp.save(f"{D}/s07_b.png")
    rs.confere(); rs.clique_tela(pal["x"] + E.HEX["vermelho"][0] / 2,
                                 pal["y"] + E.HEX["vermelho"][1] / 2); time.sleep(1.5)
    cap("s07_c")
    rs.confere(); rs.clique_img(1946, 118, escala=2.0, janela=J); time.sleep(2.0)
    cap("s07_d")
    assert "red" in E.linha_prop(J, "BrickColor").lower(), "nao ficou vermelha"
    rs.tecla(E.ESC); time.sleep(1.0); cap("s07_e")
    reg("cor", antes="s07_a.png", paleta="s07_b.png", armada="s07_c.png",
        depois="s07_d.png", limpo="s07_e.png", alvo_seta=[1990, 118],
        alvo_hex=[ox + E.HEX["vermelho"][0], oy + E.HEX["vermelho"][1]], alvo_aplicar=[1946, 118])

    # 7 — material Neon
    E.limpa_popups(J); E.seleciona(J, "Part")
    cap("s08_a")
    rs.confere(); rs.clique_img(1885, 118, escala=2.0, janela=J); time.sleep(2.2)
    mp = [j for j in rs.janelas() if j.get("nome") == "MaterialPicker"]
    assert mp, "o seletor de materiais nao abriu"
    p = mp[0]; ox, oy = int((p["x"] - J["x"]) * 2), int((p["y"] - J["y"]) * 2)

    def comp2(saida):
        b = Image.open(rs.captura(J["id"], "/tmp/_m2.png")[0]).convert("RGB")
        rs.captura(p["id"], "/tmp/_p2.png")
        b.paste(Image.open("/tmp/_p2.png").convert("RGB"), (ox, oy)); b.save(f"{D}/{saida}")

    rs.confere(); rs.clique_tela(p["x"] + 528 / 2, p["y"] + 40 / 2); time.sleep(1.0)
    comp2("s08_b.png")
    import numpy as np
    for _ in range(3):
        rs.confere(); rs.clique_tela(p["x"] + 280 / 2, p["y"] + 40 / 2); time.sleep(1.0)
        rs.captura(p["id"], "/tmp/_bf.png")
        q = np.asarray(Image.open("/tmp/_bf.png").convert("RGB"), dtype=int)[14:70, 10:550]
        if ((q[:, :, 2] > 150) & (q[:, :, 2] - q[:, :, 0] > 50)).sum() > 300:
            break
    rs.digita_teclas("neon"); time.sleep(1.8)
    comp2("s08_c.png")
    rs.confere(); rs.clique_tela(p["x"] + 88 / 2, p["y"] + 228 / 2); time.sleep(2.4)
    cap("s08_d")
    assert "neon" in E.linha_prop(J, "Material").lower(), "nao virou Neon"
    rs.tecla(E.ESC); time.sleep(1.0); cap("s08_e")
    reg("material", antes="s08_a.png", picker="s08_b.png", busca="s08_c.png",
        depois="s08_d.png", limpo="s08_e.png", alvo_seta=[1885, 118],
        alvo_busca=[ox + 280, oy + 40], alvo_neon=[ox + 88, oy + 228])

    # 8 — renomear
    E.limpa_popups(J)
    l = E.acha_linha(J, "Part")
    cap("s09_a")
    E.renomeia(J, "Part", "Lava")
    cap("s09_b")
    reg("renomear", antes="s09_a.png", depois="s09_b.png", alvo=[l[0], l[1]])
    return True


def parte2(J):
    # 9 — inserir o Script pelo "+"
    E.limpa_popups(J); E.aba(J, "Modelo")
    l = E.seleciona(J, "Lava")
    cap("s10_a")
    ids = {j["id"] for j in rs.janelas()}
    rs.confere(); rs.clique_img(l[2] + 30, l[1], escala=2.0, janela=J); time.sleep(2.2)
    menu = [j for j in rs.janelas() if j["id"] not in ids and j["w"] > 150 and j["h"] > 150]
    assert menu, "o menu do + nao abriu"
    mm = menu[0]
    mo_x, mo_y = int((mm["x"] - J["x"]) * 2), int((mm["y"] - J["y"]) * 2)
    comp = Image.open(rs.captura(J["id"], "/tmp/_mm.png")[0]).convert("RGB")
    rs.captura(mm["id"], "/tmp/_mp.png")
    comp.paste(Image.open("/tmp/_mp.png").convert("RGB"), (mo_x, mo_y)); comp.save(f"{D}/s10_b.png")
    alvo = E.item_do_menu(mm, "Script")
    assert alvo, "nao achei Script no menu do +"
    rs.confere(); rs.clique_tela(*alvo); time.sleep(3.0)
    cap("s10_c")
    assert E.linha_prop(J, "Parent").strip().lower() == "lava", "o Script nao entrou na Lava"
    reg("inserir_script", antes="s10_a.png", menu="s10_b.png", depois="s10_c.png",
        alvo_mais=[l[2] + 30, l[1]],
        alvo_item=[int((alvo[0] - mm["x"]) * 2) + mo_x, int((alvo[1] - mm["y"]) * 2) + mo_y])

    # 10 — o editor
    E.abre_editor(J)
    cap("p11_editor_nasce")
    rs.escreve_codigo(J, L1, tem=("script.Parent",), nao_tem=("Hello",))
    cap("p12_linha1")
    rs.escreve_codigo(J, CODIGO, tem=("Touched", "Humanoid", "Health"))
    cap("p13_codigo_pronto")
    reg("codigo", nasce="p11_editor_nasce.png", linha1="p12_linha1.png",
        pronto="p13_codigo_pronto.png")

    # 11 — voltar ao mundo
    a = cap("s14_a")
    E.volta_ao_mundo(J)
    cap("s14_b")
    reg("voltar", antes="s14_a.png", depois="s14_b.png", alvo=[70, 213])

    # 12 — jogar
    E.enquadra(J, "Lava", atras=9)
    a = cap("s15_a")
    E.joga(J, espera=10.0); time.sleep(1.5)
    cap("s15_b"); time.sleep(2.0); cap("s15_c")
    reg("jogar", antes="s15_a.png", depois="s15_b.png",
        quadros=["s15_b.png", "s15_c.png"], alvo=[225, 28])

    # 13 — andar ate a lava
    rs.confere(); rs.clique_img(1200, 900, escala=2.0, janela=J); time.sleep(0.8)
    for k, seg in [(13, 1.2), (13, 1.2)]:
        rs.segura_tecla(k, seg); time.sleep(0.5)
    cap("p16_no_jogo")

    # 14 — parar
    a = cap("s17_a")
    E.para(J)
    cap("s17_b")
    reg("parar", antes="s17_a.png", depois="s17_b.png", alvo=[377, 28])
    return True
