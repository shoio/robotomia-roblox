#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Captura da Aula 10 — Checkpoint: a bandeira que salva.

   A mecanica foi MEDIDA antes de escrever a aula (ver PADRAO.md):
   RespawnLocation so funciona se a SpawnLocation estiver Enabled E Neutral;
   e com duas delas ligadas o Roblox SORTEIA onde o jogador nasce — por isso
   a aula tem o script do PlayerAdded fixando a Largada."""
import os, sys, time, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(sys.path[0])
import rs, estudio as E, motor

D = "aula10"
LAVA = """local lava = script.Parent

lava.Touched:Connect(function(parte)
\tlocal humano = parte.Parent:FindFirstChild("Humanoid")
\tif humano then
\t\thumano.Health = 0
\tend
end)"""

BANDEIRA = """local bandeira = script.Parent

bandeira.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tjogador.RespawnLocation = bandeira
\tend
end)"""

LARGADA = """game.Players.PlayerAdded:Connect(function(jogador)
\tjogador.RespawnLocation = workspace.Largada
end)"""


ETAPAS = []


def etapa(fn):
    ETAPAS.append(fn); return fn


def liga(nova=False):
    A = motor.Aula(D)
    A.J = motor.projeto_novo_confiavel() if nova else E.liga()
    if E.em_teste(A.J):
        E.para(A.J); time.sleep(4); A.J = E.liga()
    return A


@etapa
def novo():
    A = liga(nova=True)
    A.aba_modelo("s_aba")
    A.renomeia("SpawnLocation", "Largada", tag="s_largada")
    return A


@etapa
def lava(A=None):
    A = A or liga()
    J = A.J
    A.cria_peca("s_criar")
    E.poe_prop(J, "Part", "Size", "60, 1, 4")
    E.poe_prop(J, "Part", "Position", "0, 0.5, -20")
    E.enquadra(J, "Part", atras=34)
    A.cap("s_tam_b")
    A.reg("tamanho", antes="s_criar_b.png", depois="s_tam_b.png", valor="60, 1, 4")
    A.pinta("vermelho", "Bright red", alvo="Part", tag="s_cor")
    A.renomeia("Part", "Lava", tag="s_nome")
    A.insere_script("Lava", tag="s_script")
    A.codigo("local lava = script.Parent", LAVA, tem=("Touched", "Humanoid", "Health"))
    A.volta("s_volta")
    return A


@etapa
def teste1(A=None):
    A = A or liga()
    J = A.J
    E.enquadra(J, "Lava", atras=34)
    A.cap("s_jogar_a")
    E.joga(J, espera=12.0); time.sleep(3)
    A.cap("s_jogar_b"); time.sleep(2); A.cap("s_jogar_c")
    A.reg("jogar", antes="s_jogar_a.png", depois="s_jogar_b.png",
          quadros=["s_jogar_b.png", "s_jogar_c.png"], alvo=[225, 28])
    A.cap("p_no_jogo")
    A.para("s_parar")
    return A


@etapa
def bandeira(A=None):
    A = A or liga()
    J = A.J
    E.limpa_popups(J)
    # o SpawnLocation nao esta na lista curta do '+': entra pela busca
    l, m, usado = E.menu_do_mais(J, "Workspace")
    A.cap("s_band_a")
    mo_x, mo_y = int((m["x"] - J["x"]) * 2), int((m["y"] - J["y"]) * 2)
    from PIL import Image
    comp = Image.open(rs.captura(J["id"], "/tmp/_mm.png")[0]).convert("RGB")
    rs.captura(m["id"], "/tmp/_mp.png")
    comp.paste(Image.open("/tmp/_mp.png").convert("RGB"), (mo_x, mo_y))
    comp.save(f"{D}/s_band_b.png")
    rs.confere(); rs.clique_tela(m["x"] + m["w"] / 2, m["y"] + 14); time.sleep(0.8)
    rs.digita_teclas("spawn"); time.sleep(1.8)
    alvo = E.item_do_menu(m, "SpawnLocation")
    assert alvo, "a busca do menu nao achou SpawnLocation"
    rs.confere(); rs.clique_tela(*alvo); time.sleep(2.6)
    A.cap("s_band_c")
    A.reg("inserir_spawn", antes="s_band_a.png", menu="s_band_b.png", depois="s_band_c.png",
          alvo_mais=[usado, l[1]],
          alvo_item=[int((alvo[0] - m["x"]) * 2) + mo_x, int((alvo[1] - m["y"]) * 2) + mo_y])

    E.poe_prop(J, "SpawnLocation", "Position", "0, 0.5, -32")
    A.pinta("verde", "Bright green", alvo="SpawnLocation", tag="s_bandcor")
    A.renomeia("SpawnLocation", "Bandeira", tag="s_bandnome")
    A.insere_script("Bandeira", tag="s_bandscript")
    E.abre_editor(J)
    rs.escreve_codigo(J, BANDEIRA, tem=("Touched", "RespawnLocation", "jogador"))
    A.cap("p_cp_pronto")
    A.volta("s_volta2")
    return A


@etapa
def sss(A=None):
    A = A or liga()
    J = A.J
    # a segunda lava, DEPOIS da bandeira, para provar o checkpoint
    E.limpa_popups(J)
    l = E.acha_linha(J, "Lava")
    A.cap("s_dup_a")
    rs.clique_direito_img(l[0], l[1], escala=2.0, janela=J); time.sleep(1.6)
    menu = [j for j in rs.janelas() if j["w"] > 150 and j["h"] > 150 and j["camada"] >= 100]
    assert menu, "o menu do botao direito nao abriu"
    E.clica_item(J, menu[0], "Duplicar", 2.2)
    E.poe_prop(J, "Lava", "Position", "0, 0.5, -45", )
    E.enquadra(J, "Bandeira", atras=42)
    A.cap("s_dup_b")
    A.reg("duplicar", antes="s_dup_a.png", depois="s_dup_b.png", alvo=[l[0], l[1]])

    A.insere_script_em("ServerScriptService", "s_sss")
    E.abre_editor(J)
    rs.escreve_codigo(J, LARGADA, tem=("PlayerAdded", "RespawnLocation", "Largada"))
    A.cap("p_sss_pronto")
    A.volta("s_volta3")
    return A


@etapa
def teste2(A=None):
    A = A or liga()
    J = A.J
    E.enquadra(J, "Bandeira", atras=42)
    A.cap("s_jogar2_a")
    E.joga(J, espera=12.0); time.sleep(3)
    A.cap("s_jogar2_b"); time.sleep(2); A.cap("s_jogar2_c")
    A.reg("jogar2", antes="s_jogar2_a.png", depois="s_jogar2_b.png",
          quadros=["s_jogar2_b.png", "s_jogar2_c.png"], alvo=[225, 28])
    A.para("s_parar2")
    E.enquadra(J, "Bandeira", atras=48)
    A.cap("p_cena")
    return A


def main():
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    fns = ETAPAS if not alvo else [f for f in ETAPAS
                                   if ETAPAS.index(f) >= [g.__name__ for g in ETAPAS].index(alvo)]
    A = None
    for f in fns:
        print(f"== {f.__name__} ==", flush=True)
        A = f() if A is None else f(A)
    print("== fim ==")


if __name__ == "__main__":
    main()
