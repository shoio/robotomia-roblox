#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 2 — A LAVA QUE MATA. Projeto novo, passada linear, tudo conferido."""
import time, json, os, rs, monta, estudio as E
from PIL import Image

D = "aula2"; os.makedirs(D, exist_ok=True)
ALVOS = f"{D}/alvos.json"

CODIGO_L1 = "local lava = script.Parent"
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


def zera(J):
    E.limpa_popups(J)
    E.expande_workspace(J)
    for _ in range(14):
        sobra = [(t, x + w // 2, y + h // 2) for t, x, y, w, h in E.explorador(J)
                 if t.lower() in ("part", "lava", "script", "ponte", "decal", "checkpoint")]
        if not sobra:
            break
        rs.confere(); rs.clique_img(sobra[0][1], sobra[0][2], escala=2.0, janela=J); time.sleep(0.8)
        rs.confere(); rs.tecla(E.DEL); time.sleep(1.0)
    if not E.acha_linha(J, "SpawnLocation"):
        E.insere_em(J, "Workspace", "SpawnLocation")
    return True


def bloco_a(J):
    zera(J)
    E.aba(J, "Modelo")
    cap("p02_projeto_novo")
    cap("p03_aba_modelo")

    a = cap("s04_a"); p = E.botao_faixa(J, "Parte")
    E.nova_peca(J); cap("s04_b")
    reg("criar", antes="s04_a.png", depois="s04_b.png", alvo=p)

    E.enquadra(J, "Part", atras=7)
    cap("p05_camera_na_peca")

    E.seleciona(J, "Part")
    a = cap("s06_a"); p = E.botao_faixa(J, "Âncora")
    E.ancora(J); cap("s06_b")
    reg("ancorar", antes="s06_a.png", depois="s06_b.png", alvo=p)

    E.seleciona(J, "Part")
    E.escreve_no_filtro(J, "size")
    cap("p07_filtro_size")
    E.limpa_filtro(J)
    E.poe_prop_filtrada(J, "Part", "Size", "30,1,30")
    E.enquadra(J, "Part", atras=9)
    cap("p08_lava_grande")
    E.poe_prop_filtrada(J, "Part", "Position", "0,0.5,-25")
    E.enquadra(J, "Part", atras=10)
    cap("p09_lava_posicionada")
    return True


def bloco_b(J):
    """cor, material, renomear"""
    E.limpa_popups(J); E.aba(J, "Modelo")
    E.enquadra(J, "Part", atras=10)
    cap("p09_lava_posicionada")

    # cor vermelha
    E.seleciona(J, "Part")
    cap("s10_a")
    if not E.paleta_aberta(J):
        rs.confere(); rs.clique_img(1990, 118, escala=2.0, janela=J); time.sleep(2.0)
    pal = E.paleta_aberta(J)[0]
    ox, oy = int((pal["x"] - J["x"]) * 2), int((pal["y"] - J["y"]) * 2)
    comp = Image.open(rs.captura(J["id"], "/tmp/_m.png")[0]).convert("RGB")
    rs.captura(pal["id"], "/tmp/_p.png")
    comp.paste(Image.open("/tmp/_p.png").convert("RGB"), (ox, oy)); comp.save(f"{D}/s10_b.png")
    rs.confere(); rs.clique_tela(pal["x"] + E.HEX["vermelho"][0] / 2,
                                 pal["y"] + E.HEX["vermelho"][1] / 2); time.sleep(1.5)
    cap("s10_c")
    rs.confere(); rs.clique_img(1946, 118, escala=2.0, janela=J); time.sleep(2.0)
    cap("s10_d")
    assert "red" in E.linha_prop(J, "BrickColor").lower(), "nao ficou vermelha"
    rs.tecla(E.ESC); time.sleep(1.0); cap("s10_e")
    reg("cor", antes="s10_a.png", paleta="s10_b.png", armada="s10_c.png",
        depois="s10_d.png", limpo="s10_e.png", alvo_seta=[1990, 118],
        alvo_hex=[ox + E.HEX["vermelho"][0], oy + E.HEX["vermelho"][1]], alvo_aplicar=[1946, 118])

    # material Neon
    E.limpa_popups(J); E.seleciona(J, "Part")
    cap("s11_a")
    rs.confere(); rs.clique_img(1885, 118, escala=2.0, janela=J); time.sleep(2.2)
    mp = [j for j in rs.janelas() if j.get("nome") == "MaterialPicker"]
    assert mp, "o seletor de materiais nao abriu"
    p = mp[0]; ox, oy = int((p["x"] - J["x"]) * 2), int((p["y"] - J["y"]) * 2)

    def comp2(saida):
        b = Image.open(rs.captura(J["id"], "/tmp/_m2.png")[0]).convert("RGB")
        rs.captura(p["id"], "/tmp/_p2.png")
        b.paste(Image.open("/tmp/_p2.png").convert("RGB"), (ox, oy)); b.save(f"{D}/{saida}")

    rs.confere(); rs.clique_tela(p["x"] + 528 / 2, p["y"] + 40 / 2); time.sleep(1.0)
    comp2("s11_b.png")
    import numpy as np
    for _ in range(3):
        rs.confere(); rs.clique_tela(p["x"] + 280 / 2, p["y"] + 40 / 2); time.sleep(1.0)
        rs.captura(p["id"], "/tmp/_bf.png")
        q = np.asarray(Image.open("/tmp/_bf.png").convert("RGB"), dtype=int)[14:70, 10:550]
        if ((q[:, :, 2] > 150) & (q[:, :, 2] - q[:, :, 0] > 50)).sum() > 300:
            break
    rs.digita_teclas("neon"); time.sleep(1.8)
    comp2("s11_c.png")
    rs.confere(); rs.clique_tela(p["x"] + 88 / 2, p["y"] + 228 / 2); time.sleep(2.4)
    cap("s11_d")
    assert "neon" in E.linha_prop(J, "Material").lower(), "nao virou Neon"
    rs.tecla(E.ESC); time.sleep(1.0); cap("s11_e")
    reg("material", antes="s11_a.png", picker="s11_b.png", busca="s11_c.png",
        depois="s11_d.png", limpo="s11_e.png", alvo_seta=[1885, 118],
        alvo_busca=[ox + 280, oy + 40], alvo_neon=[ox + 88, oy + 228])

    # renomear
    E.limpa_popups(J)
    l = E.acha_linha(J, "Part")
    cap("s12_a")
    E.renomeia(J, "Part", "Lava")
    cap("s12_b")
    reg("renomear", antes="s12_a.png", depois="s12_b.png", alvo=[l[0], l[1]])
    return True


def bloco_c(J):
    """inserir o Script e escrever o codigo"""
    E.limpa_popups(J); E.aba(J, "Modelo")
    l = E.seleciona(J, "Lava")
    cap("s13_a")
    ids = {j["id"] for j in rs.janelas()}
    rs.confere(); rs.clique_img(l[2] + 30, l[1], escala=2.0, janela=J); time.sleep(2.2)
    menu = [j for j in rs.janelas() if j["id"] not in ids and j["w"] > 150 and j["h"] > 150]
    assert menu, "o menu do + nao abriu"
    mm = menu[0]
    mo_x, mo_y = int((mm["x"] - J["x"]) * 2), int((mm["y"] - J["y"]) * 2)
    comp = Image.open(rs.captura(J["id"], "/tmp/_mm.png")[0]).convert("RGB")
    rs.captura(mm["id"], "/tmp/_mp.png")
    comp.paste(Image.open("/tmp/_mp.png").convert("RGB"), (mo_x, mo_y)); comp.save(f"{D}/s13_b.png")
    alvo = E.item_do_menu(mm, "Script")
    assert alvo, "nao achei Script no menu"
    rs.confere(); rs.clique_tela(*alvo); time.sleep(3.0)
    cap("s13_c")
    assert E.linha_prop(J, "Parent").strip().lower() == "lava", "o Script nao entrou na Lava"
    reg("inserir_script", antes="s13_a.png", menu="s13_b.png", depois="s13_c.png",
        alvo_mais=[l[2] + 30, l[1]],
        alvo_item=[int((alvo[0] - mm["x"]) * 2) + mo_x, int((alvo[1] - mm["y"]) * 2) + mo_y])

    E.abre_editor(J)
    cap("p14_editor_como_nasce")
    rs.escreve_codigo(J, CODIGO_L1, tem=("script.Parent",), nao_tem=("Hello",))
    cap("p15_linha1")
    rs.escreve_codigo(J, CODIGO, tem=("Touched", "Humanoid", "Health"))
    cap("p16_codigo_pronto")
    reg("codigo", nasce="p14_editor_como_nasce.png", linha1="p15_linha1.png",
        pronto="p16_codigo_pronto.png")
    return True


def bloco_d(J):
    """jogar, morrer, parar"""
    E.volta_ao_mundo(J)
    E.enquadra(J, "Lava", atras=11)
    a = cap("s17_a")
    E.joga(J, espera=10.0); time.sleep(2.0)
    cap("s17_b"); time.sleep(2.0); cap("s17_c"); time.sleep(2.0); cap("s17_d")
    reg("jogar", antes="s17_a.png", depois="s17_b.png",
        quadros=["s17_b.png", "s17_c.png", "s17_d.png"], alvo=[225, 28])
    a = cap("s18_a")
    E.para(J)
    cap("s18_b")
    reg("parar", antes="s18_a.png", depois="s18_b.png", alvo=[377, 28])
    return True


def bloco_e(J):
    """a plataforma segura por cima da lava"""
    E.limpa_popups(J); E.aba(J, "Modelo")
    a = cap("s19_a")
    E.nova_peca(J)
    E.seleciona(J, "Part")
    E.ancora(J)
    E.poe_prop_filtrada(J, "Part", "Size", "8,1,8")
    E.poe_prop_filtrada(J, "Part", "Position", "0,4,-16")
    E.seleciona(J, "Part")
    # pinta de verde para ler como "segura"
    if not E.paleta_aberta(J):
        rs.confere(); rs.clique_img(1990, 118, escala=2.0, janela=J); time.sleep(2.0)
    pal = E.paleta_aberta(J)[0]
    rs.confere(); rs.clique_tela(pal["x"] + E.HEX["verde"][0] / 2,
                                 pal["y"] + E.HEX["verde"][1] / 2); time.sleep(1.5)
    rs.confere(); rs.clique_img(1946, 118, escala=2.0, janela=J); time.sleep(2.0)
    E.renomeia(J, "Part", "Ponte")
    E.enquadra(J, "Lava", atras=11)
    cap("p19_ponte")
    reg("ponte", foto="p19_ponte.png", antes="s19_a.png")

    a = cap("s20_a")
    E.joga(J, espera=10.0); time.sleep(2.0)
    cap("s20_b"); time.sleep(2.0); cap("s20_c")
    reg("teste_final", antes="s20_a.png", depois="s20_b.png",
        quadros=["s20_b.png", "s20_c.png"], alvo=[225, 28])
    E.para(J)
    cap("p21_final")
    return True
