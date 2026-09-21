#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere o alvo de TODO clipe de gesto contra a captura que ele usa.
   Nasceu de um erro real: um clipe da Aula 8 apontava o cursor para
   'Personagem' enquanto o texto mandava clicar em 'Parte' — porque a captura
   tinha sido feita com a faixa noutra aba."""
import os, sys
from confere_alvos import rotulo_em

# (pasta, captura ANTES, alvo, rotulo que TEM de estar ali)
CLIPES = [
 ("aula2","s04_a.png",[1269,118],"parte"),
 ("aula2","s06_a.png",[2361,118],"ancora"),
 ("aula2","s07_a.png",[1990,118],"cor"),
 ("aula2","s08_a.png",[1885,118],"material"),
 ("aula3","s_criar_a.png",[1269,118],"parte"),
 ("aula3","s_ancora_a.png",[2361,118],"ancora"),
 ("aula3","s_cor_a.png",[1990,118],"cor"),
 ("aula4","s_criar_a.png",[1269,118],"parte"),
 ("aula4","s_ancora_a.png",[2361,118],"ancora"),
 ("aula4","s_cor_a.png",[1990,118],"cor"),
 ("aula5","s_moeda_a.png",[1269,118],"parte"),
 ("aula5","s_anc_moeda_a.png",[2361,118],"ancora"),
 ("aula5","s_cor_a.png",[1990,118],"cor"),
 ("aula6","s_porta_a.png",[1269,118],"parte"),
 ("aula6","s_anc_porta_a.png",[2362,118],"ancora"),
 ("aula6","s_botao_a.png",[1269,118],"parte"),
 ("aula6","s_cor_porta_a.png",[1990,118],"cor"),
 ("aula6","s_cor_botao_a.png",[1990,118],"cor"),
 ("aula7","s_criar_a.png",[1269,118],"parte"),
 ("aula7","s_ancora_a.png",[2361,118],"ancora"),
 ("aula7","s_cor_a.png",[1990,118],"cor"),
 ("aula8","s_moeda_a.png",[1269,179],"parte"),
 ("aula8","s_anc_moeda_a.png",[2361,175],"ancora"),
 ("aula8","s_loja_a.png",[1269,179],"parte"),
 ("aula8","s_cor_moeda_a.png",[1990,179],"cor"),
 ("aula8","s_cor_loja_a.png",[1990,179],"cor"),
 ("aula9","s_lava_a.png",[1269,115],"parte"),
 ("aula9","s_anc_lava_a.png",[2361,111],"ancora"),
 ("aula9","s_cor_lava_a.png",[1990,115],"cor"),
 ("aula9","s_mat_lava_a.png",[1885,115],"material"),
 ("aula9","s_moeda_a.png",[1269,115],"parte"),
 ("aula9","s_anc_moeda_a.png",[2361,111],"ancora"),
 ("aula9","s_cor_moeda_a.png",[1990,115],"cor"),
]


def main():
    ruins = []
    for pasta, arq, alvo, esperado in CLIPES:
        img = os.path.join(pasta, arq)
        if not os.path.exists(img):
            print(f"  {pasta}/{arq:<24} FALTA O ARQUIVO"); ruins.append((pasta, arq)); continue
        perto = rotulo_em(img, alvo[0], alvo[1])
        j = " ".join(perto).lower().replace("â", "a").replace("ã", "a").replace("ç", "c")
        ok = esperado in j
        print(f"  {pasta}/{arq:<24} {alvo} -> {perto}  {'ok' if ok else '<<< ERRADO'}")
        if not ok:
            ruins.append((pasta, arq, alvo, perto, esperado))
    print(f"\nerrados: {len(ruins)}")
    for r in ruins: print("  ", r)
    return 1 if ruins else 0


if __name__ == "__main__":
    sys.exit(main())
