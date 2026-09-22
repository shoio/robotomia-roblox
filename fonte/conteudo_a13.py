# -*- coding: utf-8 -*-
"""Aula 13 — Apertar E para usar (ProximityPrompt)."""

ALAVANCA = '''local alavanca = script.Parent
local aviso = alavanca.ProximityPrompt
local ponte = workspace.Ponte

aviso.Triggered:Connect(function(jogador)
\tponte.Transparency = 0
\tponte.CanCollide = true
\ttask.wait(5)
\tponte.Transparency = 1
\tponte.CanCollide = false
end)'''

AULA = {
 "n": 13,
 "slug": "aula13",
 "titulo": "Apertar E para usar",
 "subtitulo": "Uma alavanca que só funciona se você chegar perto e apertar uma tecla. É a primeira vez que o jogador escolhe agir.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 13 · alavanca",
 "fim": "Acabou a Aula 13. Até hoje as suas peças reagiam a ESBARRÃO: bastava encostar. Agora existe uma que espera o jogador decidir — e essa diferença é o que transforma obstáculo em quebra-cabeça.",
 "avisos": [
   ("Projeto novo", "Esta aula começa do zero, num projeto novo."),
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Uma ideia nova", "Até agora tudo era <span class=ui>Touched</span>: acontece com quem esbarra, de propósito ou sem querer. Hoje é <span class=ui>Triggered</span>: só acontece se a pessoa <b>quiser</b>."),
   ("Atalhos", "Este material usa <span class=ui>Ctrl</span>, do Windows. Num Mac, troque Ctrl por <span class=ui>⌘</span>."),
 ],
 "passos": [
  dict(n=1, titulo="Abra o Studio e escolha BASEPLATE", img="comum/c01_tela_inicial.jpg", clipe=None,
    corpo="Projeto novo. <b>Role a página para baixo</b> até <span class=ui>Abrir um modelo</span> e clique no <span class=ui>Baseplate</span>.",
    ck="Abriu o mundo cinza.",
    sos=[("Apareceu uma janelinha de Boas-vindas por cima","Clique em <span class=ui>Voltar ao início</span>, o botão da esquerda — ou no <b>✕</b> do canto. Não clique em <span class=ui>Iniciar a introdução</span>."),
         ("Abriu o projeto antigo","Feche a aba dele no <b>x</b> e volte para o Início.")]),

  dict(n=2, titulo="Prepare o editor (uma vez em cada computador)", img="comum/c06_preparar_editor.jpg", clipe=None,
    corpo="Hoje você vai <b>digitar código</b>. O Studio vem com duas ajudas que atrapalham quem está aprendendo: ele sugere linhas inteiras e fecha parênteses e aspas sozinho. Vamos desligar as duas.<br><br>No Windows: <span class=ui>Arquivo → Configurações do Studio</span>. No Mac: <span class=ui>Roblox Studio → Configurações do Studio</span>.<br><br><b>1.</b> Na busca escreva <b>assist</b> e desmarque <span class=ui>Ativar assistente de código</span>.<br><b>2.</b> Apague a busca, escreva <b>fechamento</b> e desmarque <span class=ui>Colchetes de fechamento automáticos</span> e <span class=ui>Aspas de fechamento automáticas</span>.<br><br>Feche a janela. Fica guardado no computador — se você já fez isto numa aula passada <b>neste mesmo computador</b>, é só conferir que as caixinhas continuam vazias.",
    ck="As três caixinhas estão <b>vazias</b>: assistente de código, colchetes e aspas.",
    sos=[("Não acho Configurações do Studio","No Windows é o menu <span class=ui>Arquivo</span>, bem no canto de cima à esquerda da janela."),
         ("A busca não acha nada","Escreva só <b>assist</b>, sem acento e sem mais nada."),
         ("Já está tudo desmarcado","Ótimo — este computador já foi preparado. Feche a janela e siga."),
         ("Por que desligar?","Ligado, o editor escreve linhas que você não pediu, e o <b>Tab</b> aceita a sugestão em vez de recuar.")]),

  dict(n=3, titulo="Abra a lista e vá para a aba MODELO", img="aula13/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique na <b>setinha</b> à esquerda de <span class=ui>Workspace</span> para abrir a lista, e depois na aba <span class=ui>Modelo</span>.",
    ck="A faixa mostra <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho a aba Modelo","Ela fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=4, titulo="Cave o buraco: duas beiradas e um vão", img="aula13/s_beiras_b.jpg", clipe="02_criar_peca.gif",
    corpo="O jogo de hoje é atravessar um vão. Faça <b>duas</b> peças iguais, uma de cada lado — <span class=ui>Parte</span> e <span class=ui>Âncora</span> em cada:<br><br><b>Beira de cá:</b> <b>size</b> = <b>30, 1, 10</b>, <b>position</b> = <b>0, 0.5, -10</b>.<br><b>Beira de lá:</b> <b>size</b> = <b>30, 1, 10</b>, <b>position</b> = <b>0, 0.5, -40</b>.<br><br>Entre elas sobra um vão de <b>20 passos</b> — longe demais para pular. É de propósito.",
    ck="Duas plataformas cinzas com um vão largo entre as duas.",
    sos=[("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete."),
         ("Dá para pular o vão","Então ele está curto. Confira: uma beira em <b>-10</b> e a outra em <b>-40</b>."),
         ("Não vejo as duas de uma vez","Role a rodinha do mouse para trás — a câmera afasta.")]),

  dict(n=5, titulo="Faça a ponte — e deixe-a invisível", img="aula13/s_ponte_b.jpg", clipe=None,
    corpo="Mais uma peça: <span class=ui>Parte</span> → <span class=ui>Âncora</span>, <b>size</b> = <b>6, 1, 22</b>, <b>position</b> = <b>0, 0.5, -25</b>. Ela liga as duas beiras.<br><br>Renomeie para <b>Ponte</b> — com P maiúsculo, o código vai procurar esse nome exato.<br><br>Agora <b>faça ela sumir</b>: busque <b>transparency</b> nas Propriedades e ponha <b>1</b>; depois busque <b>cancollide</b> e <b>desmarque</b>.<br><br>Ela continua na lista, mas não dá para ver nem pisar. É esse o estado inicial do jogo.",
    ck="A ponte sumiu da tela, mas <span class=ui>Ponte</span> continua na lista da direita.",
    sos=[("Sumiu e não acho mais","Ela está na lista. Clique no nome, leve o mouse ao mundo 3D e aperte <b>F</b>."),
         ("Transparency 1 e ainda dá para pisar","Faltou desmarcar o <span class=ui>CanCollide</span>. São duas coisas diferentes: uma é ver, outra é esbarrar."),
         ("Não acho CanCollide","Escreva <b>collide</b> na busca das Propriedades.")]),

  dict(n=6, titulo="Faça a alavanca", img="aula13/s_alavanca_b.jpg", clipe=None,
    corpo="Mais uma peça, pequena, na beira de cá: <span class=ui>Parte</span> → <span class=ui>Âncora</span>, <b>size</b> = <b>2, 4, 2</b>, <b>position</b> = <b>6, 2.5, -12</b>.<br><br>Pinte de <b>amarelo</b> e renomeie para <b>Alavanca</b>.",
    ck="Um postinho amarelo em pé, no canto da plataforma de cá.",
    sos=[("Ficou dentro do chão","O segundo número da position é a altura. Com size 4 de altura, use <b>2.5</b>."),
         ("Ficou longe demais","O primeiro número é para os lados. Use <b>6</b> para ela ficar na beirada.")]),

  dict(n=7, titulo="Ponha o aviso de apertar E", img="aula13/s_prompt_c.jpg", clipe="14_inserir_prompt.gif",
    corpo="Aqui está a novidade da aula. Clique na <span class=ui>Alavanca</span>, clique no <b>+</b> e, na caixa <span class=ui>Pesquisar objeto</span>, escreva <b>proximity</b>. Clique em <span class=ui>ProximityPrompt</span>.<br><br><span class=ui>Proximity</span> quer dizer <i>proximidade</i>: perto. Esta peça mostra um balãozinho na tela quando o jogador chega perto, e some quando ele se afasta. Ela <b>sozinha</b> não faz nada — só avisa.",
    ck="Dentro de <span class=ui>Alavanca</span> apareceu <span class=ui>ProximityPrompt</span>.",
    sos=[("A busca não acha","Escreva só <b>proxi</b>, sem espaço."),
         ("Entrou no lugar errado","Arraste-o por cima da palavra <span class=ui>Alavanca</span> na lista.")]),

  dict(n=8, titulo="Escreva o que o balão vai dizer", img="aula13/s_promptprop_b.jpg", clipe=None,
    corpo="Com o <span class=ui>ProximityPrompt</span> selecionado, nas <span class=ui>Propriedades</span>:<br><br><b>1.</b> busque <b>actiontext</b> e escreva <b>Abrir a ponte</b> — é o que aparece em letra grande.<br><b>2.</b> apague a busca, escreva <b>objecttext</b> e escreva <b>Alavanca</b> — é o rótulo pequeno em cima.<br><b>3.</b> busque <b>maxdistance</b> e ponha <b>10</b> — de quantos passos de longe o balão já aparece.",
    ck="As três propriedades estão preenchidas.",
    sos=[("Não acho ActionText","Escreva <b>action</b> na busca das Propriedades."),
         ("O que é HoldDuration?","É quantos segundos o jogador tem de <b>segurar</b> a tecla. Em <b>0</b> basta apertar. Experimente <b>1</b> depois, para ver a barrinha enchendo.")]),

  dict(n=9, titulo="Jogue só para ver o balão", img="aula13/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Aperte o <b>▶</b> e ande até perto do postinho amarelo.<br><br>Aperte o <b>E</b>. Não vai acontecer nada — ainda não há código. Mas o balão aparece e some conforme você chega perto e se afasta.",
    ck="O balão com <b>Abrir a ponte</b> aparece quando você chega perto da alavanca.",
    sos=[("Não aparece balão nenhum","Confira se o <span class=ui>ProximityPrompt</span> está <b>dentro</b> da Alavanca, e se o <span class=ui>MaxDistance</span> não está em 0."),
         ("Aparece de muito longe","Diminua o <span class=ui>MaxDistance</span>."),
         ("Aperto E e nada acontece","É esperado neste passo. O código vem no passo 11.")]),

  dict(n=10, titulo="Pare e ponha um Script na alavanca", img="aula13/s_script_c.jpg", clipe="08_inserir_script.gif",
    corpo="Pare o jogo no <b>quadrado vermelho</b>.<br><br>Clique na <span class=ui>Alavanca</span>, clique no <b>+</b> e escolha <span class=ui>Script</span>.",
    ck="Dentro da Alavanca estão agora o <span class=ui>ProximityPrompt</span> e o <span class=ui>Script</span>.",
    sos=[("O Script ficou fora","Arraste-o por cima da palavra <span class=ui>Alavanca</span> na lista.")]),

  dict(n=11, titulo="Escreva o código da alavanca", img="aula13/p_codigo_pronto.jpg", clipe=None,
    codigo=ALAVANCA, auto=(11,),
    corpo="Apague a linha pronta (clique no fim dela e segure <b>Backspace</b>) e escreva as onze linhas:",
    depois="Compare com a Aula 6, da porta: lá era <span class=ui>botao.Touched:Connect</span>, aqui é <span class=ui>aviso.Triggered:Connect</span>. O resto do desenho é igual.<br><br>Repare também que hoje é ao contrário: a ponte <b>aparece</b> por cinco segundos e depois some de novo. Você tem de correr.<br><br><b>Não digite a linha em cinza.</b> O editor escreve o <span class=ui>end)</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b>.",
    ck="Nenhum risco vermelho.",
    sos=[("Diz que ProximityPrompt não é membro de Alavanca","Ou ele não está dentro da Alavanca, ou você o renomeou. O nome tem de ser o de fábrica: <b>ProximityPrompt</b>."),
         ("Diz que Ponte não existe","O nome da peça na lista tem de ser exatamente <b>Ponte</b>, com P maiúsculo."),
         ("Sobrou end a mais","Você digitou o que o editor já tinha escrito. Apague o extra."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=12, titulo="Atravesse", img="aula13/s_jogar2_b.jpg", clipe=None,
    corpo="Aperte o <b>▶</b>, chegue perto da alavanca, aperte <b>E</b> — e <b>corra</b>.<br><br>A ponte aparece, você tem cinco segundos, e ela some de novo.",
    ck="Você atravessou para a outra beira antes de a ponte sumir.",
    sos=[("A ponte aparece mas eu caio","Ela apareceu mas continua atravessável: confira a linha <span class=ui>ponte.CanCollide = true</span>."),
         ("Não dá tempo","Troque o <span class=ui>task.wait(5)</span> por <b>8</b>."),
         ("Apertei E e nada","Confira se sobrou risco vermelho no código, e se você clicou fora do editor antes de jogar."),
         ("Caí no vazio e fiquei caindo para sempre","Normal no Baseplate se você passar da borda. Pare o jogo e jogue de novo.")]),

  dict(n=13, titulo="Entenda: Touched e Triggered", img="aula13/p_codigo_pronto.jpg", clipe=None,
    corpo="<b>Touched</b> — acontece com <b>quem esbarrar</b>. Não pergunta nada. Uma pedra rolando dispara igual.<br><br><b>Triggered</b> — acontece só se a pessoa <b>apertar a tecla</b>. Tem intenção.<br><br>Repare numa coisa no código: o <span class=ui>Triggered</span> já entrega o <span class=ui>jogador</span> pronto, entre os parênteses. No <span class=ui>Touched</span> a gente recebia um <i>pedaço de boneco</i> e tinha de descobrir de quem era, com o <span class=ui>GetPlayerFromCharacter</span>. Aqui não precisa: o Roblox sabe quem apertou.",
    ck="Você consegue dizer por que a alavanca não dispara sozinha quando alguém esbarra nela.",
    sos=[("Quando usar cada um?","<b>Touched</b> para armadilha e para moeda. <b>Triggered</b> para porta, botão, comprar, pegar — tudo que o jogador escolhe fazer.")]),

  dict(n=14, titulo="Faça o balão exigir que segure a tecla", img="aula13/s_hold_b.jpg", clipe=None,
    corpo="Pare o jogo. Nas <span class=ui>Propriedades</span> do <span class=ui>ProximityPrompt</span>, busque <b>holdduration</b> e ponha <b>2</b>.<br><br>Jogue de novo e segure o <b>E</b>: aparece uma barrinha enchendo. Se você soltar antes, não vale.",
    ck="A barrinha enche em dois segundos e só então a ponte aparece.",
    sos=[("Nada muda","Confira se você mudou no <span class=ui>ProximityPrompt</span> e não na Alavanca."),
         ("Para que serve isso?","Para coisas importantes: destravar um cofre, entregar um item. Evita que a pessoa faça sem querer.")]),

  dict(n=15, titulo="Use o nome de quem puxou", img="aula13/p_nome_pronto.jpg", clipe=None,
    corpo="O <span class=ui>jogador</span> que está entre os parênteses do <span class=ui>Triggered</span> serve para alguma coisa. Acrescente esta linha logo depois do <span class=ui>aviso.Triggered:Connect(function(jogador)</span>:<br><br><span class=ui>print(jogador.Name .. \" puxou a alavanca\")</span><br><br>Jogue, puxe, e olhe o painel <span class=ui>Saída</span> embaixo.",
    ck="No painel Saída aparece o seu nome de usuário seguido de “puxou a alavanca”.",
    sos=[("Não acho o painel Saída","Aba <span class=ui>Ver</span> → botão <span class=ui>Saída</span>."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço.")]),

  dict(n=16, titulo="Pinte a ponte antes de mostrar", img="aula13/s_pontecor_b.jpg", clipe=None,
    corpo="A ponte aparecendo cinza fica sem graça. Pare o jogo, clique na <span class=ui>Ponte</span> na lista e pinte de <b>azul</b>.<br><br>Cuidado: pintar <b>não</b> desfaz o Transparency. Se ela voltar a aparecer, é porque o Transparency saiu de 1 — ponha de volta.",
    ck="No jogo, a ponte que aparece é azul.",
    sos=[("A ponte voltou a ficar visível no Studio","Confira o <span class=ui>Transparency</span>: tem de estar em <b>1</b> enquanto você monta."),
         ("Não consigo clicar nela no mundo 3D","Ela está invisível e sem colisão. Clique no nome dela <b>na lista</b>.")]),

  dict(n=17, titulo="Ponha uma segunda alavanca do outro lado", img="aula13/p_cena.jpg", clipe=None,
    corpo="Para conseguir voltar, você precisa de uma alavanca na beira de lá.<br><br>Botão direito na <span class=ui>Alavanca</span> → <span class=ui>Duplicar</span>. A cópia já vem com o balão <b>e</b> com o script dentro. Mude a <b>position</b> dela para <b>6, 2.5, -38</b>.",
    ck="Há uma alavanca amarela em cada beira, e as duas abrem a mesma ponte.",
    sos=[("A cópia não funciona","Você duplicou a peça errada. Apague e duplique a <span class=ui>Alavanca</span> que tem o ProximityPrompt e o Script dentro."),
         ("As duas ficaram no mesmo lugar","Mude a position da <b>cópia</b>, não da original.")]),

  dict(n=18, titulo="Teste como se fosse outra pessoa", img="aula13/s_jogar3_b.jpg", clipe=None,
    corpo="Jogue e faça o que um jogador chato faria:<br><br>• apertar <b>E</b> duas vezes seguidas;<br>• apertar <b>E</b> e <b>não</b> atravessar;<br>• apertar <b>E</b> nas duas alavancas ao mesmo tempo.<br><br>Anote o que ficar estranho. Uma coisa vai ficar — e é sobre ela o próximo passo.",
    ck="Você achou pelo menos um comportamento esquisito.",
    sos=[("Não achei nada esquisito","Aperte E, espere a ponte sumir, e aperte E de novo bem rápido, várias vezes seguidas.")]),

  dict(n=19, titulo="Conserte o E apertado duas vezes", img="aula13/p_conserto_pronto.jpg", clipe=None,
    corpo="Apertando <b>E</b> duas vezes seguidas, a ponte some <b>antes</b> dos cinco segundos: o segundo aperto começa a contar de novo e o primeiro termina no meio, mandando ela sumir.<br><br>O conserto é uma linha no começo do código, que desliga o balão enquanto a ponte está aberta, e outra no fim, que liga de volta:<br><br>logo depois do <span class=ui>Connect(function(jogador)</span>, ponha <span class=ui>aviso.Enabled = false</span>;<br>e na última linha de dentro, depois do <span class=ui>ponte.CanCollide = false</span>, ponha <span class=ui>aviso.Enabled = true</span>.",
    ck="Apertando E várias vezes seguidas, o balão some enquanto a ponte está aberta e volta quando ela fecha.",
    sos=[("O balão nunca mais volta","Faltou a linha <span class=ui>aviso.Enabled = true</span> no fim, ou ela ficou fora do bloco."),
         ("Por que isto acontece?","Porque cada aperto roda o código <b>de novo</b>, sem esperar o anterior terminar. Desligar o balão é a forma mais simples de impedir o segundo aperto.")]),

  dict(n=20, titulo="Salve", img="aula13/s_parar_b.jpg", clipe=None,
    corpo="Pare o jogo. <b>Ctrl + S</b> → <span class=ui>Salvar em arquivo</span> → nome <b>alavanca</b>.<br><br>Se quiser, publique: <span class=ui>Arquivo → Publicar na Roblox</span>.",
    ck="Salvou sem erro.",
    sos=[("Pediu para publicar","Escolha <span class=ui>Salvar em arquivo</span>."),
         ("Quero uma alavanca que só funciona uma vez","Depois do <span class=ui>Triggered</span>, ponha <span class=ui>aviso:Destroy()</span> em vez de religar o balão.")]),
 ],
}
