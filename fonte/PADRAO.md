# Como se faz uma aula de Roblox da Robotomia

Este arquivo é o contrato. Quem for escrever uma aula nova — pessoa ou agente —
lê isto antes e não inventa formato próprio. Cada regra aqui nasceu de um
defeito real que passou pela leitura e só apareceu quando alguém **seguiu a
aula como aluno**.

---

## 0. Onde as coisas moram

Um repositório só: `github.com/shoio/robotomia-roblox`.

```
/                      ← O SITE PUBLICADO (GitHub Pages serve a raiz)
  index.html             a capa com os cartões das aulas
  aulaN/
    index.html           a página da aula
    aulaN.pdf            a mesma aula impressa
    fotos/*.jpg          1200 px, qualidade 84
    clipes/*.gif         os clipes de gesto
  .nojekyll

/fonte/                ← A FÁBRICA. Nada aqui é publicado.
  PADRAO.md              este arquivo
  build_curso.py         monta o site inteiro na raiz  ← o único comando
  gera_curso.py          o HTML, o CSS e o JS de uma página de aula
  faz_pdfs.py            imprime cada página em PDF (roda dentro do build)
  confere_aulas.py       o GUARDA do conteúdo (roda no começo do build)
  confere_clipes.py      confere o alvo do cursor de cada clipe
  confere_alvos.py       o OCR que o confere_clipes usa

  conteudo_a2.py … a9.py   o conteúdo de cada aula (um arquivo por aula)
  aula1/passos.json        a Aula 1, que é mais velha e ficou em JSON

  rs.py        dirige o Roblox Studio (clique, tecla, captura, OCR)
  estudio.py   as ~45 rotinas de alto nível, cada uma se conferindo
  motor.py     a classe Aula: projeto novo, cria peça, pinta, joga…
  monta.py     diferença de imagem, para MEDIR o que mudou na tela
  anota.py     desenha círculo, seta e rótulo em cima da captura
  gif.py       monta o clipe a partir das capturas reais
  gera_gifs.py monta todos os clipes de uma aula (as 11 receitas de gesto)
  reenc.py     reencena um gesto que faltou

  aulaN/           as capturas em tamanho cheio (JPEG q92) e o alvos.json
  aulaN/gifs/      os clipes prontos
  aula1/final/     as fotos anotadas da Aula 1
  comum/           as fotos compartilhadas por várias aulas
  historico/       scripts superados; ficam só como registro
```

**Um comando monta tudo:**

```bash
python3 fonte/build_curso.py
```

Ele roda o guarda, gera as nove páginas, converte as fotos, copia os clipes,
escreve o índice e imprime os nove PDFs. Se o guarda reprovar, ele para antes
de escrever qualquer coisa.

---

## 1. O que é uma aula da Robotomia

| | |
|---|---|
| Público | 10 a 14 anos, 20 por turma, um computador cada |
| Duração | 1 hora de aula, **50 minutos de conteúdo** |
| Tamanho | **19 ou 20 passos** — é o que cabe em 50 min |
| Projeto | **sempre começa num Baseplate novo.** As aulas são em semanas diferentes; nada depende do arquivo da semana passada |
| Sistema | o material fala de **Windows**: `Ctrl`, nunca `⌘` |
| Fim | a aula termina com alguma coisa que dá para **jogar no mesmo dia** |

### A regra que manda em todas

> **Nenhum passo pode supor que o aluno já sabe fazer aquilo.**

Não é «não repita o óbvio», é o contrário: repita. O aluno lê **um passo por
vez**, não a página. Um passo que delega — «use a receita», «como na aula
passada», «igual ao de cima» — parece completo na leitura contínua e é o que
mais deixa a criança parada. O passo onde a mão se mexe carrega o procedimento
inteiro, mesmo repetindo o vizinho.

---

## 2. O formato de um passo

Cada aula é um dicionário `AULA` num arquivo `conteudo_aN.py`:

```python
AULA = {
 "n": 5, "slug": "aula5",
 "titulo": "Moedas e placar",
 "subtitulo": "Encostou, sumiu, somou — com o placar na tela.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 5 · moedas",
 "fim": "Acabou a Aula 5. …",           # o parágrafo de fechamento
 "avisos": [("Título", "texto"), …],     # os cartõezinhos da capa
 "passos": [ dict(…), … ],
}
```

E cada passo:

| campo | obrigatório | o que é |
|---|---|---|
| `n` | sim | o número; tem de ser 1, 2, 3… sem buraco |
| `titulo` | sim | verbo no imperativo: «Crie a peça», «Pinte de azul» |
| `img` | sim | caminho da foto de origem, ex. `aula5/s_cor_e.jpg` |
| `clipe` | não | nome do GIF em `aula5/gifs/`, ou `None` |
| `corpo` | sim | a instrução. HTML simples: `<b>`, `<br>`, `<i>`, `<span class=ui>` |
| `codigo` | não | o código que o aluno digita, como string com `\t` de verdade |
| `auto` | com `codigo` | as linhas que **o editor escreve sozinho** (os `end`) |
| `depois` | não | o parágrafo depois do bloco de código |
| `ck` | sim | o quadro **verde**: como o aluno sabe que deu certo |
| `sos` | sim | o quadro **laranja**: lista de `(sintoma, conserto)` |

`<span class=ui>Assim</span>` é para **nome de botão, aba, menu ou campo** —
tudo que o aluno procura na tela. `<b>` é ênfase. Não misture.

### O quadro verde (`ck`)

Descreve o que **aparece na tela**, não o que o aluno deveria ter feito.
«O botão Âncora ficou aceso, com um fundo mais claro que os outros» serve;
«você ancorou a peça» não serve, porque não dá para conferir.

### O quadro laranja (`sos`)

O sintoma é a frase que a criança diria, e vem primeiro: *«Cliquei e não
aconteceu nada»*, *«Sumiu tudo do meu mundo!»*. O conserto é uma ou duas
frases. Este quadro é o que evita 20 mãos levantadas ao mesmo tempo — é ele
que faz a aula rodar com um professor só.

---

## 3. Código: o aluno digita

O aluno **digita** o código, nunca copia. O bloco sai assim:

```python
dict(n=7, titulo="Escreva o placar", img="aula5/p_placar_pronto.jpg",
     codigo=PLACAR, auto=(10,),
     corpo="Este é o código que cria o placar. Nove linhas:", …)
```

`auto` marca as linhas que **o editor do Studio escreve sozinho** quando o
aluno aperta Enter — os `end` e o `end)`. Elas saem em cinza itálico, com o
rodapé «as linhas em cinza o editor escreve sozinho — não digite elas». Sem
isso o aluno digita os `end` também e termina com três a mais. O guarda exige
que `auto` seja **exatamente** as linhas que começam com `end`.

### As três configurações que têm de estar desligadas

Toda aula que digita código tem, **como passo 2**, o passo *«Prepare o editor
(uma vez em cada computador)»*, que desliga em `Configurações do Studio`:

1. `Ativar assistente de código` — senão o **Tab** aceita a sugestão da IA em
   vez de recuar, e o editor escreve linhas que ninguém pediu;
2. `Colchetes de fechamento automáticos`;
3. `Aspas de fechamento automáticas`.

Não basta mandar «faça o passo 2 da Aula 2»: o computador da semana pode ser
outro e o aluno pode ter faltado. O passo é **da própria aula**.

### A aspa é tecla muda (teclado brasileiro)

Medido três vezes na tela do Studio:

| o aluno faz | o que sai |
|---|---|
| `"` e depois a letra | `Instance.new("IntValue")` vira `Instance.new(ÏntValue")` |
| `"` no fim da linha, e Enter | `"leaderstats"` vira `"leaderstats""` |
| `"` e depois a **barra de espaço** | `"` limpa, sem espaço — resolve os dois |

Todo bloco de código que tem aspa ganha esse aviso no rodapé (automático, em
`gera_curso.bloco_codigo`) e um socorro no quadro laranja. O guarda cobra.

### Nunca mande apertar Tab

O editor já recua sozinho. Com o assistente ligado, Tab aceita a sugestão.

---

## 4. Foto e clipe

Cada passo tem uma **foto da tela**. Os passos de **gesto novo** ganham
também um **clipe**: um GIF curto com o cursor saindo, andando até o botão,
clicando, e a tela mudando. O leitor troca entre clipe e foto por duas abas.

Regras:

- **Nada de tela desenhada.** Toda imagem é captura do Studio de verdade.
- O cursor do clipe tem de cair **no botão que o texto nomeia**. Um clipe da
  Aula 8 apontava «Personagem» enquanto o texto mandava clicar em «Parte»,
  porque a captura tinha sido feita com a faixa noutra aba. Por isso existe
  `confere_clipes.py`, que faz OCR num recorte em volta do alvo de cada gesto
  e compara com o rótulo esperado. **33 gestos, 0 errados** — rode sempre.
- **Se o clipe mostra um gesto, o texto tem de nomear esse gesto.** O passo 12
  da Aula 9 tinha um clipe inserindo um `Script` e a palavra «Script» não
  aparecia na instrução: quem seguia o passo terminava com um Script vazio.
- No PDF o clipe vira a foto (o `@media print` troca), então **o PDF nunca
  perde um passo**.

O clipe se monta de um par **antes/depois** mais o ponto do alvo, que ficam
registrados no `aulaN/alvos.json`. `gera_gifs.py` monta todos de uma vez.

O GIF é otimizado com paleta única tirada de **6 quadros espalhados** pelo
clipe (amostrar só o primeiro e o último deixa a paleta de cores do Studio
cinzenta), `disposal=1` e `optimize=True`: 2 MB viram ~110 KB.

---

## 5. O guarda

`confere_aulas.py` roda no começo de todo build e **para o build** se
reprovar. Regras, e o defeito que cada uma tapa:

| regra | o defeito que ela pegou |
|---|---|
| numeração 1..N sem buraco | inserir um passo e esquecer de renumerar |
| quem digita código tem o passo «Prepare o editor», e ele desliga as **duas** coisas | o passo só existia na Aula 2 |
| toda aula manda ir para a aba `Modelo` | a Aula 9 nunca mandava; sem ela os botões «não existem» na tela |
| `auto` == exatamente as linhas `end` | três `end)` no script do aluno |
| código com aspa tem o socorro da tecla muda | `Instance.new(ÏntValue")` |
| todo passo de código avisa do popup de sugestão | o Enter aceita a sugestão |
| toda referência «Aula N, passo M» existe | a renumeração quebrou a de outra aula |
| termo marcado numa referência existe no passo apontado | «Volte ao passo 9 e confira o `leaderstats`» apontando para outro assunto |
| passo que insere Script diz que código vai dentro | Script vazio |
| se o clipe insere Script, a **instrução** fala em Script | a palavra estava só no quadro laranja |

**Toda regra nova se sabota uma vez** para ver reprovar. Duas das regras acima
nasceram verdes por engano: uma lia a página inteira quando devia ler só a
instrução, outra procurava uma palavra que o próprio socorro continha.

---

## 6. A pipeline de captura

Quem grava as telas dirige o Roblox Studio por script, em laço fechado:
clica, **confere na tela** que aconteceu, e só então segue.

- `rs.py` — o motorista: `clique_img`, `tecla`, `digita_codigo`, `captura`,
  `ocr` (Tesseract `por+eng`, com TSV para coordenada), `escreve_codigo`.
- `estudio.py` — as rotinas que a aula usa: `seleciona`, `insere_em`,
  `pinta`, `material`, `ancora`, `poe_prop`, `abre_editor`, `joga`, `para`.
  Cada uma **verifica o próprio efeito** e tenta de novo.
- `motor.py` — `class Aula`: `projeto_novo`, `cria_peca`, `enquadra`,
  `renomeia`, `codigo`, `joga`, `cap`, `reg`.

Coisas que custaram caro e estão resolvidas dentro dessas funções — não
reimplemente:

- **Nada de coordenada fixa.** Todo botão se acha **pelo texto**, com OCR: a
  faixa se reorganiza e a janela pode ganhar ou perder a barra de título.
- **`Cmd+A` no Studio seleciona OBJETOS, não texto.** `Cmd+A` + `Delete` num
  painel já apagou a cena inteira duas vezes. Em campo de propriedade é
  seguro **só** porque logo depois vem a digitação, que substitui.
- **A cor se aplica em três cliques**: a setinha abre a paleta, o hexágono
  **arma** a cor, e o clique no **círculo** do botão `Cor` é quem pinta. E o
  interruptor «Clique no objeto para aplicar a cor» tem de ficar **desligado**
  — ligado, o botão `Cor` para de funcionar.
- **A seleção lava a cor na captura.** Confira a cor pelo painel de
  Propriedades ou num quadro sem seleção, nunca no pixel selecionado.
- **Janela fantasma**: a lista do sistema guarda janelas já fechadas, e clicar
  nelas manda o clique para a janela de trás. `janela_de_verdade()` detecta.
- **`F` enquadra a câmera só com o mouse em cima do mundo 3D.** Na lista, o
  `F` começa a renomear a peça.

---

## 7. Fazer uma aula nova, do zero

1. **Escrever o roteiro** antes de tocar no Studio: os 19–20 passos em uma
   linha cada, com o que cada um constrói e o que o aluno vê.
2. **Copiar o `conteudo_aN.py` mais parecido** e trocar o conteúdo. Nunca
   começar de um arquivo vazio — o formato inteiro vem de graça.
3. **Gravar no Studio**: `motor.Aula` num Baseplate novo, seguindo os passos
   na ordem, com `cap()` a cada mudança e `reg()` nos gestos que vão virar
   clipe. Isso produz `aulaN/*.jpg` e `aulaN/alvos.json`.
4. **Montar os clipes**: `python3 fonte/gera_gifs.py aulaN`.
5. **Conferir os clipes**: `python3 fonte/confere_clipes.py` — 0 errados.
6. **Rodar a aula de verdade**, em jogo, provando que o código funciona.
7. **`python3 fonte/build_curso.py`** — o guarda roda junto.
8. **Ler a aula como aluno**, um passo por vez, sem usar o que você sabe.
   É neste passo que aparecem os defeitos que nenhum guarda pega.
9. Commitar e empurrar. O GitHub Pages publica em ~1 minuto.

### Acrescentar uma aula à lista

Em `build_curso.py`: uma linha em `PLANO`, uma função `aulaN()` e o nome na
tupla do laço. São três linhas.

---

## 8. Vários agentes ao mesmo tempo

O que **não** paraleliza:

- **O Roblox Studio é um só.** A captura é serial: um agente por vez dirige o
  Studio. É a etapa mais cara e é o gargalo real.
- **O build e o `git push`** são seriais. `git add -A` num repositório
  compartilhado entrega a fatia do outro agente junto — commite **com
  pathspec**, e o `add` e o `commit` no mesmo comando.

O que paraleliza bem:

- **Escrever o conteúdo.** Um arquivo `conteudo_aN.py` por aula, sem nada
  compartilhado entre eles: dois agentes escrevendo as aulas 10 e 11 nunca
  tocam no mesmo arquivo.
- **A revisão «como aluno»** de aulas diferentes.
- **Roteirizar** a sequência inteira antes de qualquer captura.

Divisão que funciona: **um agente captura** (serial, no Studio) enquanto os
**outros escrevem o texto** das aulas cujo roteiro já está fechado; no fim, um
agente só roda o build e publica. O que garante o mesmo formato não é
disciplina de cada um — é o `conteudo_aN.py` copiado de um irmão mais o
`confere_aulas.py`, que reprova o build de quem saiu do padrão.

---

## 9. O que ainda está torto

Dito para quem for continuar, não para esconder:

- Todas as capturas são de **macOS**, e o material fala de **Windows**. As
  telas são quase iguais, mas não são iguais.
- Os passos da Aula 4 que acontecem no **site** da Roblox não têm foto.
- **Nada foi testado com crianças de verdade** ainda.
