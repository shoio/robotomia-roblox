# Plano do 2º bloco — Aulas 10 a 18

Proposta. **Nada disto está construído ainda.** O formato, os guardas e o
processo são os do `PADRAO.md`: 19–20 passos, 50 minutos, projeto novo a cada
aula, o aluno digita o código, e a aula termina com algo jogável no mesmo dia.

---

## O que o aluno já sabe, saindo da Aula 9

**Studio:** criar peça, âncora, mover, dimensionar, cor, material, renomear,
duplicar, Explorador, painel de Propriedades, inserir `Script`, jogar e parar,
salvar em arquivo, publicar e deixar público.

**Código:** `script.Parent`, `workspace.Nome`, `Touched:Connect`,
`FindFirstChild("Humanoid")`, `if … then`, `task.wait`, `while true do`,
propriedades (`Transparency`, `CanCollide`, `Health`, `WalkSpeed`, `CFrame`),
`leaderstats` com `IntValue`, `GetPlayerFromCharacter`, `:Destroy()`,
`Instance.new`, variável para guardar número (`local preco = 3`).

**O que falta, e é o que este bloco cobre:** falar com o jogador pela tela,
som, interagir sem encostar, movimento suave, um objeto na mão, medir tempo,
e guardar o progresso de um dia para o outro.

---

## As nove aulas

| # | Aula | O que o aluno constrói | O que é novo |
|---|---|---|---|
| 10 | **Checkpoint: a bandeira que salva** | Obby com 3 bandeiras; morrer volta para a última, não para o começo | `SpawnLocation` extra, `jogador.RespawnLocation`, `Players:GetPlayerFromCharacter` de novo |
| 11 | **Um letreiro na tela** | Um aviso que muda: «Faltam 3 moedas» → «Pode passar!» | `ScreenGui` + `TextLabel` em `StarterGui`, mudar `.Text` pelo script |
| 12 | **Som** | Música de fundo, «ping» ao pegar moeda, som ao morrer | `Sound` dentro da peça, `SoundId`, `:Play()`, `Volume` |
| 13 | **Apertar E para usar** | Uma alavanca que abaixa a ponte — sem precisar encostar | `ProximityPrompt`, evento `.Triggered`, `ActionText` |
| 14 | **A porta que desliza** | Porta correndo para o lado, plataforma que vai e volta sozinha | `TweenService:Create`, `TweenInfo.new`, `:Play()` |
| 15 | **Uma ferramenta na mão** | Uma lanterna (ou martelo) que o boneco pega e usa clicando | `Tool` em `StarterPack`, `Handle`, evento `.Activated` |
| 16 | **Cronômetro e recorde** | O obby cronometrado; o placar mostra o melhor tempo da partida | `tick()`, formatar tempo, `StringValue` no `leaderstats`, `math.floor` |
| 17 | **O progresso fica salvo** | As moedas continuam amanhã, no mesmo jogo publicado | `DataStoreService`, `GetAsync`/`SetAsync`, `pcall`, `PlayerRemoving`, ligar **API Services** |
| 18 | **Projeto livre 2 e mostra** | Jogo próprio com o kit dos dois blocos, publicado e jogado pelos colegas | nada novo: escolher, montar, testar, publicar, trocar links |

### Por que nesta ordem

- **10 primeiro** porque é a dívida mais antiga: a Aula 1, no passo 18, diz
  *«Checkpoint é assunto da próxima aula»* — e checkpoint nunca aparece nas
  nove. Construir a 10 é também consertar essa frase.
- **11 e 12** são as duas coisas que mais mudam a sensação de «jogo de
  verdade» e custam pouquíssimo código. Vêm cedo de propósito.
- **13, 14 e 15** são interação: sem encostar, com movimento bonito, e com um
  objeto na mão. Cada uma é um gesto novo do Studio, não só código.
- **16** junta medir tempo com o `leaderstats` que eles já conhecem.
- **17 é a mais difícil do curso** e vai no fim por isso (ver o risco abaixo).
- **18** fecha como a 9 fechou, com mostra e troca de links.

---

## Riscos, ditos antes de construir

**Aula 17 (DataStore) é a única que pode não rodar na escola.** Ela exige:
o jogo **publicado** (Aula 4), a opção **Ativar acesso da API Studio**
(*Enable Studio Access to API Services*) ligada nas configurações do jogo, e
uma conta que possa criar experiências. Se a rede ou a conta da escola
bloquear, a aula morre em sala. **Antes de construir a 17, isso se testa na
máquina da escola.** Se não passar, o plano B no mesmo slot é
*«Dois jogadores ao mesmo tempo»* (`Teams`, teste local com 2 jogadores),
que não depende de nada externo e é igualmente motivante.

**Aula 12 (Som) depende de IDs de áudio da biblioteca da Roblox**, que saem
do ar sem aviso. Os IDs escolhidos têm de ser conferidos no dia da captura, e
a aula precisa ensinar o aluno a **procurar outro** na Caixa de Ferramentas —
senão vira aula quebrada quando o ID morrer.

**Aula 11 e 15 mexem em `StarterGui` e `StarterPack`**, que são pastas do
Explorador que o aluno nunca abriu. Cada uma precisa do passo de «role a lista
até achar», como a Aula 5 precisou para o `ServerScriptService`.

---

## Na fila, para um terceiro bloco

Ideias que não couberam, guardadas para não se perderem:

`Teams` e dois jogadores · partículas e luz (`ParticleEmitter`, `PointLight`)
· `Model` e agrupar peças · dano parcial em vez de morte (`Health - 20`) ·
câmera em primeira pessoa · terreno (`Terrain`) · animação do boneco ·
`RemoteEvent` (cliente × servidor) · loja com GUI de verdade · badges.

---

## Como construir isto com vários agentes

A conta de tempo, pelo que as nove primeiras custaram:

| etapa | paraleliza? | por quê |
|---|---|---|
| roteiro dos 20 passos | **sim** | é texto, um arquivo por aula |
| escrever o `conteudo_aN.py` | **sim** | um arquivo por aula, nada compartilhado |
| **capturar no Studio** | **não** | o Roblox Studio é um só nesta máquina — é o gargalo |
| montar e conferir os clipes | sim, depois da captura | lê só os arquivos da própria aula |
| provar a aula rodando no jogo | **não** | precisa do Studio |
| build e publicação | **não** | um agente só, com `git add` por pathspec |

**A divisão que funciona:** fecham-se os nove roteiros primeiro (paralelo);
um agente entra no Studio e captura aula por aula (serial); enquanto ele
captura a aula N, os outros escrevem o texto das aulas N+1 em diante; no fim,
um agente roda `python3 fonte/build_curso.py` e publica.

O que garante o mesmo formato não é disciplina de cada agente — é copiar o
`conteudo_aN.py` de uma aula irmã e o `confere_aulas.py`, que **reprova o
build** de quem saiu do padrão. Quem escrever uma aula nova lê o `PADRAO.md`
antes, inteiro.
