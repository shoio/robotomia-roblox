#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reencena os gestos que faltam, gravando par antes/depois e o alvo MEDIDO."""
import time, json, os, rs, monta
from PIL import Image

ESC, Z = 53, 6
V = (624, 200, 2550, 1700)          # so a area 3D
ALVOS = "aula1/alvos_gif.json"

def J(): return monta.JAN

def reg():
    return json.load(open(ALVOS)) if os.path.exists(ALVOS) else {}

def grava(nome, **kw):
    d = reg(); d[nome] = kw; json.dump(d, open(ALVOS,"w"), indent=1, ensure_ascii=False)
    print(f"  -> {nome}: {kw}")

def prep():
    monta.jan(); rs.ativa(); time.sleep(0.7); rs.confere()

def desfaz(n=1):
    for _ in range(n):
        rs.confere(); rs.tecla(Z, cmd=True); time.sleep(1.2)
