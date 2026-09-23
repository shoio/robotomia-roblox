#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Captura da Aula 13 — Apertar E para usar (ProximityPrompt).

   O que esta captura tem de PROVAR, porque a aula foi escrita sem Studio:
   - o ProximityPrompt entra pela BUSCA do menu do '+' (nao esta na lista curta);
   - ActionText/ObjectText/MaxDistance sao mesmo os nomes dos campos;
   - o balao aparece perto e o E dispara o Triggered;
   - HoldDuration=2 troca o toque por segurar."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(sys.path[0])
import rs, estudio as E, motor

D = "aula13"

ALAVANCA = """local alavanca = script.Parent
local aviso = alavanca.ProximityPrompt
local ponte = workspace.Ponte

aviso.Triggered:Connect(function(jogador)
\tponte.Transparency = 0
\tponte.CanCollide = true
\ttask.wait(5)
\tponte.Transparency = 1
\tponte.CanCollide = false
end)"""

COM_NOME = """local alavanca = script.Parent
local aviso = alavanca.ProximityPrompt
local ponte = workspace.Ponte

aviso.Triggered:Connect(function(jogador)
\tprint(jogador.Name .. " puxou a alavanca")
\tponte.Transparency = 0
\tponte.CanCollide = true
\ttask.wait(5)
\tponte.Transparency = 1
\tponte.CanCollide = false
end)"""

CONSERTO = """local alavanca = script.Parent
local aviso = alavanca.ProximityPrompt
local ponte = workspace.Ponte

aviso.Triggered:Connect(function(jogador)
\taviso.Enabled = false
\tprint(jogador.Name .. " puxou a alavanca")
\tponte.Transparency = 0
\tponte.CanCollide = true
\ttask.wait(5)
\tponte.Transparency = 1
\tponte.CanCollide = false
\taviso.Enabled = true
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
    return A


@etapa
def cena(A=None):
    """As duas beiras, o vao, a ponte invisivel e a alavanca."""
    A = A or liga()
    J = A.J
    A.cria_peca("s_beiras")
    E.poe_prop(J, "Part", "Size", "30, 1, 10")
    E.poe_prop(J, "Part", "Position", "0, 0.5, -10")
    A.ancora(alvo="Part", tag="s_ancbeira")
    A.renomeia("Part", "BeiraCa", tag="s_nomebeira")

    A.cria_peca("s_beira2")
    E.poe_prop(J, "Part", "Size", "30, 1, 10")
    E.poe_prop(J, "Part", "Position", "0, 0.5, -40")
    A.ancora(alvo="Part", tag="s_ancbeira2")
    A.renomeia("Part", "BeiraLa", tag="s_nomebeira2")
    E.enquadra(J, "BeiraCa", atras=46)
    A.cap("s_beiras_b")

    A.cria_peca("s_ponte")
    E.poe_prop(J, "Part", "Size", "6, 1, 22")
    E.poe_prop(J, "Part", "Position", "0, 0.5, -25")
    A.ancora(alvo="Part", tag="s_ancponte")
    A.renomeia("Part", "Ponte", tag="s_nomeponte")
    E.poe_prop(J, "Ponte", "Transparency", "1")
    E.marca_prop(J, "Ponte", "CanCollide", "workspace.Ponte.CanCollide", quero=False)
    E.enquadra(J, "BeiraCa", atras=46)
    A.cap("s_ponte_b")

    A.cria_peca("s_alav")
    E.poe_prop(J, "Part", "Size", "2, 4, 2")
    E.poe_prop(J, "Part", "Position", "6, 2.5, -12")
    A.pinta("amarelo", "Bright yellow", alvo="Part", tag="s_coralav")
    A.ancora(alvo="Part", tag="s_ancalav")
    A.renomeia("Part", "Alavanca", tag="s_nomealav")
    E.enquadra(J, "Alavanca", atras=20)
    A.cap("s_alavanca_b")
    return A


@etapa
def prompt(A=None):
    """O ProximityPrompt e os tres campos que a aula manda preencher."""
    A = A or liga()
    J = A.J
    A.insere_buscando("Alavanca", "ProximityPrompt", "s_prompt", "inserir_prompt")
    E.poe_prop(J, "ProximityPrompt", "ActionText", "Abrir a ponte")
    E.poe_prop(J, "ProximityPrompt", "ObjectText", "Alavanca")
    E.poe_prop(J, "ProximityPrompt", "MaxDistance", "10")
    A.cap("s_promptprop_b")
    return A


@etapa
def teste1(A=None):
    """Jogar so para ver o balao — ainda sem uma linha de codigo."""
    A = A or liga()
    J = A.J
    A.anda_ate(J, "Alavanca", "Abrir a ponte", tag="s_jogar", atras=22, palavras=("abrir", "alavanca"))
    return A


@etapa
def codigo(A=None):
    """O script da alavanca, e a travessia."""
    A = A or liga()
    J = A.J
    A.insere_script("Alavanca", tag="s_script")
    A.codigo("local alavanca = script.Parent", ALAVANCA,
             tem=("Triggered", "Transparency", "CanCollide"))
    A.volta("s_volta")
    A.puxa_alavanca(J, "Alavanca", tag="s_jogar2")
    return A


@etapa
def segurar(A=None):
    """HoldDuration: o toque vira segurar."""
    A = A or liga()
    J = A.J
    E.poe_prop(J, "ProximityPrompt", "HoldDuration", "2")
    A.cap("s_hold_b")
    A.abre_script_de("Alavanca")
    rs.escreve_codigo(J, COM_NOME, tem=("jogador.Name", "puxou"))
    A.cap("p_nome_pronto")
    A.volta("s_volta2")
    return A


@etapa
def fim(A=None):
    """A ponte azul, a segunda alavanca e o conserto do E duas vezes."""
    A = A or liga()
    J = A.J
    A.pinta("azul", "Bright blue", alvo="Ponte", tag="s_pontecor")
    E.poe_prop(J, "Ponte", "Transparency", "1")      # pintar nao desfaz, mas confiro
    E.enquadra(J, "BeiraCa", atras=46)
    A.cap("s_pontecor_b")

    A.duplica(J, "Alavanca", tag="s_dup")
    E.poe_prop(J, "Alavanca", "Position", "6, 2.5, -38", n=1)
    E.enquadra(J, "Ponte", atras=52)
    A.cap("p_cena")

    A.abre_script_de("Alavanca")
    rs.escreve_codigo(J, CONSERTO, tem=("aviso.Enabled", "false", "true"))
    A.cap("p_conserto_pronto")
    A.volta("s_volta3")
    A.puxa_alavanca(J, "Alavanca", tag="s_jogar3")
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
