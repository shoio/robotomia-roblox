#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Confere a SINTAXE de todo codigo das aulas com o interpretador Lua.

   Nao prova a API do Roblox — para isso so o Studio serve. Prova que nao ha
   'end' faltando, parentese aberto nem virgula perdida, que e a familia de
   erro que mais aparece quando eu escrevo codigo sem rodar."""
import importlib, json, os, re, subprocess, tempfile

import os as _os; _os.chdir(_os.path.dirname(_os.path.abspath(__file__)))


def codigos():
    saida = []
    J = json.load(open("aula1/passos.json", encoding="utf-8"))
    for p in J:
        if p.get("codigo"):
            saida.append((1, p["n"], p["codigo"]))
    for i in range(2, 30):
        try:
            A = importlib.import_module(f"conteudo_a{i}").AULA
        except ModuleNotFoundError:
            continue
        for p in A["passos"]:
            if p.get("codigo"):
                saida.append((i, p["n"], p["codigo"]))
    return saida


def confere():
    erros = []
    for aula, passo, cod in codigos():
        with tempfile.NamedTemporaryFile("w", suffix=".lua", delete=False,
                                         encoding="utf-8") as f:
            f.write(cod); nome = f.name
        # o lua imprime a mensagem util na PRIMEIRA linha ("... near <eof>");
        # a ultima e so o rastro da pilha e nao diz nada.
        r = subprocess.run(["lua", "-e",
                            f"local f, err = loadfile({nome!r}) "
                            f"if not f then io.stderr:write(err) os.exit(1) end"],
                           capture_output=True, text=True)
        os.unlink(nome)
        if r.returncode != 0:
            msg = (r.stderr.strip().splitlines() or ["erro sem mensagem"])[0]
            msg = re.sub(r"^.*\.lua:", "linha ", msg)
            erros.append(f"aula {aula} passo {passo}: {msg}")
    return erros


if __name__ == "__main__":
    e = confere()
    for m in e:
        print("  !!", m)
    print(f"  {len(codigos())} blocos de codigo, {len(e)} com erro de sintaxe")
    raise SystemExit(1 if e else 0)
