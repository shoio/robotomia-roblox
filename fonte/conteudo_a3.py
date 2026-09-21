# -*- coding: utf-8 -*-
"""Aula 3 — Plataformas que somem."""

CODIGO = '''local piso = script.Parent

piso.Touched:Connect(function(parte)
\tlocal humano = parte.Parent:FindFirstChild("Humanoid")
\tif humano then
\t\tpiso.Transparency = 0.7
\t\tpiso.CanCollide = false
\t\ttask.wait(2)
\t\tpiso.Transparency = 0
\t\tpiso.CanCollide = true
\tend
end)'''

AULA = {
 "n": 3, "slug": "aula3",
 "titulo": "Plataformas que somem",
 "subtitulo": "Você pisa, o chão desaparece por dois segundos e volta. É o obby virando um jogo de tempo.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 3 · o código conta o tempo",
 "fim": "Acabou a Aula 3. Agora o seu código não só reage — ele espera, muda a peça e desfaz a mudança sozinho.",
 "avisos": [
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Projeto novo", "Esta aula começa do zero, num projeto novo. Você não precisa do arquivo da aula passada."),
   ("Já sabe disto", "Criar, ancorar, pintar, renomear e colocar o Script é igual à Aula 2. Se esqueceu algum, volte lá e confira."),
   ("Atalhos", "Este material usa <span class=ui>Ctrl</span>, do Windows. Num Mac, troque Ctrl por <span class=ui>⌘</span>."),
 ],
 "passos": [
  dict(n=1, titulo="Abra o Studio e escolha BASEPLATE", img="comum/c01_tela_inicial.jpg", clipe=None,
    corpo="Abra o Roblox Studio. <b>Role a página para baixo</b> até a fileira <span class=ui>Abrir um modelo</span> e clique no primeiro, o <span class=ui>Baseplate</span>.<br><br>Projeto novo, do zero. Hoje não usamos nada da aula passada.",
    ck="Abriu um mundo cinza com chão quadriculado e a plataforma clara no meio.",
    sos=[("Abriu o projeto antigo","Feche a aba dele no <b>x</b> e volte para o <b>Início</b>."),
         ("Apareceu uma janelinha de Boas-vindas por cima","Clique em <span class=ui>Voltar ao início</span>, o botão da esquerda — ou no <b>✕</b> do canto. Não clique em <span class=ui>Iniciar a introdução</span>.")]),

  dict(n=2, titulo="Prepare o editor (uma vez em cada computador)", img="comum/c06_preparar_editor.jpg", clipe=None,
    corpo="Hoje você vai <b>digitar código</b>. O Studio vem com duas ajudas que atrapalham quem está aprendendo: ele sugere linhas inteiras e fecha parênteses e aspas sozinho. Vamos desligar as duas.<br><br>No Windows: <span class=ui>Arquivo → Configurações do Studio</span>. No Mac: <span class=ui>Roblox Studio → Configurações do Studio</span>.<br><br><b>1.</b> Na busca escreva <b>assist</b> e desmarque <span class=ui>Ativar assistente de código</span>.<br><b>2.</b> Apague a busca, escreva <b>fechamento</b> e desmarque <span class=ui>Colchetes de fechamento automáticos</span> e <span class=ui>Aspas de fechamento automáticas</span>.<br><br>Feche a janela. Fica guardado no computador — se você já fez isto numa aula passada <b>neste mesmo computador</b>, é só conferir que as caixinhas continuam vazias.",
    ck="As três caixinhas estão <b>vazias</b>: assistente de código, colchetes e aspas.",
    sos=[("Não acho Configurações do Studio","No Windows é o menu <span class=ui>Arquivo</span>, bem no canto de cima à esquerda da janela."),
         ("A busca não acha nada","Escreva só <b>assist</b>, sem acento e sem mais nada."),
         ("Já está tudo desmarcado","Ótimo — este computador já foi preparado. Feche a janela e siga."),
         ("Por que desligar?","Ligado, o editor escreve linhas que você não pediu, e o <b>Tab</b> aceita a sugestão em vez de recuar. Desligado, o que está escrito na aula é exatamente o que você digita.")]),

  dict(n=3, titulo="Vá para a aba MODELO", img="aula3/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique em <span class=ui>Modelo</span>, na linha de abas lá em cima.<br><br>Sem isso os botões desta aula não aparecem na sua tela.",
    ck="A faixa mostra <span class=ui>Parte</span>, <span class=ui>Material</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho a aba","Ela fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=4, titulo="Crie a peça", img="aula3/s_criar_b.jpg", clipe="02_criar_peca.gif",
    corpo="Clique em <span class=ui>Parte</span> — no <b>desenho</b>, não na palavra.",
    ck="Nasceu um bloco cinza e apareceu <span class=ui>Part</span> na lista da direita.",
    sos=[("Nada aconteceu","Você clicou na palavra. Clique no desenho acima dela."),
         ("Criei duas","Aperte <b>Ctrl + Z</b>.")]),

  dict(n=5, titulo="Leve a câmera até ela", img="aula3/p_camera.jpg", clipe=None,
    corpo="Clique em <span class=ui>Part</span> na lista, ponha o mouse em cima do mundo 3D e aperte <b>F</b>.<br><br>Depois aperte <b>S</b> algumas vezes para afastar.",
    ck="A peça está no meio da tela, com o chão aparecendo em volta.",
    sos=[("Apertei F e nada","O mouse precisa estar em cima do mundo 3D, não da lista."),
         ("Começou a escrever o nome","Aperte <b>Esc</b>. O F foi para a lista.")]),

  dict(n=6, titulo="Ancore", img="aula3/s_ancora_b.jpg", clipe="03_ancorar.gif",
    corpo="Com a peça selecionada, clique em <span class=ui>Âncora</span>.<br><br><b>Criou, ancorou.</b> Sem isso a peça cai no segundo em que o jogo começa.",
    ck="O botão <span class=ui>Âncora</span> ficou aceso.",
    sos=[("Como confiro?","Na caixa de busca das <span class=ui>Propriedades</span> digite <b>anchor</b>: a caixinha <span class=ui>Anchored</span> fica marcada.")]),

  dict(n=7, titulo="Deixe a peça do tamanho de um chão", img="aula3/s_tam_b.jpg", clipe="04_tamanho.gif",
    corpo="Embaixo à direita fica o painel <span class=ui>Propriedades</span>. Na caixa de busca dele escreva <b>size</b>.<br><br>Sobra uma linha só: <span class=ui>Size</span>. Clique <b>duas vezes</b> no valor, apague o que está lá e escreva <b>24, 1, 24</b>. Aperte <b>Enter</b>.<br><br>Esses três números são largura, altura e comprimento.",
    ck="A peça virou uma placa larga e fina, bem maior que a plataforma clara.",
    sos=[("Só mudou um número","O campo estava com parte do texto selecionada. Clique duas vezes no valor, aperte <b>Ctrl + A</b> e só então escreva."),
         ("Não acho a caixa de busca","Fica logo abaixo do título <span class=ui>Propriedades</span>, escrita “Propriedades de filtro”."),
         ("Não tenho o painel Propriedades","Aba <span class=ui>Início</span> → botão <span class=ui>Propriedades</span>."),
         ("Apague o filtro depois","Deixe a caixa de busca vazia, senão o painel continua mostrando só uma linha."),
         ("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete.")]),

  dict(n=8, titulo="Pinte de azul", img="aula3/s_cor_e.jpg", clipe="05_cor.gif",
    corpo="Três cliques, nesta ordem:<br><br><b>1.</b> a <b>setinha</b> ao lado do círculo do botão <span class=ui>Cor</span>;<br><b>2.</b> um hexágono azul;<br><b>3.</b> o <b>círculo do botão Cor</b> — é esse que pinta.",
    ck="A placa ficou azul.",
    sos=[("Escolhi e não pintou","Falta o terceiro clique, no círculo do botão Cor."),
         ("Continua sem pintar","No rodapé do painel de cores há um interruptor “Clique no objeto para aplicar a cor”. Ele fica <b>desligado</b>.")]),

  dict(n=9, titulo="Chame a peça de PISO", img="aula3/s_nome_b.jpg", clipe="07_renomear.gif",
    corpo="Botão direito em <span class=ui>Part</span> na lista → <span class=ui>Renomear</span> → escreva <b>Piso</b> → <b>Enter</b>.",
    ck="Na lista está <span class=ui>Piso</span>.",
    sos=[("Voltou para Part","Você apertou Esc. Termine com <b>Enter</b>.")]),

  dict(n=10, titulo="Coloque um Script dentro do Piso", img="aula3/s_script_c.jpg", clipe="08_inserir_script.gif",
    corpo="Clique em <span class=ui>Piso</span> na lista. Aparece um <b>+</b> depois do nome — clique nele e escolha <span class=ui>Script</span>.",
    ck="Abriu o editor, e <span class=ui>Script</span> aparece <b>para dentro</b> de <span class=ui>Piso</span> na lista.",
    sos=[("O Script ficou fora do Piso","Arraste-o por cima da palavra <span class=ui>Piso</span> na lista."),
         ("Não aparece o +","Clique uma vez na linha do Piso primeiro.")]),

  dict(n=11, titulo="Limpe o que veio pronto", img="aula3/p_editor_nasce.jpg", clipe=None,
    corpo="O script nasce com <span class=ui>print(\"Hello world!\")</span>. Apague a linha inteira: clique no fim dela e segure <b>Backspace</b> até a linha 1 ficar vazia.",
    ck="A linha 1 está vazia.",
    sos=[("Sumiu a aba do script","Clique duas vezes em <span class=ui>Script</span> na lista.")]),

  dict(n=12, titulo="Escreva a primeira linha", img="aula3/p_linha1.jpg", clipe=None,
    codigo="local piso = script.Parent",
    corpo="Como na aula passada, a primeira linha dá um apelido para a peça:",
    depois="Agora, escrever <b>piso</b> é a mesma coisa que escrever “a placa azul”.",
    ck="Sem risco vermelho embaixo.",
    sos=[("Risco vermelho","Confira o ponto entre <span class=ui>script</span> e <span class=ui>Parent</span>, e o <b>P</b> maiúsculo."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=13, titulo="Escreva o resto", img="aula3/p_codigo_pronto.jpg", clipe=None,
    codigo=CODIGO, auto=(11, 12),
    corpo="O código inteiro fica assim:",
    depois="São <b>dois</b> <span class=ui>end</span> e o último termina com <span class=ui>)</span>. É onde todo mundo erra.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Nenhum risco vermelho, e aparecem as linhas verticais ligando o <span class=ui>function</span> ao <span class=ui>end</span>.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Risco vermelho no fim","Falta um <span class=ui>end</span> ou o <span class=ui>)</span> final."),
         ("task.wait dá erro","É <span class=ui>task.wait(2)</span>, com ponto entre task e wait."),
         ("Escrevi Transparency errado","Tem que ser exatamente assim, com T maiúsculo e y no fim."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço.")]),

  dict(n=14, titulo="Entenda o que você escreveu", img="aula3/p_codigo_pronto.jpg", clipe=None,
    corpo="<b>piso.Transparency = 0.7</b> — deixa a peça quase invisível. 0 é sólida, 1 é totalmente transparente.<br><br><b>piso.CanCollide = false</b> — <b>esta é a linha que faz você cair.</b> CanCollide é “dá para esbarrar?”. Com <span class=ui>false</span>, o boneco atravessa.<br><br><b>task.wait(2)</b> — <b>espere dois segundos.</b> O código para aqui e continua depois.<br><br>As duas últimas linhas desfazem tudo: a peça volta a ser sólida e visível.<br><br>Sem o <span class=ui>CanCollide</span> a peça só ficaria transparente e você continuaria andando por cima dela, como se fosse um vidro.",
    ck="Você sabe dizer qual linha faz o boneco cair — e não é a da transparência.",
    sos=[("Qual a diferença entre as duas?","Transparency é só aparência. CanCollide é se a peça existe para o corpo bater.")]),

  dict(n=15, titulo="Volte para o mundo", img="aula3/s_volta_b.jpg", clipe="09_voltar_ao_mundo.gif",
    corpo="Clique na aba <span class=ui>Place1</span>, ao lado da aba <span class=ui>Script</span>.",
    ck="Você está vendo a placa azul de novo.",
    sos=[("Fechei a aba do Script","Não perdeu nada. Duplo clique em <span class=ui>Script</span> na lista.")]),

  dict(n=16, titulo="Jogue e pise", img="aula3/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Aperte o <b>▶</b> azul.<br><br>Você nasce em cima da placa. No instante em que encosta, ela fica quase invisível, você atravessa e cai no chão cinza. Dois segundos depois ela volta.",
    ck="A placa azul ficou translúcida e você caiu. Depois ela voltou sólida.",
    sos=[("Nada aconteceu","Três conferências, nesta ordem: <b>1)</b> o Script está dentro do Piso? <b>2)</b> sobrou risco vermelho no código? <b>3)</b> você salvou o código antes de jogar? Basta clicar fora do editor."),
         ("Ficou transparente mas não caí","Faltou a linha <span class=ui>piso.CanCollide = false</span>."),
         ("Caí para sempre","A peça sumiu e não voltou: confira as duas últimas linhas, que desfazem a mudança.")]),

  dict(n=17, titulo="Pare o jogo", img="aula3/s_parar_b.jpg", clipe="11_parar.gif",
    corpo="Aperte o <b>quadrado vermelho</b>.<br><br>Lembre: o que você constrói com o jogo rodando <b>some</b> quando o jogo para.",
    ck="Voltou a tela de montar.",
    sos=[("Sumiu o que eu fiz","Você fez com o jogo rodando. Refaça com o jogo parado.")]),

  dict(n=18, titulo="Faça um caminho de plataformas", img="aula3/s_jogar_a.jpg", clipe=None,
    corpo="Agora o divertido. Com o jogo <b>parado</b>:<br><br><b>1.</b> Botão direito no <span class=ui>Piso</span> da lista → <span class=ui>Duplicar</span>.<br><b>2.</b> A cópia nasce no mesmo lugar. Use a ferramenta <span class=ui>Mover</span> (segundo botão da faixa, o das setas) e arraste a cópia <b>pela seta</b> para o lado.<br><b>3.</b> Repita mais duas ou três vezes, formando um caminho.<br><br>Cada cópia já vem com o script dentro. Todas somem sozinhas.",
    ck="Você tem três ou quatro placas azuis em fila, e na lista aparecem vários <span class=ui>Piso</span>.",
    sos=[("A cópia veio sem script","Você duplicou a peça errada. Apague e duplique o <span class=ui>Piso</span> que tem o <span class=ui>Script</span> dentro."),
         ("Arrastei e a peça foi para longe","<b>Ctrl + Z</b> e arraste devagar, pela seta, não pelo meio da peça."),
         ("As placas ficaram grudadas","Diminua o tamanho delas: filtro <b>size</b>, valor <b>8, 1, 8</b>.")]),

  dict(n=19, titulo="Atravesse o caminho", img="aula3/s_jogar_c.jpg", clipe=None,
    corpo="Jogue de novo e tente atravessar sem cair.<br><br>Não dá para parar: cada placa aguenta você por um instante só. Esse é o jogo.",
    ck="Você conseguiu chegar do outro lado pelo menos uma vez.",
    sos=[("É impossível","Aumente o tempo: troque <span class=ui>task.wait(2)</span> por <span class=ui>task.wait(4)</span> em uma das placas e veja a diferença."),
         ("É fácil demais","Diminua para <span class=ui>task.wait(1)</span> e afaste mais as placas.")]),

  dict(n=20, titulo="Salve", img="aula3/s_parar_b.jpg", clipe=None,
    corpo="<b>Ctrl + S</b> → <b>Salvar em arquivo</b> → nome <b>plataformas</b>.",
    ck="O pontinho de “não salvo” sumiu do nome da aba.",
    sos=[("Pediu para publicar","Escolha <b>Salvar em arquivo</b>. Publicar é a Aula 4.")]),
 ],
}
