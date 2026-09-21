#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta cenas exatas no Studio pela barra de comando, e fixa a camera.
   Isso e andaime MEU: o aluno nunca ve a barra de comando."""
import time, rs, monta, reenc

def liga():
    reenc.prep()
    return monta.JAN

def roda(J, lua, espera=2.2):
    rs.comando_lua(J, lua, espera)

LIMPA = ('for _,v in ipairs(workspace:GetChildren()) do '
         'if (v:IsA("BasePart") or v:IsA("Model")) and v.Name~="Baseplate" and v.Name~="Terrain" '
         'then v:Destroy() end end')

def camera(J, de, para):
    roda(J, f'workspace.CurrentCamera.CFrame = CFrame.new(Vector3.new({de[0]},{de[1]},{de[2]}),'
            f' Vector3.new({para[0]},{para[1]},{para[2]}))', 1.4)

def conta(J, classe="Part"):
    roda(J, f'local n=0 for _,v in ipairs(workspace:GetDescendants()) do if v.ClassName=="{classe}" then n=n+1 end end print("CONTA-"..n)', 1.8)
    r = rs.saida_contem(J, "CONTA-")
    return r
