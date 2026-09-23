#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Captura da Aula 11 — Um letreiro na tela (ScreenGui + TextLabel).

   Pontos que a captura tem de PROVAR (estavam marcados no RETOMAR.md como
   escritos sem Studio):
   - o campo Size de um TextLabel aceita os quatro numeros "1, 0, 0, 60";
   - TextScaled marcado faz a letra crescer;
   - jogador.PlayerGui.Aviso.Texto.Text e mesmo o caminho que muda o letreiro
     na tela de quem esta jogando."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(sys.path[0])
import rs, estudio as E, motor

D = "aula11"

CHEGADA = """local chegada = script.Parent

chegada.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tjogador.PlayerGui.Aviso.Texto.Text = "VOCE CHEGOU!"
\tend
end)"""

LAVA = """local lava = script.Parent

lava.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tjogador.PlayerGui.Aviso.Texto.Text = "Caiu! Tente de novo."
\t\tparte.Parent.Humanoid.Health = 0
\tend
end)"""

NOME = """local chegada = script.Parent

chegada.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tjogador.PlayerGui.Aviso.Texto.Text = jogador.Name .. " chegou!"
\tend
end)"""

AVISO = "Pule a lava e chegue no verde"

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
    return A


@etapa
def gui(A=None):
    """A folha (ScreenGui) e o letreiro (TextLabel), dentro do StarterGui."""
    A = A or liga()
    J = A.J
    E.limpa_popups(J)
    l = E.acha_linha(J, "StarterGui")
    assert l, "nao achei o StarterGui no Explorador"
    rs.confere(); rs.clique_img(l[0], l[1], escala=2.0, janela=J); time.sleep(0.8)
    A.cap("s_sgui_a")

    A.insere_buscando("StarterGui", "ScreenGui", "s_screen", "inserir_screengui")
    A.renomeia("ScreenGui", "Aviso", tag="s_screennome")
    A.insere_buscando("Aviso", "TextLabel", "s_label", "inserir_textlabel")
    A.renomeia("TextLabel", "Texto", tag="s_labelnome")

    # o que a aula manda o aluno digitar, na ordem em que ela manda
    E.poe_prop(J, "Texto", "Size", "1, 0, 0, 60")
    E.poe_prop(J, "Texto", "Text", AVISO)
    A.cap("s_labelsize_b")
    E.marca_prop(J, "Texto", "TextScaled", "game.StarterGui.Aviso.Texto.TextScaled")
    A.cap("s_labelscaled_b")
    return A


@etapa
def cena(A=None):
    """A lava vermelha e a plataforma verde da chegada."""
    A = A or liga()
    J = A.J
    A.cria_peca("s_criar")
    E.poe_prop(J, "Part", "Size", "60, 1, 4")
    E.poe_prop(J, "Part", "Position", "0, 0.5, -20")
    A.pinta("vermelho", "Bright red", alvo="Part", tag="s_corlava")
    A.ancora(alvo="Part", tag="s_anclava")
    A.renomeia("Part", "Lava", tag="s_nomelava")

    A.cria_peca("s_criar2")
    E.poe_prop(J, "Part", "Size", "10, 1, 10")
    E.poe_prop(J, "Part", "Position", "0, 0.5, -34")
    A.pinta("verde", "Bright green", alvo="Part", tag="s_corcheg")
    A.ancora(alvo="Part", tag="s_anccheg")
    A.renomeia("Part", "Chegada", tag="s_nomecheg")

    E.enquadra(J, "Chegada", atras=40)
    A.cap("s_cena_b")
    return A


@etapa
def teste1(A=None):
    """Jogar so para ver o letreiro — ainda sem uma linha de codigo."""
    A = A or liga()
    J = A.J
    E.enquadra(J, "Chegada", atras=40)
    A.cap("s_jogar_a")
    E.joga(J, espera=12.0); time.sleep(3)
    A.cap("s_jogar_b"); time.sleep(2); A.cap("s_jogar_c")
    A.reg("jogar", antes="s_jogar_a.png", depois="s_jogar_b.png",
          quadros=["s_jogar_b.png", "s_jogar_c.png"], alvo=[225, 28])
    # PROVA: o letreiro esta na tela, com o texto que a aula mandou escrever
    assert E.texto_na_tela(J, AVISO.split()[0]), "o letreiro nao apareceu no jogo"
    A.para("s_parar")
    return A


@etapa
def chegada(A=None):
    """O script da Chegada: o jogo passa a falar com quem esta jogando."""
    A = A or liga()
    J = A.J
    A.insere_script("Chegada", tag="s_chegscript")
    A.codigo("local chegada = script.Parent", CHEGADA,
             tem=("Touched", "PlayerGui", "CHEGOU"), foto="p_chegada_pronto",
             reg_nome="codigo_chegada")
    A.volta("s_volta")
    A.anda_ate(J, "Chegada", "CHEGOU", tag="s_jogar2", atras=40)
    return A


@etapa
def lava(A=None):
    """O script da Lava: o mesmo letreiro, do outro lado da historia."""
    A = A or liga()
    J = A.J
    A.insere_script("Lava", tag="s_lavascript")
    A.codigo("local lava = script.Parent", LAVA,
             tem=("Touched", "PlayerGui", "Health"), foto="p_lava_pronto",
             reg_nome="codigo_lava")
    A.volta("s_volta2")
    A.anda_ate(J, "Lava", "Caiu", tag="s_jogar3", atras=34)
    return A


@etapa
def nome(A=None):
    """A troca da linha do meio: o letreiro passa a dizer o nome do jogador."""
    A = A or liga()
    J = A.J
    A.abre_script_de("Chegada")
    rs.escreve_codigo(J, NOME, tem=("jogador.Name", "chegou"))
    A.cap("p_nome_pronto")
    A.volta("s_volta3")
    E.enquadra(J, "Chegada", atras=44)
    A.cap("p_cena")
    return A


def main():
    alvo = sys.argv[1] if len(sys.argv) > 1 else None
    nomes = [g.__name__ for g in ETAPAS]
    fns = ETAPAS if not alvo else ETAPAS[nomes.index(alvo):]
    A = None
    for f in fns:
        print(f"== {f.__name__} ==", flush=True)
        A = f() if A is None else f(A)
    print("== fim ==")


if __name__ == "__main__":
    main()
