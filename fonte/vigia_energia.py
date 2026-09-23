#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vigia de energia, tampa e tela — uma linha por MUDANCA.

   Nasceu da noite de 22-09-2026: a captura ficou presa com a tela acesa na
   bateria, e as 06:22 a tampa e o carregador mudaram de estado com 11
   segundos de diferenca. Depois nao deu para saber qual dos tres se mexeu
   primeiro, porque ninguem estava anotando.

       python3 fonte/vigia_energia.py ~/energia.log &

   Escreve so quando alguma coisa muda, mais um batimento de hora em hora,
   para dar para distinguir 'nada aconteceu' de 'o vigia morreu'.
"""
import subprocess, sys, time

ESPERA = 10.0
BATIMENTO = 3600.0


def le():
    ps = subprocess.run(["pmset", "-g", "ps"], capture_output=True, text=True).stdout
    tomada = "AC Power" in ps
    carga = ""
    for pedaco in ps.split():
        if pedaco.endswith("%;"):
            carga = pedaco.rstrip(";")
            break
    io = subprocess.run(["ioreg", "-r", "-k", "AppleClamshellState"],
                        capture_output=True, text=True).stdout
    tampa_fechada = '"AppleClamshellState" = Yes' in io
    asserts = subprocess.run(["pmset", "-g", "assertions"], capture_output=True, text=True).stdout
    presa = "PreventUserIdleDisplaySleep    1" in asserts
    return dict(tomada=tomada, carga=carga, tampa_fechada=tampa_fechada, tela_presa=presa)


def linha(e):
    return (f"tomada={'SIM' if e['tomada'] else 'NAO'} "
            f"carga={e['carga']:<5} "
            f"tampa={'FECHADA' if e['tampa_fechada'] else 'aberta'} "
            f"tela_presa_acesa={'SIM' if e['tela_presa'] else 'nao'}")


def main(saida):
    f = open(saida, "a", buffering=1)
    anterior = None
    ultimo_batimento = 0.0
    while True:
        try:
            agora = le()
        except Exception as erro:                      # um erro de leitura nao mata o vigia
            f.write(f"{time.strftime('%d-%m %H:%M:%S')}  !! nao consegui ler: {erro}\n")
            time.sleep(ESPERA); continue
        t = time.time()
        comparavel = {k: v for k, v in agora.items() if k != "carga"}
        mudou = anterior is None or comparavel != anterior
        if mudou or t - ultimo_batimento > BATIMENTO:
            marca = "MUDOU " if (mudou and anterior is not None) else "      "
            f.write(f"{time.strftime('%d-%m %H:%M:%S')}  {marca}{linha(agora)}\n")
            ultimo_batimento = t
        anterior = comparavel
        time.sleep(ESPERA)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "energia.log")
