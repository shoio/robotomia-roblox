# Onde parei e como retomar

**Estado em 23-09-2026, 08h50.** A **Aula 10 está no ar** — capturada,
conferida, provada em jogo e publicada. As Aulas 11 a 18 continuam
**escritas e sem foto nenhuma**.

| aula | texto | mecânica provada | captura | no ar |
|---|---|---|---|---|
| 10 Checkpoint | ✅ | ✅ **em jogo** | ✅ 19 fotos, 8 clipes | ✅ |
| 11 Letreiro | ✅ | ⚠️ a provar | não | não |
| 12 Som | ✅ | ⚠️ a provar | não | não |
| 13 ProximityPrompt | ✅ | ⚠️ a provar | não | não |
| 14 TweenService | ✅ | ⚠️ a provar | não | não |
| 15 Tool | ✅ | ⚠️ a provar | não | não |
| 16 Cronômetro | ✅ | ⚠️ a provar | não | não |
| 17 DataStore | ✅ | ⚠️ a provar | não | não |
| 18 Projeto livre 2 | ✅ | — | não | não |

`cap11.py` e `cap13.py` já estão escritos, **nunca rodaram**.

## Antes de qualquer captura

```bash
pmset -g ps            # tem de dizer 'AC Power'
python3 fonte/vigia_energia.py ~/energia-robotomia.log &
```

A captura **recusa começar na bateria** e **aborta** se o carregador parar.
Isso existe porque uma sessão noturna prendeu a tela acesa com o Mac na
bateria: em 6h30 na tomada ele carregou 12 pontos, porque o carregador estava
alimentando um Mac acordado com o Studio aberto.

**Espere pelo PID, nunca por texto.** Um vigia feito com `pgrep -f cap10.py`
casou com o próprio comando de espera, nunca terminou e me deixou sete horas
sem perceber que a captura tinha morrido.

## O que cada aula custa, medido na Aula 10

Seis etapas, ~25 minutos com o Studio livre. Retomar por etapa:
`python3 fonte/cap10.py bandeira` roda dela em diante.

## Armadilhas que já custaram uma captura inteira (todas consertadas)

- **`abre_editor` clica na primeira aba chamada «Script»** — e todas se chamam
  assim. A Aula 10 foi capturada uma vez inteira com o código da bandeira
  dentro da lava e `Hello world` dentro da bandeira, com as fotos do editor
  mostrando tudo certo. Agora só se escreve em editor que ainda tem a linha
  padrão (`editor_do_novo`), e no fim a captura **pergunta ao jogo** quem é o
  dono de cada código (`confere_scripts`).
- **O OCR lia vazio** em recorte grande e escuro (o painel do editor com duas
  linhas): o limiar afunda quando quase tudo é fundo. `rs.ocr(limiar=90)`.
- **A paleta de cores por coordenada fixa** entregava `Grime` no lugar de
  verde, um vão preto no lugar de azul e `New Yeller` no lugar de amarelo. O
  hexágono agora se acha **pela cor**.
- **`expande` alternava** a árvore em vez de garantir aberta; chamada duas
  vezes ela fechava, e o clique seguinte começava a **renomear** o Script.
- **Com o Workspace aberto, os serviços ficam fora da vista** e a rodinha
  **não rola** esse painel (medido). Quem resolve é fechar o Workspace:
  `E.mostra_servico`. As Aulas 11 (StarterGui) e 15 (StarterPack) vão precisar
  disto, e o texto delas tem de ensinar o gesto — o passo 18 da Aula 10 não
  ensinava e foi corrigido.
- **Janela fantasma**: nunca pegar `[0]` da lista de janelas para menu de
  contexto. `E.menu_contexto` compara a lista antes e depois.
- **A leitura larga do painel de Propriedades perde o fim do valor**
  (`Bright yellow` virava `Bright`) e a leitura estreita traz a **borda** como
  `|`. `linha_prop` usa as duas e compara por palavra com tolerância.
- **`faz_pdfs` tinha `range(1, 10)` cravado** — a Aula 10 entraria no site sem
  PDF, calada. Agora ele lê do disco.

## O que ainda NÃO existe

- **Abrir no editor um script que já tem código.** O duplo clique no
  Explorador começa a renomear. A Aula 11 (passo 19) e a 13 (passo 15)
  precisam disso: elas mandam **voltar a um script** e trocar uma linha.
  Sem resolver isso, essas duas aulas não capturam até o fim.
- A **Caixa de Ferramentas** (Aula 12): nenhum gesto dela está automatizado.
- **Aula 17 (DataStore)** depende de publicar e de ligar o acesso da API.
  Plano B no `PLANO_AULAS_10_18.md`.
