#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ferramenta para inspecionar e operar o Roblox Studio em laço fechado:
   agir → capturar → ler por OCR → conferir."""
import subprocess, time, os, re, sys
import Quartz
from PIL import Image

SP = "/private/tmp/claude-501/-Users-shoio/6f4de3a6-72e1-4514-805d-e784bd37f029/scratchpad"
APP = "Roblox Studio"


# ───────────────────────────── janelas ─────────────────────────────

def janelas(dono=APP):
    wl = Quartz.CGWindowListCopyWindowInfo(
        Quartz.kCGWindowListOptionAll | Quartz.kCGWindowListExcludeDesktopElements,
        Quartz.kCGNullWindowID)
    out = []
    for w in wl:
        if (w.get("kCGWindowOwnerName") or "") != dono:
            continue
        b = w.get("kCGWindowBounds", {})
        out.append(dict(id=w.get("kCGWindowNumber"),
                        nome=w.get("kCGWindowName") or "",
                        x=int(b.get("X", 0)), y=int(b.get("Y", 0)),
                        w=int(b.get("Width", 0)), h=int(b.get("Height", 0)),
                        camada=w.get("kCGWindowLayer")))
    return out


def principal():
    """A maior janela de conteúdo (camada 0)."""
    cs = [j for j in janelas() if j["camada"] == 0 and j["w"] > 600 and j["h"] > 400]
    if not cs:
        return None
    return max(cs, key=lambda j: j["w"] * j["h"])


def dialogos():
    """Janelas pequenas de camada 0 ou acima — caixas de diálogo."""
    return [j for j in janelas() if 150 < j["w"] <= 1000 and 80 < j["h"] <= 900]


# ───────────────────────────── captura ─────────────────────────────

def captura(wid=None, arquivo=None):
    """Salva PNG da janela (mesmo sem estar na frente). Devolve (caminho, escala)."""
    if wid is None:
        p = principal()
        if p is None:
            raise RuntimeError("nenhuma janela principal do Studio")
        wid, lw = p["id"], p["w"]
    else:
        j = [x for x in janelas() if x["id"] == wid]
        lw = j[0]["w"] if j else None
    img = Quartz.CGWindowListCreateImage(
        Quartz.CGRectNull, Quartz.kCGWindowListOptionIncludingWindow, wid,
        Quartz.kCGWindowImageBoundsIgnoreFraming)
    if img is None:
        raise RuntimeError(f"não consegui capturar a janela {wid}")
    w = Quartz.CGImageGetWidth(img); h = Quartz.CGImageGetHeight(img)
    prov = Quartz.CGImageGetDataProvider(img)
    data = bytes(Quartz.CGDataProviderCopyData(prov))
    bpr = Quartz.CGImageGetBytesPerRow(img)
    im = Image.frombuffer("RGBA", (w, h), data, "raw", "BGRA", bpr, 1).convert("RGB")
    arquivo = arquivo or f"{SP}/rs_cap.png"
    im.save(arquivo)
    escala = (w / lw) if lw else 2.0        # Retina costuma ser 2.0
    return arquivo, escala


# ─────────────────────────────── OCR ───────────────────────────────

def ocr(arquivo=None, regiao=None, psm="11", idioma="por+eng", escala=2):
    """Devolve [(texto, x, y, w, h)] em pixels DA IMAGEM.
       regiao = (x0,y0,x1,y1) em fração 0..1."""
    arquivo = arquivo or f"{SP}/rs_cap.png"
    im = Image.open(arquivo).convert("L")
    W, H = im.size
    ox = oy = 0
    if regiao:
        x0, y0, x1, y1 = regiao
        ox, oy = int(x0 * W), int(y0 * H)
        im = im.crop((ox, oy, int(x1 * W), int(y1 * H)))
    if escala != 1:
        im = im.resize((im.width * escala, im.height * escala), Image.LANCZOS)
    p = f"{SP}/_ocr.png"; im.save(p)
    r = subprocess.run(["tesseract", p, "-", "-l", idioma, "--psm", psm, "tsv"],
                       capture_output=True, text=True)
    itens = []
    for linha in r.stdout.splitlines()[1:]:
        c = linha.split("\t")
        if len(c) < 12:
            continue
        txt = c[11].strip()
        try:
            conf = float(c[10])
        except ValueError:
            continue
        if not txt or conf < 45:
            continue
        x, y, w, h = (int(c[6]), int(c[7]), int(c[8]), int(c[9]))
        itens.append((txt, ox + x // escala, oy + y // escala, w // escala, h // escala))
    return itens


def texto(arquivo=None, regiao=None, psm="11"):
    return " · ".join(t for t, *_ in ocr(arquivo, regiao, psm))


def acha(alvo, arquivo=None, regiao=None, psm="11"):
    """Procura um rótulo. Devolve (x, y) do CENTRO em pixels da imagem, ou None."""
    alvo_n = alvo.lower()
    for t, x, y, w, h in ocr(arquivo, regiao, psm):
        if alvo_n == t.lower() or alvo_n in t.lower():
            return (x + w // 2, y + h // 2)
    return None


# ────────────────────────── mouse e teclado ────────────────────────

def _evento_mouse(tipo, x, y, botao=Quartz.kCGMouseButtonLeft):
    e = Quartz.CGEventCreateMouseEvent(None, tipo, (x, y), botao)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)


def clique_tela(x, y, duplo=False):
    """Clica em coordenadas da TELA (pontos, não pixels)."""
    _evento_mouse(Quartz.kCGEventMouseMoved, x, y)
    time.sleep(0.12)
    _evento_mouse(Quartz.kCGEventLeftMouseDown, x, y)
    time.sleep(0.05)
    _evento_mouse(Quartz.kCGEventLeftMouseUp, x, y)
    if duplo:
        time.sleep(0.08)
        e = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseDown, (x, y), 0)
        Quartz.CGEventSetIntegerValueField(e, Quartz.kCGMouseEventClickState, 2)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)
        e = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseUp, (x, y), 0)
        Quartz.CGEventSetIntegerValueField(e, Quartz.kCGMouseEventClickState, 2)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)
    time.sleep(0.25)


def clique_img(px, py, escala=None, janela=None, duplo=False):
    """Clica usando coordenadas de PIXEL da captura, convertendo para tela."""
    j = janela or principal()
    if escala is None:
        escala = 2.0
    x = j["x"] + px / escala
    y = j["y"] + py / escala
    clique_tela(x, y, duplo)
    return (x, y)


def tecla(codigo, cmd=False, shift=False, alt=False, ctrl=False):
    flags = 0
    if cmd:   flags |= Quartz.kCGEventFlagMaskCommand
    if shift: flags |= Quartz.kCGEventFlagMaskShift
    if alt:   flags |= Quartz.kCGEventFlagMaskAlternate
    if ctrl:  flags |= Quartz.kCGEventFlagMaskControl
    for baixo in (True, False):
        e = Quartz.CGEventCreateKeyboardEvent(None, codigo, baixo)
        Quartz.CGEventSetFlags(e, flags)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)
        time.sleep(0.03)
    time.sleep(0.15)


def digita(txt):
    for ch in txt:
        e = Quartz.CGEventCreateKeyboardEvent(None, 0, True)
        Quartz.CGEventKeyboardSetUnicodeString(e, len(ch), ch)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)
        e = Quartz.CGEventCreateKeyboardEvent(None, 0, False)
        Quartz.CGEventKeyboardSetUnicodeString(e, len(ch), ch)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)
        time.sleep(0.02)
    time.sleep(0.15)


def ativa():
    subprocess.run(["osascript", "-e", f'tell application "{APP}" to activate'],
                   capture_output=True)
    time.sleep(1.2)


def menu(caminho):
    """Aciona um item de menu pelo caminho, ex.: ['File','New']."""
    itens = " of ".join(f'menu item "{p}"' if i == len(caminho) - 1 else f'menu "{p}"'
                        for i, p in enumerate(reversed(caminho)))
    scr = (f'tell application "System Events" to tell process "RobloxStudio" '
           f'to click menu item "{caminho[-1]}" of menu 1 of menu bar item "{caminho[0]}" '
           f'of menu bar 1')
    r = subprocess.run(["osascript", "-e", scr], capture_output=True, text=True)
    time.sleep(1.0)
    return r.returncode == 0, (r.stderr or "").strip()


def menus_disponiveis():
    scr = ('tell application "System Events" to tell process "RobloxStudio" '
           'to get name of every menu bar item of menu bar 1')
    r = subprocess.run(["osascript", "-e", scr], capture_output=True, text=True)
    return [s.strip() for s in r.stdout.split(",")] if r.returncode == 0 else []


def itens_do_menu(nome):
    scr = (f'tell application "System Events" to tell process "RobloxStudio" '
           f'to get name of every menu item of menu 1 of menu bar item "{nome}" of menu bar 1')
    r = subprocess.run(["osascript", "-e", scr], capture_output=True, text=True)
    return [s.strip() for s in r.stdout.split(",")] if r.returncode == 0 else []


def arrasta_tela(x0, y0, x1, y1, passos=28):
    """Arrasta o mouse de (x0,y0) ate (x1,y1) em coordenadas de TELA."""
    _evento_mouse(Quartz.kCGEventMouseMoved, x0, y0); time.sleep(0.15)
    _evento_mouse(Quartz.kCGEventLeftMouseDown, x0, y0); time.sleep(0.15)
    for k in range(1, passos + 1):
        x = x0 + (x1 - x0) * k / passos
        y = y0 + (y1 - y0) * k / passos
        e = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventLeftMouseDragged, (x, y),
                                           Quartz.kCGMouseButtonLeft)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)
        time.sleep(0.02)
    time.sleep(0.15)
    _evento_mouse(Quartz.kCGEventLeftMouseUp, x1, y1)
    time.sleep(0.5)


def arrasta_img(px0, py0, px1, py1, escala=2.0, janela=None):
    j = janela or principal()
    arrasta_tela(j["x"] + px0/escala, j["y"] + py0/escala,
                 j["x"] + px1/escala, j["y"] + py1/escala)


def arrasta_direito(x0, y0, x1, y1, passos=26):
    """Arrasta com o BOTAO DIREITO — no Studio isso gira a camera."""
    D = Quartz.kCGMouseButtonRight
    e = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventMouseMoved, (x0,y0), D)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, e); time.sleep(0.15)
    e = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventRightMouseDown, (x0,y0), D)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, e); time.sleep(0.15)
    for k in range(1, passos+1):
        x = x0 + (x1-x0)*k/passos; y = y0 + (y1-y0)*k/passos
        e = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventRightMouseDragged, (x,y), D)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, e); time.sleep(0.025)
    time.sleep(0.15)
    e = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventRightMouseUp, (x1,y1), D)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, e); time.sleep(0.5)


def roda(x, y, cliques=5):
    """Roda do mouse em (x,y) da TELA. Positivo = aproxima."""
    _evento_mouse(Quartz.kCGEventMouseMoved, x, y); time.sleep(0.2)
    for _ in range(abs(cliques)):
        e = Quartz.CGEventCreateScrollWheelEvent(None, Quartz.kCGScrollEventUnitLine, 1,
                                                 1 if cliques > 0 else -1)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)
        time.sleep(0.09)
    time.sleep(0.6)


def arrasta_direito_img(px0, py0, px1, py1, escala=2.0, janela=None):
    j = janela or principal()
    arrasta_direito(j["x"]+px0/escala, j["y"]+py0/escala,
                    j["x"]+px1/escala, j["y"]+py1/escala)


def roda_img(px, py, cliques=5, escala=2.0, janela=None):
    j = janela or principal()
    roda(j["x"]+px/escala, j["y"]+py/escala, cliques)


class SaiuDoAr(Exception):
    """O Studio deixou de ser a janela da frente — abortar antes de clicar."""


def confere(janela_esperada=None):
    """Guarda de segurança: só deixa agir se o Studio estiver na frente
       e a janela continuar do mesmo tamanho e lugar."""
    r = subprocess.run(["osascript","-e",
        'tell application "System Events" to get name of first process whose frontmost is true'],
        capture_output=True, text=True)
    frente = (r.stdout or "").strip()
    if frente != "RobloxStudio":
        raise SaiuDoAr(f"app na frente e '{frente}', nao o Studio — ABORTADO sem clicar")
    p = principal()
    if p is None:
        raise SaiuDoAr("janela principal do Studio sumiu — ABORTADO")
    if janela_esperada:
        for k in ("x","y","w","h"):
            if p[k] != janela_esperada[k]:
                raise SaiuDoAr(f"a janela mudou de {janela_esperada} para {p} — ABORTADO")
    return p


def seguro(fn, janela_esperada=None):
    """Executa fn() só se a guarda passar."""
    confere(janela_esperada)
    return fn()


def clique_direito_tela(x, y):
    """Clique com o botao direito em (x,y) da TELA — abre menu de contexto."""
    D = Quartz.kCGMouseButtonRight
    e = Quartz.CGEventCreateMouseEvent(None, Quartz.kCGEventMouseMoved, (x, y), D)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, e); time.sleep(0.25)
    for tipo in (Quartz.kCGEventRightMouseDown, Quartz.kCGEventRightMouseUp):
        e = Quartz.CGEventCreateMouseEvent(None, tipo, (x, y), D)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, e); time.sleep(0.12)
    time.sleep(0.5)
    return (x, y)


def clique_direito_img(px, py, escala=2.0, janela=None):
    j = janela or principal()
    return clique_direito_tela(j["x"] + px/escala, j["y"] + py/escala)


def clique_lento(x, y, hover=0.6, segura=0.18):
    """Clique com hover longo — popups Qt (paleta de cor) ignoram clique rapido."""
    _evento_mouse(Quartz.kCGEventMouseMoved, x, y);       time.sleep(hover/2)
    _evento_mouse(Quartz.kCGEventMouseMoved, x+1, y+1);   time.sleep(hover/2)
    _evento_mouse(Quartz.kCGEventMouseMoved, x, y);       time.sleep(0.2)
    _evento_mouse(Quartz.kCGEventLeftMouseDown, x, y);    time.sleep(segura)
    _evento_mouse(Quartz.kCGEventLeftMouseUp, x, y);      time.sleep(0.4)


def area_de_transferencia(texto):
    import subprocess
    subprocess.run(["pbcopy"], input=texto.encode("utf-8"), check=True)
    time.sleep(0.3)


def cola(texto=None):
    """Cola (Cmd+V). ATENCAO: Cmd+A no Studio seleciona OBJETOS, nao texto —
       nao da para usar 'selecionar tudo' para limpar o editor."""
    if texto is not None:
        area_de_transferencia(texto)
    tecla(9, cmd=True)
    time.sleep(0.8)


ESQ, DIR, CIMA, BAIXO = 123, 124, 126, 125


def texto_do_editor(janela, arquivo="/tmp/_ed.png"):
    """Le o codigo que esta na tela do editor.
       Regiao em PIXELS, nao em fracao: a faixa de ferramentas tem altura fixa,
       entao quando a janela encolhe a fracao passa a pegar a faixa em vez do
       codigo — foi assim que eu 'perdi' um codigo que estava certo na tela."""
    from PIL import Image as _I
    a, _ = captura(janela["id"], arquivo)
    im = _I.open(a)
    L, A = im.size
    reg = (100 / L, 235 / A, min(1.0, 1750 / L), min(1.0, 1150 / A))
    itens = ocr(arquivo, regiao=reg, psm="6", escala=2)
    return " ".join(t.strip() for t, *_ in itens if t.strip())


def escreve_codigo(janela, texto, ponto=(700, 300), tem=(), nao_tem=("Hello",), tentativas=4):
    """Troca o conteudo do editor pelo codigo e CONFERE lendo a tela.
       Cmd+A seleciona OBJETOS no Studio; no editor, ir ao topo e selecionar
       ate o fim pega o documento inteiro sem depender de onde o clique caiu."""
    ultimo = ""
    for k in range(tentativas):
        ativa(); time.sleep(0.4)
        clique_img(ponto[0], ponto[1], escala=2.0, janela=janela); time.sleep(0.7)
        tecla(CIMA, cmd=True); time.sleep(0.3)
        tecla(BAIXO, cmd=True, shift=True); time.sleep(0.3)
        cola(texto)
        time.sleep(1.2)
        ultimo = texto_do_editor(janela)
        faltando = [p for p in tem if p.lower() not in ultimo.lower()]
        sobrando = [p for p in nao_tem if p.lower() in ultimo.lower()]
        # o OCR engole uma linha de vez em quando (confunde o triangulo de
        # dobra com letra). Exigir TODOS os marcadores reprovava codigo certo;
        # a maioria deles, somada a ausencia do texto padrao, ja e prova boa.
        bastante = tem and (len(tem) - len(faltando)) >= max(1, int(len(tem) * 0.6))
        if (not faltando or bastante) and not sobrando:
            return ultimo
        print(f"   (editor tentativa {k+1}: faltou {faltando}, sobrou {sobrando})")
        time.sleep(1.0)
    raise RuntimeError(f"nao consegui deixar o codigo certo no editor\nlido: {ultimo[:300]}")


ESQ, DIR, CIMA, BAIXO = 123, 124, 126, 125

TECLAS = {"a":0,"s":1,"d":2,"f":3,"h":4,"g":5,"z":6,"x":7,"c":8,"v":9,"b":11,
          "q":12,"w":13,"e":14,"r":15,"y":16,"t":17,"o":31,"u":32,"i":34,"p":35,
          "l":37,"j":38,"k":40,"n":45,"m":46,
          "1":18,"2":19,"3":20,"4":21,"5":23,"6":22,"7":26,"8":28,"9":25,"0":29,
          " ":49,"-":27,"=":24,".":47,",":43}


def digita_teclas(texto):
    """Digita com codigos de tecla reais — o Studio ignora o caminho Unicode
       em varios campos (a busca de material, por exemplo)."""
    for ch in texto:
        base = ch.lower()
        if base not in TECLAS:
            raise ValueError(f"nao sei digitar {ch!r}")
        tecla(TECLAS[base], shift=ch.isupper())
        time.sleep(0.06)


def saida_contem(janela, alvo, arquivo="/tmp/_saida.png"):
    """Procura um texto no painel Saida."""
    captura(janela["id"], arquivo)
    for t, *_ in ocr(arquivo, regiao=(0, 0.58, 1, 0.97), psm="6", escala=2):
        if alvo.lower() in t.lower():
            return t.strip()
    return None


def segura_tecla(codigo, segundos=1.0):
    """Mantem a tecla pressionada — andar no jogo precisa de tecla SEGURA,
       nao de toque."""
    e = Quartz.CGEventCreateKeyboardEvent(None, codigo, True)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)
    fim = time.time() + segundos
    while time.time() < fim:
        e = Quartz.CGEventCreateKeyboardEvent(None, codigo, True)
        Quartz.CGEventSetIntegerValueField(e, Quartz.kCGKeyboardEventAutorepeat, 1)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)
        time.sleep(0.03)
    e = Quartz.CGEventCreateKeyboardEvent(None, codigo, False)
    Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)
    time.sleep(0.2)


SIMB = {"(": (25, True), ")": (29, True), '"': (39, True), ":": (41, True),
        ".": (47, False), "=": (24, False), "_": (27, True), "+": (24, True),
        ">": (47, True), "-": (27, False), ",": (43, False)}


def digita_codigo(texto, pausa=0.05):
    """Digita letra por letra, como o aluno faz. Serve para DESCOBRIR o que o
       editor faz sozinho (fechar aspas, fechar parenteses, autocompletar)."""
    for ch in texto:
        if ch == "\n":
            tecla(36); time.sleep(pausa * 3); continue
        if ch == "\t":
            tecla(48); time.sleep(pausa); continue
        b = ch.lower()
        if b in TECLAS:
            tecla(TECLAS[b], shift=ch.isupper())
        elif ch in SIMB:
            cod, sh = SIMB[ch]
            tecla(cod, shift=sh)
        else:
            raise ValueError(f"nao sei digitar {ch!r}")
        time.sleep(pausa)


def tecla_rapida(codigo, cmd=False, shift=False):
    flags = 0
    if cmd:   flags |= Quartz.kCGEventFlagMaskCommand
    if shift: flags |= Quartz.kCGEventFlagMaskShift
    for baixo in (True, False):
        e = Quartz.CGEventCreateKeyboardEvent(None, codigo, baixo)
        Quartz.CGEventSetFlags(e, flags)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, e)
        time.sleep(0.004)
