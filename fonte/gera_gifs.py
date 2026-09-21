#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta os clipes de uma aula a partir do alvos.json do motor."""
import json, os, importlib
import gif

# os caminhos de conteudo sao relativos a fonte/: rode de onde quiser
import os as _os; _os.chdir(_os.path.dirname(_os.path.abspath(__file__)))

RECEITAS = [
  ("aba_modelo",      "01_aba_modelo.gif",      "gesto",    (0,0,2600,1600), 860),
  ("criar",           "02_criar_peca.gif",      "gesto",    (0,0,2600,1600), 860),
  ("ancorar",         "03_ancorar.gif",         "gesto",    (900,0,2940,1600), 820),
  ("tamanho",         "04_tamanho.gif",         "par",      (900,0,2940,1700), 820),
  ("cor",             "05_cor.gif",             "cor",      (600,0,2700,1500), 880),
  ("material",        "06_material.gif",        "material", (600,0,2700,1500), 880),
  ("renomear",        "07_renomear.gif",        "gesto",    (1400,0,2940,1500), 800),
  ("inserir_script",  "08_inserir_script.gif",  "menu",     (900,0,2940,1700), 860),
  ("voltar",          "09_voltar_ao_mundo.gif", "gesto",    (0,100,2000,1400), 800),
  ("jogar",           "10_jogar.gif",           "jogo",     (0,0,2600,1600), 860),
  ("parar",           "11_parar.gif",           "jogo",     (0,0,2600,1600), 860),
]


def monta(pasta):
    gif.D = pasta
    gif.OUT = os.path.join(pasta, "gifs")
    os.makedirs(gif.OUT, exist_ok=True)
    A = json.load(open(os.path.join(pasta, "alvos.json")))
    feitos = []
    for chave, saida, tipo, box, larg in RECEITAS:
        c = A.get(chave)
        if not c:
            continue
        if tipo == "gesto":
            r = gif.gesto(saida, c["antes"], c["depois"], c["alvo"], box=box, larg=larg)
        elif tipo == "par":
            r = gif.gesto(saida, c["antes"], c["depois"], [1470, 900], box=box, larg=larg,
                          n_mov=4, n_clique=1)
        elif tipo == "cor":
            r = gif.sequencia(saida, [(c["antes"], c["alvo_seta"]), (c["paleta"], c["alvo_hex"]),
                                      (c["armada"], c["alvo_aplicar"]), (c["depois"], None)],
                              box=box, larg=larg, extras=[c["limpo"]])
        elif tipo == "material":
            r = gif.sequencia(saida, [(c["antes"], c["alvo_seta"]), (c["picker"], c["alvo_busca"]),
                                      (c["busca"], c["alvo_neon"]), (c["depois"], None)],
                              box=box, larg=larg, extras=[c["limpo"]])
        elif tipo == "menu":
            r = gif.sequencia(saida, [(c["antes"], c["alvo_mais"]), (c["menu"], c["alvo_item"]),
                                      (c["depois"], None)], box=box, larg=larg)
        elif tipo == "jogo":
            r = gif.sequencia(saida, [(c["antes"], c["alvo"]), (c["depois"], None)],
                              box=box, larg=larg, extras=c.get("quadros", [])[1:])
        feitos.append((saida, r[1], r[2]))
    return feitos


if __name__ == "__main__":
    import sys
    for n, q, s in monta(sys.argv[1]):
        print(f"  {n:<26} {q:>3} quadros  {s//1024:>4} KB")
