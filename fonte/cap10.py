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
