#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aula 2 — A lava que mata. Passada linear no Studio, em PROJETO NOVO,
   gravando par antes/depois e o alvo medido de cada gesto."""
import time, json, os, rs, monta, estudio as E
from PIL import Image

D = "aula2"
os.makedirs(D, exist_ok=True)
ALVOS = f"{D}/alvos.json"
A = {}

CODIGO = '''local lava = script.Parent

lava.Touched:Connect(function(parte)
\tlocal humano = parte.Parent:FindFirstChild("Humanoid")
\tif humano then
\t\thumano.Health = 0
\tend
end)'''


def reg(nome, **kw):
    if os.path.exists(ALVOS):
        A.update(json.load(open(ALVOS)))
    A[nome] = {k: (list(v) if isinstance(v, tuple) else v) for k, v in kw.items()}
    json.dump(A, open(ALVOS, "w"), indent=1, ensure_ascii=False)
    print(f"  ok {nome}")


def cap(n):
    a, _ = rs.captura(monta.JAN["id"], f"{D}/{n}.png")
    return f"{D}/{n}.png"


def limpa_cena(J):
    """Projeto novo: so Baseplate e SpawnLocation."""
    for _ in range(12):
        sobra = [(t, x + w // 2, y + h // 2) for t, x, y, w, h in E.explorador(J)
                 if t in ("Part", "Lava", "Script", "Checkpoint", "MARCADOR")]
        if not sobra:
            return True
        rs.confere(); rs.clique_img(sobra[0][1], sobra[0][2], escala=2.0, janela=J); time.sleep(0.8)
        rs.confere(); rs.tecla(E.DEL); time.sleep(1.0)
    return False


def passo1_a8(J):
    E.limpa_popups(J)
    E.aba(J, "Modelo")
    cap("p01_aba_modelo")

    # 1 — criar a peça
    a = cap("s02_a"); p = E.botao_faixa(J, "Parte")
    E.nova_peca(J); b = cap("s02_b")
    reg("criar", antes="s02_a.png", depois="s02_b.png", alvo=p)

    # 2 — levar a câmera até ela (F)
    E.enquadra(J, "Part", atras=6)
    cap("p03_enquadrada")

    # 3 — ancorar
    E.seleciona(J, "Part")
    a = cap("s04_a"); p = E.botao_faixa(J, "Âncora")
    E.ancora(J); b = cap("s04_b")
    reg("ancorar", antes="s04_a.png", depois="s04_b.png", alvo=p)

    # 4 — pintar de vermelho
    E.seleciona(J, "Part")
    a = cap("s05_a")
    if not E.paleta_aberta(J):
        rs.confere(); rs.clique_img(1990, 118, escala=2.0, janela=J); time.sleep(2.0)
    pal = E.paleta_aberta(J)[0]
    rs.captura(J["id"], "/tmp/_m.png"); rs.captura(pal["id"], "/tmp/_p.png")
    comp = Image.open("/tmp/_m.png").convert("RGB")
    ox, oy = int((pal["x"] - J["x"]) * 2), int((pal["y"] - J["y"]) * 2)
    comp.paste(Image.open("/tmp/_p.png").convert("RGB"), (ox, oy))
    comp.save(f"{D}/s05_b.png")
    rs.confere(); rs.clique_tela(pal["x"] + E.HEX["vermelho"][0] / 2,
                                 pal["y"] + E.HEX["vermelho"][1] / 2); time.sleep(1.5)
    cap("s05_c")
    rs.confere(); rs.clique_img(1946, 118, escala=2.0, janela=J); time.sleep(2.0)
    cap("s05_d")
    bc = E.linha_prop(J, "BrickColor")
    assert "red" in bc.lower(), f"BrickColor ficou {bc}"
    rs.tecla(E.ESC); time.sleep(1.0); cap("s05_e")
    reg("cor", antes="s05_a.png", paleta="s05_b.png", armada="s05_c.png",
        depois="s05_d.png", limpo="s05_e.png",
        alvo_seta=[1990, 118], alvo_hex=[ox + E.HEX["vermelho"][0], oy + E.HEX["vermelho"][1]],
        alvo_aplicar=[1946, 118])
    return True


def passo9_a14(J):
    # 5 — material Neon
    E.limpa_popups(J); E.seleciona(J, "Part")
    a = cap("s06_a")
    rs.confere(); rs.clique_img(1885, 118, escala=2.0, janela=J); time.sleep(2.2)
    mp = [j for j in rs.janelas() if j.get("nome") == "MaterialPicker"]
    assert mp, "o seletor de materiais nao abriu"
    p = mp[0]
    ox, oy = int((p["x"] - J["x"]) * 2), int((p["y"] - J["y"]) * 2)

    def compoe(saida):
        rs.captura(J["id"], "/tmp/_m.png"); rs.captura(p["id"], "/tmp/_p.png")
        b = Image.open("/tmp/_m.png").convert("RGB")
        b.paste(Image.open("/tmp/_p.png").convert("RGB"), (ox, oy))
        b.save(f"{D}/{saida}")

    rs.confere(); rs.clique_tela(p["x"] + 528 / 2, p["y"] + 40 / 2); time.sleep(1.0)
    compoe("s06_b.png")
    for _ in range(3):
        rs.confere(); rs.clique_tela(p["x"] + 280 / 2, p["y"] + 40 / 2); time.sleep(1.0)
        rs.captura(p["id"], "/tmp/_bf.png")
        import numpy as np
        q = np.asarray(Image.open("/tmp/_bf.png").convert("RGB"), dtype=int)[14:70, 10:550]
        if ((q[:, :, 2] > 150) & (q[:, :, 2] - q[:, :, 0] > 50)).sum() > 300:
            break
    rs.digita_teclas("neon"); time.sleep(1.8)
    compoe("s06_c.png")
    rs.confere(); rs.clique_tela(p["x"] + 88 / 2, p["y"] + 228 / 2); time.sleep(2.4)
    cap("s06_d")
    m = E.linha_prop(J, "Material")
    assert "neon" in m.lower(), f"Material ficou {m}"
    rs.tecla(E.ESC); time.sleep(1.0); cap("s06_e")
    reg("material", antes="s06_a.png", picker="s06_b.png", busca="s06_c.png",
        depois="s06_d.png", limpo="s06_e.png", alvo_seta=[1885, 118],
        alvo_busca=[ox + 280, oy + 40], alvo_neon=[ox + 88, oy + 228])

    # 6 — renomear para Lava
    E.limpa_popups(J)
    l = E.acha_linha(J, "Part")
    a = cap("s07_a")
    E.renomeia(J, "Part", "Lava")
    b = cap("s07_b")
    reg("renomear", antes="s07_a.png", depois="s07_b.png", alvo=[l[0], l[1]])

    # 7 — inserir o Script pelo "+"
    E.limpa_popups(J)
    l = E.seleciona(J, "Lava")
    a = cap("s08_a")
    ids = {j["id"] for j in rs.janelas()}
    rs.confere(); rs.clique_img(l[2] + 30, l[1], escala=2.0, janela=J); time.sleep(2.2)
    menu = [j for j in rs.janelas() if j["id"] not in ids and j["w"] > 150 and j["h"] > 150]
    assert menu, "o menu do + nao abriu"
    mm = menu[0]
    mo_x, mo_y = int((mm["x"] - J["x"]) * 2), int((mm["y"] - J["y"]) * 2)
    comp = Image.open(rs.captura(J["id"], "/tmp/_mm.png")[0]).convert("RGB")
    rs.captura(mm["id"], "/tmp/_mp.png")
    comp.paste(Image.open("/tmp/_mp.png").convert("RGB"), (mo_x, mo_y))
    comp.save(f"{D}/s08_b.png")
    alvo_item = E.item_do_menu(mm, "Script")
    assert alvo_item, "nao achei Script no menu do +"
    rs.confere(); rs.clique_tela(*alvo_item); time.sleep(3.0)
    px = int((alvo_item[0] - mm["x"]) * 2); py = int((alvo_item[1] - mm["y"]) * 2)
    cap("s08_c")
    assert E.acha_linha(J, "Script"), "o Script nao apareceu"
    reg("inserir_script", antes="s08_a.png", menu="s08_b.png", depois="s08_c.png",
        alvo_mais=[l[2] + 30, l[1]], alvo_item=[mo_x + px, mo_y + py])

    # 8 — o editor, antes e depois do codigo
    cap("p09_editor_vazio")
    rs.escreve_codigo(J, CODIGO, tem=("Touched", "Humanoid", "Health"))
    cap("p10_editor_pronto")
    reg("codigo", foto_antes="p09_editor_vazio.png", foto_depois="p10_editor_pronto.png")
    return True
