# -*- coding: utf-8 -*-
"""Aula 14 — A porta que desliza (TweenService)."""

VAIVEM = '''local TweenService = game:GetService("TweenService")
local plataforma = script.Parent

local destino = plataforma.Position + Vector3.new(0, 0, -24)
local jeito = TweenInfo.new(3, Enum.EasingStyle.Sine, Enum.EasingDirection.InOut, -1, true)

local anda = TweenService:Create(plataforma, jeito, {Position = destino})
anda:Play()'''

PORTA = '''local TweenService = game:GetService("TweenService")
local porta = script.Parent
local aviso = porta.ProximityPrompt

local fechada = porta.Position
local aberta = porta.Position + Vector3.new(0, 12, 0)

local abre = TweenService:Create(porta, TweenInfo.new(1.5), {Position = aberta})
local fecha = TweenService:Create(porta, TweenInfo.new(1.5), {Position = fechada})

aviso.Triggered:Connect(function(jogador)
\tabre:Play()
\ttask.wait(5)
\tfecha:Play()
end)'''

AULA = {
 "n": 14,
 "slug": "aula14",
 "titulo": "A porta que desliza",
 "subtitulo": "Nada mais de coisas que somem: hoje as peças se movem de verdade, devagar e bonito, sozinhas.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 14 · movimento",
 "fim": "Acabou a Aula 14. Até hoje, para uma peça sair do lugar, ela tinha de sumir e reaparecer. Agora ela <b>desliza</b> — e você só precisou dizer para onde e em quanto tempo.",
 "avisos": [
   ("Projeto novo", "Esta aula começa do zero, num projeto novo."),
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Vem da Aula 13", "A porta usa o <span class=ui>ProximityPrompt</span>, o balãozinho de apertar E. Se você faltou naquela aula, o passo 12 mostra como pôr um."),
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

  dict(n=3, titulo="Abra a lista e vá para a aba MODELO", img="aula14/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique na <b>setinha</b> à esquerda de <span class=ui>Workspace</span> para abrir a lista, e depois na aba <span class=ui>Modelo</span>.",
    ck="A faixa mostra <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho a aba Modelo","Ela fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=4, titulo="Faça a plataforma que vai e volta", img="aula14/s_plat_b.jpg", clipe="02_criar_peca.gif",
    corpo="<span class=ui>Parte</span> → <span class=ui>Âncora</span>.<br><br>Nas <span class=ui>Propriedades</span>: <b>size</b> = <b>8, 1, 8</b> e <b>position</b> = <b>0, 4, -8</b>. Pinte de <b>azul</b> e renomeie para <b>Plataforma</b>.<br><br>A <span class=ui>Âncora</span> é obrigatória hoje: peça sem âncora cai, e o que vai movê-la é o código, não a física.",
    ck="Uma plataforma azul quadrada, flutuando um pouco acima do chão.",
    sos=[("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete."),
         ("Ela cai quando eu jogo","Faltou a <span class=ui>Âncora</span>.")]),

  dict(n=5, titulo="Ponha um Script na plataforma", img="aula14/s_script_c.jpg", clipe="08_inserir_script.gif",
    corpo="Clique na <span class=ui>Plataforma</span>, clique no <b>+</b> e escolha <span class=ui>Script</span>.",
    ck="Abriu o editor, e o Script está dentro da Plataforma.",
    sos=[("O Script ficou fora","Arraste-o por cima da palavra <span class=ui>Plataforma</span> na lista.")]),

  dict(n=6, titulo="Escreva o vaivém", img="aula14/p_vaivem_pronto.jpg", clipe=None,
    codigo=VAIVEM, auto=(),
    corpo="Apague a linha pronta (clique no fim dela e segure <b>Backspace</b>) e escreva as oito linhas:",
    depois="Repare: <b>não tem nenhum <span class=ui>end</span></b>. Não há <span class=ui>function</span> nem <span class=ui>if</span> nem <span class=ui>while</span> — só instruções, uma embaixo da outra. É o código mais curto do curso e o que faz a coisa mais bonita.<br><br><b>Não aperte Tab.</b>",
    ck="Nenhum risco vermelho, e as oito linhas estão todas coladas na margem esquerda.",
    sos=[("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço."),
         ("Risco vermelho na linha do TweenInfo","Confira as chaves <b>{ }</b> da última linha e os parênteses. São muitos: conte os que abrem e os que fecham."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever."),
         ("Escrevi Vector3 com v minúsculo","Tem de ser <b>Vector3</b>, com V maiúsculo e o número 3 colado.")]),

  dict(n=7, titulo="Jogue e olhe", img="aula14/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Aperte o <b>▶</b>.<br><br>A plataforma sai andando sozinha, desacelera no fim, volta, e faz isso para sempre. Suba nela.",
    ck="A plataforma vai e volta sem parar, suavemente, e leva você junto quando você está em cima.",
    sos=[("Ela não se mexe","Confira se sobrou risco vermelho e se você clicou fora do editor antes de jogar."),
         ("Ela pisca em vez de deslizar","Você pôs o destino muito longe e o tempo muito curto. Confira o <b>3</b> do TweenInfo."),
         ("Ela vai mas não volta","Faltou o <b>true</b> no fim do TweenInfo — é ele que manda voltar."),
         ("Ela vai só uma vez","Faltou o <b>-1</b>. É ele que quer dizer “repita para sempre”.")]),

  dict(n=8, titulo="Entenda as três partes", img="aula14/p_vaivem_pronto.jpg", clipe=None,
    corpo="Mexer uma peça com suavidade precisa de três coisas, e cada uma é uma linha:<br><br><b>O destino</b> — <span class=ui>plataforma.Position + Vector3.new(0, 0, -24)</span>. Não é um lugar fixo: é <i>onde ela está</i> mais 24 passos para trás. Por isso funciona onde quer que você a ponha.<br><br><b>O jeito</b> — <span class=ui>TweenInfo.new(3, ..., -1, true)</span>. Três segundos, suave nas pontas, repetir <b>para sempre</b> (-1), e <b>voltar</b> no caminho (true).<br><br><b>O movimento</b> — <span class=ui>TweenService:Create(quem, jeito, {o que muda})</span>, e depois <span class=ui>:Play()</span>. Entre as chaves você diz <b>qual propriedade</b> vai mudar.",
    ck="Você consegue dizer qual dos três números faz a plataforma andar mais longe.",
    sos=[("Qual é qual?","O <b>-24</b> é a distância. O <b>3</b> é o tempo. O <b>-1</b> é quantas vezes.")]),

  dict(n=9, titulo="Brinque com os números", img="aula14/p_vaivem_pronto.jpg", clipe=None,
    corpo="Pare o jogo e experimente, um de cada vez:<br><br>• troque o <b>-24</b> por <b>-60</b> — ela anda muito mais;<br>• troque o <b>3</b> por <b>0.5</b> — vira um chicote;<br>• troque <span class=ui>Vector3.new(0, 0, -24)</span> por <span class=ui>Vector3.new(0, 20, 0)</span> — ela passa a subir e descer;<br>• troque <span class=ui>Sine</span> por <span class=ui>Bounce</span> — ela quica ao chegar.",
    ck="Você testou pelo menos três variações e sabe dizer o que cada número faz.",
    sos=[("Bounce deu erro","Escreva <span class=ui>Enum.EasingStyle.Bounce</span>, com B maiúsculo."),
         ("Ficou rápido demais e travou","Nada quebrou. Ponha um número maior no tempo.")]),

  dict(n=10, titulo="Agora a porta: faça a peça", img="aula14/s_porta_b.jpg", clipe=None,
    corpo="Pare o jogo. Mais uma peça: <span class=ui>Parte</span> → <span class=ui>Âncora</span>.<br><br><b>size</b> = <b>12, 12, 1</b> e <b>position</b> = <b>0, 6, -30</b>. Pinte de <b>vermelho</b> e renomeie para <b>Porta</b>.<br><br>Alta e fina, plantada no chão, atravessada no caminho.",
    ck="Uma parede vermelha em pé, mais à frente que a plataforma.",
    sos=[("Ficou meio enterrada","O segundo número da position é a altura. Com 12 de altura, use <b>6</b>."),
         ("Ficou deitada","A ordem do size é largura, altura, comprimento: <b>12, 12, 1</b>.")]),

  dict(n=11, titulo="Faça um degrau para chegar na porta", img="aula14/s_degrau_b.jpg", clipe=None,
    corpo="<span class=ui>Parte</span> → <span class=ui>Âncora</span>, <b>size</b> = <b>10, 1, 10</b>, <b>position</b> = <b>0, 0.5, -24</b>.<br><br>É só um chão em frente à porta, para você ter onde parar e apertar o E.",
    ck="Há um chão logo antes da parede vermelha.",
    sos=[("Não precisa disto?","Precisa: sem um lugar firme na frente da porta, você não consegue ficar parado para apertar a tecla.")]),

  dict(n=12, titulo="Ponha o balão de apertar E na porta", img="aula14/s_prompt_c.jpg", clipe="14_inserir_prompt.gif",
    corpo="Clique na <span class=ui>Porta</span>, clique no <b>+</b> e busque <b>proximity</b>. Clique em <span class=ui>ProximityPrompt</span>.<br><br>Nas <span class=ui>Propriedades</span> dele: <span class=ui>ActionText</span> = <b>Abrir</b>, <span class=ui>ObjectText</span> = <b>Porta</b>, <span class=ui>MaxDistance</span> = <b>12</b>.",
    ck="Dentro de <span class=ui>Porta</span> está o <span class=ui>ProximityPrompt</span>, com os textos preenchidos.",
    sos=[("A busca não acha","Escreva só <b>proxi</b>, sem espaço."),
         ("Entrou no lugar errado","Arraste-o por cima da palavra <span class=ui>Porta</span> na lista.")]),

  dict(n=13, titulo="Ponha um Script na porta", img="aula14/s_script2_c.jpg", clipe=None,
    corpo="Clique na <span class=ui>Porta</span>, clique no <b>+</b> e escolha <span class=ui>Script</span>.",
    ck="Dentro da Porta estão o <span class=ui>ProximityPrompt</span> e o <span class=ui>Script</span>.",
    sos=[("Já tenho um Script na plataforma","Este é outro. Cada peça tem o seu.")]),

  dict(n=14, titulo="Escreva o código da porta", img="aula14/p_porta_pronto.jpg", clipe=None,
    codigo=PORTA, auto=(15,),
    corpo="Apague a linha pronta e escreva as quinze linhas:",
    depois="A diferença para o vaivém: aqui há <b>dois</b> movimentos guardados, o <span class=ui>abre</span> e o <span class=ui>fecha</span>, e nenhum dos dois toca sozinho. Eles esperam o <span class=ui>Triggered</span>.<br><br>Repare que <span class=ui>fechada</span> é guardada <b>antes</b> de a porta se mexer — é a posição de onde ela saiu, e é para lá que ela volta.<br><br><b>Não digite a linha em cinza.</b> E <b>não aperte Tab</b>.",
    ck="Nenhum risco vermelho.",
    sos=[("Diz que ProximityPrompt não é membro de Porta","Ou ele não está dentro da Porta, ou você o renomeou. O nome tem de ser o de fábrica."),
         ("A porta sobe e não desce","Falta o <span class=ui>fecha:Play()</span>, ou ele ficou fora do bloco."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço."),
         ("Sobrou end a mais","Você digitou o que o editor já tinha escrito. Apague o extra."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=15, titulo="Atravesse a porta", img="aula14/s_jogar2_b.jpg", clipe=None,
    corpo="Aperte o <b>▶</b>, suba na plataforma que vai e volta, desça no degrau, chegue perto da porta e aperte <b>E</b>.<br><br>Ela sobe deslizando, fica cinco segundos aberta e desce.",
    ck="A porta subiu devagar, você passou por baixo, e ela desceu sozinha.",
    sos=[("A porta some em vez de subir","Você escreveu <span class=ui>Transparency</span> no lugar de <span class=ui>Position</span> dentro das chaves."),
         ("Ela sobe pouco","Aumente o <b>12</b> do <span class=ui>Vector3.new(0, 12, 0)</span>."),
         ("Não dá tempo de passar","Troque o <span class=ui>task.wait(5)</span> por <b>8</b>."),
         ("A porta me empurra quando desce","É normal: ela é sólida. Saia de baixo dela.")]),

  dict(n=16, titulo="Faça a porta deslizar para o LADO", img="aula14/p_porta_pronto.jpg", clipe=None,
    corpo="Uma troca só, na linha do <span class=ui>aberta</span>:<br><br><span class=ui>local aberta = porta.Position + Vector3.new(14, 0, 0)</span><br><br>Agora ela corre para o lado, como porta de shopping, em vez de subir.<br><br>Os três números do <span class=ui>Vector3</span> são, nesta ordem: <b>lados</b>, <b>altura</b>, <b>frente e trás</b>.",
    ck="A porta desliza para o lado quando você aperta E.",
    sos=[("Ela some dentro da parede","Não há parede — ela desliza no vazio mesmo. Se quiser esconder, ponha uma peça grossa ao lado."),
         ("Quero que ela gire","Girar é com <span class=ui>CFrame</span> e <span class=ui>CFrame.Angles</span>, que você viu na Aula 7. Dá para tweenar CFrame também, mas fica para outro dia.")]),

  dict(n=17, titulo="Teste como se fosse outra pessoa", img="aula14/s_jogar3_b.jpg", clipe=None,
    corpo="Jogue e faça o que um jogador chato faria:<br><br>• apertar <b>E</b> várias vezes seguidas;<br>• ficar em cima da porta quando ela sobe;<br>• pular da plataforma em movimento.<br><br>Anote o que ficar estranho.",
    ck="Você achou pelo menos um comportamento esquisito.",
    sos=[("Apertei E duas vezes e ela ficou no meio","É o mesmo problema da Aula 13. O conserto também: <span class=ui>aviso.Enabled = false</span> na primeira linha de dentro, e <span class=ui>aviso.Enabled = true</span> na última.")]),

  dict(n=18, titulo="Conserte o E apertado duas vezes", img="aula14/p_conserto_pronto.jpg", clipe=None,
    corpo="Como na Aula 13: desligue o balão enquanto a porta está aberta.<br><br>Logo depois do <span class=ui>aviso.Triggered:Connect(function(jogador)</span>, ponha:<br><span class=ui>aviso.Enabled = false</span><br><br>E depois do <span class=ui>fecha:Play()</span>, ponha:<br><span class=ui>task.wait(1.5)</span><br><span class=ui>aviso.Enabled = true</span><br><br>O <span class=ui>task.wait(1.5)</span> a mais é o tempo que a porta leva descendo: o balão só volta quando ela terminar.",
    ck="Apertando E várias vezes, a porta faz o movimento inteiro sem se atrapalhar.",
    sos=[("O balão nunca mais volta","Faltou a linha <span class=ui>aviso.Enabled = true</span>, ou ela ficou fora do bloco."),
         ("Por que 1.5?","Porque é o tempo que você pôs no <span class=ui>TweenInfo.new(1.5)</span>. Se mudar um, mude o outro.")]),

  dict(n=19, titulo="Junte tudo num caminho", img="aula14/p_cena.jpg", clipe=None,
    corpo="Cinco minutos para deixar a cena jogável de ponta a ponta:<br><br>• duplique a <span class=ui>Plataforma</span> e mude a <b>position</b> da cópia, para ter duas em movimento;<br>• ponha uma lava embaixo, para cair ter consequência (receita da Aula 2);<br>• leve a porta para o fim do caminho.<br><br>Cada cópia da plataforma já vem com o script e anda sozinha.",
    ck="Dá para atravessar do começo ao fim usando as plataformas e a porta.",
    sos=[("As duas plataformas andam juntas, coladas","Mude a <b>position</b> de uma delas, ou o tempo no TweenInfo de uma, para ficarem fora de compasso."),
         ("Caí e fiquei caindo para sempre","Ponha um chão largo embaixo de tudo, ou uma lava.")]),

  dict(n=20, titulo="Salve", img="aula14/s_parar_b.jpg", clipe=None,
    corpo="Pare o jogo. <b>Ctrl + S</b> → <span class=ui>Salvar em arquivo</span> → nome <b>desliza</b>.<br><br>Se quiser, publique: <span class=ui>Arquivo → Publicar na Roblox</span>.",
    ck="Salvou sem erro.",
    sos=[("Pediu para publicar","Escolha <span class=ui>Salvar em arquivo</span>."),
         ("Quero mudar a cor junto com o movimento","Dá: dentro das chaves você pode pôr mais de uma propriedade, separadas por vírgula — por exemplo <span class=ui>{Position = aberta, Transparency = 0.5}</span>.")]),
 ],
}
