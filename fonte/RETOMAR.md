# Onde parei e como retomar

**Estado em 22-09-2026, 01h.** As nove aulas do 2º bloco (10 a 18) estão
**escritas por inteiro** e passam nos guardas. **Nenhuma está publicada**: falta
a captura das telas no Studio.

## Por que parou

A tela do Mac **bloqueou** no meio da captura da Aula 10. Com a sessão
bloqueada o `CGWindowListCreateImage` devolve imagem **preta**, o OCR lê vazio,
e o robô que dirige o Studio fica cego — sem dizer por quê.

```bash
python3 -c "import Quartz; print(Quartz.CGSessionCopyCurrentDictionary()['CGSSessionScreenIsLocked'])"
```

## Primeira coisa a fazer

1. Destravar o Mac.
2. **Desligar o bloqueio automático da tela** — Ajustes → Tela Bloqueada →
   *Exigir senha depois...* → **Nunca**, enquanto durarem as capturas.
3. Conferir que o comando acima devolve `False`.

## Retomar a Aula 10

Sobraram 18 capturas boas, até o editor de código. O roteiro é resumível por
etapa:

```bash
python3 fonte/cap10.py lava       # refaz da lava em diante
```

Etapas, na ordem: `novo · lava · teste1 · bandeira · sss · teste2`.
Passar o nome de uma etapa roda **dela em diante**.

Depois da captura:

```bash
python3 fonte/gera_gifs.py aula10     # monta os clipes
python3 fonte/confere_clipes.py       # tem de dar 0 errados
```

Depois converter os PNG para JPEG e reescrever as referências (o mesmo que foi
feito na migração da fonte), acrescentar a aula ao `PLANO` do `build_curso.py`
com a função `aula10()`, e rodar o build.

## O que falta em cada aula

| aula | texto | mecânica provada | captura | no ar |
|---|---|---|---|---|
| 10 Checkpoint | ✅ | ✅ medida na tela | 18 de ~34 | não |
| 11 Letreiro | ✅ | ⚠️ a provar | não | não |
| 12 Som | ✅ | ⚠️ a provar | não | não |
| 13 ProximityPrompt | ✅ | ⚠️ a provar | não | não |
| 14 TweenService | ✅ | ⚠️ a provar | não | não |
| 15 Tool | ✅ | ⚠️ a provar | não | não |
| 16 Cronômetro | ✅ | ⚠️ a provar | não | não |
| 17 DataStore | ✅ | ⚠️ a provar | não | não |
| 18 Projeto livre 2 | ✅ | — (só receitas importadas) | não | não |

## Pontos que eu marquei para PROVAR no Studio

Escrevi estas aulas sem poder rodar o Studio. O código passa no `confere_lua.py`
(sintaxe), mas sintaxe não é API. Estes são os pontos que eu não consegui medir
e que a captura tem de confirmar — se algum estiver errado, o conserto é no
texto da aula, não no aluno:

- **Aula 11, passo 9** — o campo `Size` de um `TextLabel` é um UDim2. Conferir
  se o painel aceita os quatro números como `1, 0, 0, 60`.
- **Aula 12, passos 6 e 11** — conferir se o áudio da Caixa de Ferramentas
  entra **dentro do objeto selecionado** (é o que a aula manda o aluno fazer).
- **Aula 15, passo 11** — conferir se `Humanoid.JumpHeight` é mesmo o que vale
  (e se o padrão é 7.2) ou se este lugar usa `JumpPower`.
- **Aula 15, passo 18** — conferir se uma `Tool` largada no Workspace se pega
  andando por cima.
- **Aula 16, passo 17** — conferir se `CharacterAdded` dentro do `PlayerAdded`
  pega também o **primeiro** nascimento.
- **Aula 17, passos 3, 4 e 14** — o caminho todo do DataStore: publicar, ligar
  *Ativar acesso da API Studio*, e provar que o número volta. **Este é o único
  que pode não funcionar na escola** — se a conta ou a rede bloquearem, o plano
  B (no `PLANO_AULAS_10_18.md`) é trocar a aula por *Dois jogadores ao mesmo
  tempo* com `Teams`.

## Depois da captura, a engenharia reversa

Cada aula capturada ainda precisa da passada como aluno, um passo por vez —
é ela que achou os defeitos das nove primeiras. O `confere_aulas.py` cobre as
regras mecânicas; o que ele não vê é o passo que está certo e **incompleto**.
