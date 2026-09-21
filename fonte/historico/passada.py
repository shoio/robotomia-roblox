#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uma passada linear no Studio, na ORDEM DA AULA, gravando par antes/depois
   e o alvo medido de cada gesto. Cada passo confere o proprio resultado."""
import time, json, os, rs, monta, reenc
from PIL import Image
import numpy as np

ESC, Z, DEL = 53, 6, 51
V = (624, 200, 2550, 1700)
ALVOS = {}
Jn = None

def cap(n):  return monta.cap(n)
def px(f, p): return Image.open(f"aula1/{f}").convert("RGB").getpixel(p)

def peca_laranja(arq):
    a = np.asarray(Image.open(f"aula1/{arq}").convert("RGB"), dtype=int)
    mk = (a[:,:,0]>150)&(a[:,:,1]>110)&(a[:,:,1]<210)&(a[:,:,2]<130)
    mk[:250,:]=False; mk[:,:660]=False; mk[:,2450:]=False
    ys,xs = np.where(mk)
    if len(xs) < 300: return None
    return (int(np.median(xs)), int(np.median(ys)), xs.min(), ys.min(), xs.max(), ys.max())

def _limpa(v):
    if isinstance(v, (list, tuple)): return [_limpa(u) for u in v]
    return int(v) if hasattr(v, "item") else v


def reg(nome, **kw):
    kw = {k: _limpa(v) for k, v in kw.items()}
    if os.path.exists("aula1/alvos_gif.json"):        # nao apagar o que ja foi medido
        ALVOS.update(json.load(open("aula1/alvos_gif.json")))
    ALVOS[nome] = kw
    json.dump(ALVOS, open("aula1/alvos_gif.json","w"), indent=1, ensure_ascii=False)
    print(f"  ok {nome}: " + ", ".join(f"{k}={v}" for k,v in kw.items() if k!="nota"))

def clica(px_, py_, espera=1.6):
    rs.confere(); rs.clique_img(px_, py_, escala=2.0, janela=Jn); time.sleep(espera)

def popup(tam=None, nome=None, antes=None):
    for j in rs.janelas():
        if nome and j.get("nome") == nome: return j
        if tam and (j["w"], j["h"]) == tam: return j
        if antes is not None and j["id"] not in antes and j["w"] > 250 and j["h"] > 250: return j
    return None

def compoe(p, saida):
    rs.captura(Jn["id"], "/tmp/_m.png"); rs.captura(p["id"], "/tmp/_p.png")
    b = Image.open("/tmp/_m.png").convert("RGB")
    ox, oy = int((p["x"]-Jn["x"])*2), int((p["y"]-Jn["y"])*2)
    b.paste(Image.open("/tmp/_p.png").convert("RGB"), (ox, oy))
    b.save(f"aula1/{saida}")
    return ox, oy


def roda():
    global Jn
    reenc.prep(); Jn = monta.JAN
    rs.tecla(ESC); time.sleep(0.6)

    # 1 — CRIAR A PECA
    a = cap("p01_a"); pb = monta.acha_botao("Parte")
    clica(pb[0], pb[1], 2.2)
    b = cap("p01_b")
    m = monta.mudou(f"aula1/{a.split('/')[-1]}", f"aula1/{b.split('/')[-1]}", regiao=V, passo=3)
    assert m, "a peca nao apareceu"
    reg("criar_peca", antes="p01_a.png", depois="p01_b.png", alvo=list(pb))
    P = (m[0], m[1]); print("   peca criada em", P, "caixa", m[2:])

    # 2 — ANCORAR
    c = cap("p02_a"); pa = monta.acha_botao("Âncora")
    clica(pa[0], pa[1], 1.8)
    d = cap("p02_b")
    from PIL import ImageChops
    bb = ImageChops.difference(Image.open("aula1/p02_a.png").convert("RGB").crop((2280,60,2450,180)),
                               Image.open("aula1/p02_b.png").convert("RGB").crop((2280,60,2450,180))).getbbox()
    assert bb, "o botao Ancora nao acendeu"
    reg("ancorar", antes="p02_a.png", depois="p02_b.png", alvo=list(pa))

    # 3 — FERRAMENTA MOVER
    e = cap("p03_a"); pm = monta.acha_botao("Mover")
    clica(pm[0], pm[1], 1.6)
    f = cap("p03_b")
    m3 = monta.mudou("aula1/p03_a.png", "aula1/p03_b.png", regiao=V, passo=3)
    assert m3, "as setas de mover nao apareceram"
    reg("ferramenta_mover", antes="p03_a.png", depois="p03_b.png", alvo=list(pm), mudou=m3)
    return P, m3


def roda2(P, giz):
    """4 arrastar, 5 duplicar, 6 afastar a copia."""
    global Jn
    reenc.prep(); Jn = monta.JAN
    gx0, gy0, gx1, gy1 = giz[2], giz[3], giz[4], giz[5]
    seta_y = ((gx0+gx1)//2, gy0 + 60)            # haste verde, acima da peca

    # 4 — ARRASTAR PARA CIMA
    a = cap("p04_a")
    ATE = (seta_y[0], seta_y[1] - 260)
    rs.confere(); rs.arrasta_img(seta_y[0], seta_y[1], ATE[0], ATE[1], escala=2.0, janela=Jn)
    time.sleep(1.8)
    b = cap("p04_b")
    m = monta.mudou("aula1/p04_a.png", "aula1/p04_b.png", regiao=V, passo=3)
    assert m, "a peca nao subiu"
    reg("arrastar", antes="p04_a.png", depois="p04_b.png", de=list(seta_y), ate=list(ATE), mudou=m)

    # onde a peca esta agora (centro do gizmo novo)
    PN = (m[0], (m[3]+m[5])//2)
    # 5 — DUPLICAR pelo botao direito
    c = cap("p05_a")
    antes_ids = {j["id"] for j in rs.janelas()}
    alvo_dir = (m[0], m[3] + 190)
    rs.confere(); rs.clique_direito_img(alvo_dir[0], alvo_dir[1], janela=Jn); time.sleep(2.2)
    menu = popup(antes=antes_ids)
    assert menu, "o menu do botao direito nao abriu"
    ox, oy = compoe(menu, "p05_b.png")
    rs.captura(menu["id"], "/tmp/_menu.png")
    dup = None
    for t,x,y,w,h in rs.ocr("/tmp/_menu.png", psm="6", escala=2):
        if t.strip().lower().startswith("duplicar"):
            dup = (x+w//2, y+h//2); break
    assert dup, "nao achei Duplicar no menu"
    print("   Duplicar no menu em", dup)
    rs.confere(); rs.clique_tela(menu["x"]+dup[0]/2, menu["y"]+dup[1]/2); time.sleep(2.2)
    d = cap("p05_c")
    reg("duplicar", antes="p05_a.png", menu="p05_b.png", depois="p05_c.png",
        alvo_direito=list(alvo_dir), alvo_menu=[ox+dup[0], oy+dup[1]])
    return alvo_dir, m


def setas(arq):
    """Mede as tres setas do gizmo pela cor. Devolve dict com as pontas."""
    a = np.asarray(Image.open(f"aula1/{arq}").convert("RGB"), dtype=int)
    a[:250,:] = 0; a[:,:660] = 0; a[:,2450:] = 0
    r = {}
    for nome, cond in [
        ("verde",    (a[:,:,1]>150)&(a[:,:,0]<130)&(a[:,:,2]<130)),
        ("vermelha", (a[:,:,0]>170)&(a[:,:,1]<110)&(a[:,:,2]<110)),
        ("azul",     (a[:,:,2]>170)&(a[:,:,0]<120)&(a[:,:,1]<160))]:
        ys, xs = np.where(cond)
        if len(xs) < 200: continue
        r[nome] = (int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max()),
                   int(np.median(xs)), int(np.median(ys)))
    return r


def roda3():
    """6 afastar a copia."""
    global Jn
    reenc.prep(); Jn = monta.JAN
    s = setas("p05_c.png"); print("   setas:", s)
    assert "vermelha" in s, "nao achei a seta vermelha"
    vx0, vy0, vx1, vy1, _, vym = s["vermelha"]
    DE  = (vx1 - 70, vym)                 # na haste vermelha, perto da ponta
    ATE = (DE[0] + 300, vym + 70)
    a = cap("p06_a")
    rs.confere(); rs.arrasta_img(DE[0], DE[1], ATE[0], ATE[1], escala=2.0, janela=Jn)
    time.sleep(1.8)
    b = cap("p06_b")
    m = monta.mudou("aula1/p06_a.png", "aula1/p06_b.png", regiao=V, passo=3)
    assert m, "a copia nao andou"
    reg("afastar_copia", antes="p06_a.png", depois="p06_b.png", de=list(DE), ate=list(ATE), mudou=m)
    return m


def roda_cor(PECA):
    """7 — cor. Antes, ARMA branco para o gesto comecar limpo:
       clicar na setinha do Cor ja aplica a cor armada, entao ela tem de
       ser igual a cor atual da peca, senao a peca muda antes da hora."""
    global Jn
    reenc.prep(); Jn = monta.JAN
    pops = lambda: [j for j in rs.janelas() if j["w"] == 368 and j["h"] == 400]
    # pre-arma branco e aplica
    clica(1990, 118, 2.0); p = pops()[0]
    rs.confere(); rs.clique_tela(p["x"]+672/2, p["y"]+679/2); time.sleep(1.4)
    clica(1946, 118, 2.0)
    base = px("p07_sel.png", PECA)
    a = cap("p07_a"); print("   peca antes:", px("p07_a.png", PECA))

    clica(1990, 118, 2.0); p = pops()[0]
    ox, oy = compoe(p, "p07_b.png")
    print("   com a paleta aberta:", px("p07_b.png", PECA))
    rs.confere(); rs.clique_tela(p["x"]+646/2, p["y"]+332/2); time.sleep(1.6)   # hexagono vermelho
    cap("p07_c"); print("   cor armada:", px("p07_c.png", PECA))
    clica(1946, 118, 2.2)
    cap("p07_d")
    # o realce azul da selecao mascara a cor: mede o DESLOCAMENTO, nao o valor
    q0 = np.asarray(Image.open("aula1/p07_a.png").convert("RGB"), dtype=int)
    q1 = np.asarray(Image.open("aula1/p07_d.png").convert("RGB"), dtype=int)
    jan = (slice(PECA[1]-90, PECA[1]+90), slice(PECA[0]-160, PECA[0]+160))
    d0 = (q0[jan][:,:,0] - q0[jan][:,:,2]).mean()
    d1 = (q1[jan][:,:,0] - q1[jan][:,:,2]).mean()
    print(f"   vermelho-menos-azul: {d0:.0f} -> {d1:.0f}")
    assert d1 - d0 > 40, "a peca nao puxou para o vermelho"
    reg("cor", antes="p07_a.png", paleta="p07_b.png", armada="p07_c.png", depois="p07_d.png",
        alvo_seta=[1990,118], alvo_hex=[ox+646, oy+332], alvo_aplicar=[1946,118],
        nota="a setinha abre a paleta; o hexagono ARMA; o botao Cor APLICA")


def interruptor(p):
    """Le e liga o 'Clique no objeto para aplicar a cor' do rodape da paleta."""
    rs.captura(p["id"], "/tmp/_tg.png")
    a = np.asarray(Image.open("/tmp/_tg.png").convert("RGB"), dtype=int)[730:780, 630:710]
    verde = ((a[:,:,1]>120)&(a[:,:,1]-a[:,:,0]>40)&(a[:,:,1]-a[:,:,2]>40)).sum()
    if verde > 200:
        return True
    rs.confere(); rs.clique_lento(p["x"]+665/2, p["y"]+755/2); time.sleep(1.2)
    rs.captura(p["id"], "/tmp/_tg2.png")
    a = np.asarray(Image.open("/tmp/_tg2.png").convert("RGB"), dtype=int)[730:780, 630:710]
    verde = ((a[:,:,1]>120)&(a[:,:,1]-a[:,:,0]>40)&(a[:,:,1]-a[:,:,2]>40)).sum()
    print("   interruptor ligado:", verde > 200)
    return verde > 200


def vermelhidao(arq, C, r=(160, 90)):
    a = np.asarray(Image.open(f"aula1/{arq}").convert("RGB"), dtype=int)
    j = a[C[1]-r[1]:C[1]+r[1], C[0]-r[0]:C[0]+r[0]]
    return float((j[:,:,0] - j[:,:,2]).mean())


def cor_v2(PECA, hexa=(646, 332)):
    """7 — cor, pelo fluxo real: setinha abre a paleta, o hexagono escolhe,
       e o clique NA PECA pinta (com 'clique no objeto' ligado)."""
    global Jn
    reenc.prep(); Jn = monta.JAN
    pops = lambda: [j for j in rs.janelas() if j["w"] == 368 and j["h"] == 400]
    if not pops(): clica(1990, 118, 2.0)
    p = pops()[0]
    assert interruptor(p), "nao consegui ligar o 'clique no objeto'"
    rs.tecla(ESC); time.sleep(0.8)

    a = cap("p07_a"); v0 = vermelhidao("p07_a.png", PECA)
    clica(1990, 118, 2.0); p = pops()[0]
    ox, oy = compoe(p, "p07_b.png")
    rs.confere(); rs.clique_tela(p["x"]+hexa[0]/2, p["y"]+hexa[1]/2); time.sleep(1.6)
    cap("p07_c")
    rs.confere(); rs.clique_tela(Jn["x"]+PECA[0]/2, Jn["y"]+PECA[1]/2); time.sleep(2.0)
    cap("p07_d"); v1 = vermelhidao("p07_d.png", PECA)
    print(f"   vermelhidao {v0:.0f} -> {v1:.0f}")
    assert v1 - v0 > 40, "a peca nao pintou"
    reg("cor", antes="p07_a.png", paleta="p07_b.png", armada="p07_c.png", depois="p07_d.png",
        alvo_seta=[1990,118], alvo_hex=[ox+hexa[0], oy+hexa[1]], alvo_peca=list(PECA),
        nota="ligar 'Clique no objeto para aplicar a cor'; depois o clique NA PECA pinta")


def brickcolor():
    """Le a linha BrickColor do painel — a unica fonte confiavel:
       o realce da selecao lava a peca na captura."""
    a, _ = rs.captura(Jn["id"], "/tmp/_bc.png")
    itens = [t.strip() for t, *_ in rs.ocr(a, regiao=(0.855, 0.630, 1, 0.655), psm="6", escala=3)]
    return " ".join(i for i in itens if i and i not in ("Mi", "E", "|", "!", "|!", "™"))


def cor_v3(PECA, hexa=(646, 332), espera="red"):
    """7 — cor: setinha abre a paleta -> hexagono -> botao Cor aplica.
       O 'Clique no objeto' tem de estar DESLIGADO, senao o botao so arma."""
    global Jn
    reenc.prep(); Jn = monta.JAN
    pops = lambda: [j for j in rs.janelas() if j["w"] == 368 and j["h"] == 400]
    if not pops(): clica(1990, 118, 2.0)
    p = pops()[0]
    rs.captura(p["id"], "/tmp/_tg.png")
    q = np.asarray(Image.open("/tmp/_tg.png").convert("RGB"), dtype=int)[730:780, 630:710]
    if ((q[:,:,1]>120)&(q[:,:,1]-q[:,:,0]>40)&(q[:,:,1]-q[:,:,2]>40)).sum() > 200:
        rs.confere(); rs.clique_lento(p["x"]+665/2, p["y"]+755/2); time.sleep(1.2)
        print("   desliguei o 'clique no objeto'")
    rs.confere(); rs.clique_tela(p["x"]+560/2, p["y"]+755/2); time.sleep(0.4)   # sai do interruptor
    rs.tecla(ESC); time.sleep(0.9)

    antes_bc = brickcolor(); print("   BrickColor antes:", antes_bc)
    a = cap("p07_a")
    clica(1990, 118, 2.0); p = pops()[0]
    ox, oy = compoe(p, "p07_b.png")
    rs.confere(); rs.clique_tela(p["x"]+hexa[0]/2, p["y"]+hexa[1]/2); time.sleep(1.6)
    cap("p07_c")
    clica(1946, 118, 2.2)
    depois_bc = brickcolor(); print("   BrickColor depois:", depois_bc)
    assert espera.lower() in depois_bc.lower(), f"esperava {espera}, veio '{depois_bc}'"
    cap("p07_d")
    rs.tecla(ESC); time.sleep(1.2)
    cap("p07_e")                                    # sem selecao: a cor aparece
    reg("cor", antes="p07_a.png", paleta="p07_b.png", armada="p07_c.png",
        depois="p07_d.png", limpo="p07_e.png",
        alvo_seta=[1990,118], alvo_hex=[ox+hexa[0], oy+hexa[1]], alvo_aplicar=[1946,118],
        nota="o realce da selecao lava a cor; clicar fora mostra o resultado")


def linha_prop(rotulo):
    """Acha a linha do painel PELO ROTULO e devolve o que esta a direita dele.
       A faixa fixa nao serve: o painel desloca conforme o objeto."""
    a, _ = rs.captura(Jn["id"], "/tmp/_mp.png")
    itens = [(t.strip(), x, y, w, h) for t, x, y, w, h in
             rs.ocr(a, regiao=(0.855, 0.55, 1, 1.0), psm="6", escala=3) if t.strip()]
    alvo = [it for it in itens if it[0].lower() == rotulo.lower()]
    if not alvo:
        return ""
    _, ax, ay, aw, ah = alvo[0]
    dir_ = [t for t, x, y, w, h in itens
            if abs((y + h // 2) - (ay + ah // 2)) < ah and x > ax + aw]
    return " ".join(dir_)


def material_prop():
    return linha_prop("Material")


def resto(PECA):
    """8 material Neon, 9 dimensionar, 10 jogar, 11 parar."""
    global Jn
    reenc.prep(); Jn = monta.JAN
    K = {"n": 45, "e": 14, "o": 31}
    rs.confere(); rs.clique_img(PECA[0], PECA[1], escala=2.0, janela=Jn); time.sleep(1.4)

    # 8 — MATERIAL NEON
    print("   Material antes:", material_prop())
    a = cap("p08_a")
    clica(1885, 118, 2.2)
    mp = [j for j in rs.janelas() if j.get("nome") == "MaterialPicker"]
    assert mp, "o seletor de materiais nao abriu"
    p = mp[0]
    ox, oy = compoe(p, "p08_b.png")
    rs.confere(); rs.clique_tela(p["x"]+280/2, p["y"]+40/2); time.sleep(0.8)
    for ch in "neon": rs.tecla(K[ch]); time.sleep(0.12)
    time.sleep(1.8)
    compoe(p, "p08_c.png")
    rs.confere(); rs.clique_tela(p["x"]+88/2, p["y"]+228/2); time.sleep(2.4)
    mat = material_prop(); print("   Material depois:", mat)
    assert "neon" in mat.lower(), f"nao virou Neon: '{mat}'"
    cap("p08_d"); rs.tecla(ESC); time.sleep(1.0); cap("p08_e")
    reg("material", antes="p08_a.png", picker="p08_b.png", busca="p08_c.png",
        depois="p08_d.png", limpo="p08_e.png", alvo_seta=[1885,118],
        alvo_busca=[ox+280, oy+40], alvo_neon=[ox+88, oy+228])

    # 9 — DIMENSIONAR
    rs.confere(); rs.clique_img(PECA[0], PECA[1], escala=2.0, janela=Jn); time.sleep(1.3)
    c = cap("p09_a"); pd = monta.acha_botao("Dimensionar")
    clica(pd[0], pd[1], 1.8)
    cap("p09_b")
    m = monta.mudou("aula1/p09_a.png", "aula1/p09_b.png", regiao=V, passo=3)
    assert m, "as alcas de dimensionar nao apareceram"
    reg("dimensionar", antes="p09_a.png", depois="p09_b.png", alvo=list(pd), mudou=m)

    # 10 — JOGAR
    e = cap("p10_a")
    clica(225, 28, 7.5)
    f = cap("p10_b"); time.sleep(1.5); cap("p10_c"); time.sleep(1.5); cap("p10_d")
    net = any("NetworkClient" in t for t, *_ in rs.ocr("aula1/p10_b.png",
              regiao=(0.86, 0.13, 1, 0.6), psm="6", escala=2))
    assert net, "nao entrou em modo de teste"
    reg("jogar", antes="p10_a.png", depois="p10_b.png",
        quadros=["p10_b.png", "p10_c.png", "p10_d.png"], alvo=[225, 28])

    # 11 — PARAR
    clica(377, 28, 6.5)
    cap("p11_b")
    reg("parar", antes="p10_d.png", depois="p11_b.png", alvo=[377, 28])


def busca_focada(p):
    """A caixa de busca do seletor ganha borda azul quando tem o foco.
       Sem essa conferencia as letras vazam para a viewport e mexem a camera."""
    rs.captura(p["id"], "/tmp/_bf.png")
    a = np.asarray(Image.open("/tmp/_bf.png").convert("RGB"), dtype=int)[14:70, 10:550]
    azul = ((a[:,:,2] > 150) & (a[:,:,2] - a[:,:,0] > 50)).sum()
    return azul > 300


def resto2(PECA):
    """8 material Neon, 9 dimensionar, 10 jogar, 11 parar — com conferencias."""
    global Jn
    reenc.prep(); Jn = monta.JAN
    K = {"n": 45, "e": 14, "o": 31}
    rs.confere(); rs.clique_img(PECA[0], PECA[1], escala=2.0, janela=Jn); time.sleep(1.4)
    assert "Part" in linha_prop("ClassName") or linha_prop("Material"), "nada selecionado"

    print("   Material antes:", linha_prop("Material"))
    a = cap("p08_a")
    clica(1885, 118, 2.2)
    mp = [j for j in rs.janelas() if j.get("nome") == "MaterialPicker"]
    assert mp, "o seletor de materiais nao abriu"
    p = mp[0]
    ox, oy = compoe(p, "p08_b.png")
    rs.confere(); rs.clique_tela(p["x"]+528/2, p["y"]+40/2); time.sleep(1.0)   # limpa o que sobrou
    ox, oy = compoe(p, "p08_b.png")
    for tent in range(3):
        rs.confere(); rs.clique_tela(p["x"]+280/2, p["y"]+40/2); time.sleep(1.0)
        if busca_focada(p): break
        print("   (a busca nao pegou o foco, tentando de novo)")
    else:
        raise AssertionError("a caixa de busca nunca pegou o foco — nao vou digitar")
    for ch in "neon": rs.tecla(K[ch]); time.sleep(0.12)
    time.sleep(1.8)
    compoe(p, "p08_c.png")
    # tem de sobrar UM material na grade, senao o clique cai no vazio
    g = np.asarray(Image.open("/tmp/_p.png").convert("RGB"), dtype=int)[150:320, 10:180]
    assert (g.mean(2) > 120).sum() > 4000, "a busca nao devolveu o Neon"
    rs.confere(); rs.clique_tela(p["x"]+88/2, p["y"]+228/2); time.sleep(2.4)
    mat = linha_prop("Material"); print("   Material depois:", mat)
    assert "neon" in mat.lower(), f"nao virou Neon: '{mat}'"
    cap("p08_d"); rs.tecla(ESC); time.sleep(1.0); cap("p08_e")
    reg("material", antes="p08_a.png", picker="p08_b.png", busca="p08_c.png",
        depois="p08_d.png", limpo="p08_e.png", alvo_seta=[1885, 118],
        alvo_busca=[ox+280, oy+40], alvo_neon=[ox+88, oy+228])

    rs.confere(); rs.clique_img(PECA[0], PECA[1], escala=2.0, janela=Jn); time.sleep(1.3)
    cap("p09_a"); pd = monta.acha_botao("Dimensionar")
    clica(pd[0], pd[1], 1.8); cap("p09_b")
    m = monta.mudou("aula1/p09_a.png", "aula1/p09_b.png", regiao=V, passo=3)
    assert m, "as alcas nao apareceram"
    reg("dimensionar", antes="p09_a.png", depois="p09_b.png", alvo=list(pd), mudou=m)

    cap("p10_a"); clica(225, 28, 7.5)
    cap("p10_b"); time.sleep(1.5); cap("p10_c"); time.sleep(1.5); cap("p10_d")
    assert any("NetworkClient" in t for t, *_ in rs.ocr("aula1/p10_b.png",
               regiao=(0.86, 0.13, 1, 0.6), psm="6", escala=2)), "nao entrou em teste"
    reg("jogar", antes="p10_a.png", depois="p10_b.png",
        quadros=["p10_b.png", "p10_c.png", "p10_d.png"], alvo=[225, 28])

    clica(377, 28, 6.5); cap("p11_b")
    reg("parar", antes="p10_d.png", depois="p11_b.png", alvo=[377, 28])


TECLA = {"a":0,"b":11,"c":8,"d":2,"e":14,"f":3,"g":5,"h":4,"i":34,"j":38,"k":40,
         "l":37,"m":46,"n":45,"o":31,"p":35,"q":12,"r":15,"s":1,"t":17,"u":32,
         "v":9,"w":13,"x":7,"y":16,"z":6}


def poe_material(nome, PECA):
    """Aplica um material pelo nome, limpando a busca antes (ela guarda o texto)."""
    global Jn
    reenc.prep(); Jn = monta.JAN
    rs.confere(); rs.clique_img(PECA[0], PECA[1], escala=2.0, janela=Jn); time.sleep(1.3)
    clica(1885, 118, 2.2)
    p = [j for j in rs.janelas() if j.get("nome") == "MaterialPicker"][0]
    rs.confere(); rs.clique_tela(p["x"]+528/2, p["y"]+40/2); time.sleep(1.0)
    for _ in range(3):
        rs.confere(); rs.clique_tela(p["x"]+280/2, p["y"]+40/2); time.sleep(1.0)
        if busca_focada(p): break
    for ch in nome.lower(): rs.tecla(TECLA[ch]); time.sleep(0.1)
    time.sleep(1.8)
    rs.confere(); rs.clique_tela(p["x"]+88/2, p["y"]+228/2); time.sleep(2.2)
    m = linha_prop("Material"); print(f"   material agora: {m}")
    assert nome.lower() in m.lower(), f"esperava {nome}, veio {m}"
    rs.tecla(ESC); time.sleep(0.8)


def poe_cor(hexa, PECA, espera):
    """Aplica uma cor da paleta pelo botao Cor (o 'clique no objeto' fica desligado)."""
    global Jn
    reenc.prep(); Jn = monta.JAN
    rs.confere(); rs.clique_img(PECA[0], PECA[1], escala=2.0, janela=Jn); time.sleep(1.3)
    clica(1990, 118, 2.0)
    p = [j for j in rs.janelas() if j["w"] == 368 and j["h"] == 400][0]
    rs.confere(); rs.clique_tela(p["x"]+hexa[0]/2, p["y"]+hexa[1]/2); time.sleep(1.5)
    clica(1946, 118, 2.0)
    bc = linha_prop("BrickColor"); print(f"   BrickColor agora: {bc}")
    assert espera.lower() in bc.lower(), f"esperava {espera}, veio {bc}"
