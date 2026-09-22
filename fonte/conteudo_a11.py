# -*- coding: utf-8 -*-
"""Aula 11 — Um letreiro na tela (ScreenGui + TextLabel)."""

CHEGADA = '''local chegada = script.Parent

chegada.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tjogador.PlayerGui.Aviso.Texto.Text = "VOCE CHEGOU!"
\tend
end)'''

VOLTOU = '''local lava = script.Parent

lava.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tjogador.PlayerGui.Aviso.Texto.Text = "Caiu! Tente de novo."
\t\tparte.Parent.Humanoid.Health = 0
\tend
end)'''

AULA = {
 "n": 11,
 "slug": "aula11",
 "titulo": "Um letreiro na tela",
 "subtitulo": "O jogo passa a falar com quem está jogando: um aviso no alto da tela que muda conforme o que acontece.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 11 · letreiro",
 "fim": "Acabou a Aula 11. O seu jogo agora avisa, cobra e parabeniza. Até hoje o jogador tinha de adivinhar o que fazer; a partir de agora você conta para ele.",
 "avisos": [
   ("Projeto novo", "Esta aula começa do zero, num projeto novo."),
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Uma pasta nova da lista", "Hoje você vai mexer no <span class=ui>StarterGui</span>, que fica na lista da direita algumas linhas abaixo de Workspace. É a caixa das coisas que aparecem <b>na tela</b>, não no mundo."),
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

  dict(n=3, titulo="Abra a lista e vá para a aba MODELO", img="aula11/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique na <b>setinha</b> à esquerda de <span class=ui>Workspace</span> para abrir a lista, e depois na aba <span class=ui>Modelo</span>, na linha de cima.",
    ck="A faixa mostra <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho a aba Modelo","Ela fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=4, titulo="Ache o StarterGui na lista", img="aula11/s_sgui_a.jpg", clipe=None,
    corpo="Na lista da direita, <b>abaixo</b> de Workspace, há uma fileira de caixas do Roblox: Players, Lighting, ReplicatedStorage, ServerScriptService… Procure <span class=ui>StarterGui</span>.<br><br><span class=ui>Gui</span> se lê “gúi” e quer dizer <i>as coisas que aparecem na tela</i>: letreiros, botões, barras de vida. Tudo que você puser aqui dentro aparece na tela de <b>todo</b> jogador quando ele entra.",
    ck="Você está vendo a linha <span class=ui>StarterGui</span> na lista da direita.",
    sos=[("Não consigo rolar a lista","Use a rodinha do mouse em cima da lista, ou escreva <b>starter</b> na caixa <span class=ui>Pesquisar</span> no alto dela."),
         ("Tem vários nomes parecidos","Você quer o <b>StarterGui</b> — não o StarterPack nem o StarterPlayer.")]),

  dict(n=5, titulo="Crie a tela: um ScreenGui", img="aula11/s_screen_c.jpg", clipe="12_inserir_screengui.gif",
    corpo="Clique em <span class=ui>StarterGui</span>, clique no <b>+</b> e, na caixa <span class=ui>Pesquisar objeto</span>, escreva <b>screen</b>. Clique em <span class=ui>ScreenGui</span>.<br><br>Um <span class=ui>ScreenGui</span> é a <b>folha transparente</b> que fica na frente da tela do jogador. Sozinho ele não mostra nada — é onde a gente cola as coisas.",
    ck="Dentro de <span class=ui>StarterGui</span> apareceu <span class=ui>ScreenGui</span>.",
    sos=[("Entrou no lugar errado","Apague com <b>Delete</b> e refaça com o <span class=ui>StarterGui</span> selecionado."),
         ("Não vejo nada mudar no mundo 3D","É esperado. Ele só aparece quando o jogo roda.")]),

  dict(n=6, titulo="Chame a folha de AVISO", img="aula11/s_screennome_b.jpg", clipe=None,
    corpo="Botão direito em <span class=ui>ScreenGui</span> → <span class=ui>Renomear</span> → <b>Aviso</b> → <b>Enter</b>.<br><br>Este nome é levado a sério: daqui a pouco o código vai procurar uma folha chamada exatamente <b>Aviso</b>.",
    ck="Na lista está <span class=ui>Aviso</span>, dentro de StarterGui.",
    sos=[("Voltou para ScreenGui","Você apertou <b>Esc</b>. Termine com <b>Enter</b>.")]),

  dict(n=7, titulo="Cole um letreiro na folha: o TextLabel", img="aula11/s_label_c.jpg", clipe=None,
    corpo="Clique em <span class=ui>Aviso</span>, clique no <b>+</b> e busque <b>textlabel</b>. Clique em <span class=ui>TextLabel</span>.<br><br>Um <span class=ui>TextLabel</span> é um retângulo com texto dentro. É o letreiro.",
    ck="Dentro de <span class=ui>Aviso</span> apareceu <span class=ui>TextLabel</span>.",
    sos=[("Entrou dentro do StarterGui, não do Aviso","Arraste-o por cima da palavra <span class=ui>Aviso</span> na lista."),
         ("A busca não acha","Escreva só <b>textl</b>, tudo junto e sem espaço.")]),

  dict(n=8, titulo="Chame o letreiro de TEXTO", img="aula11/s_labelnome_b.jpg", clipe=None,
    corpo="Botão direito nele → <span class=ui>Renomear</span> → <b>Texto</b> → <b>Enter</b>.<br><br>Agora o caminho completo do letreiro é <span class=ui>Aviso → Texto</span>. Guarde: é exatamente o que você vai escrever no código.",
    ck="Na lista: <span class=ui>StarterGui → Aviso → Texto</span>.",
    sos=[("Não sei se está dentro","A linha <span class=ui>Texto</span> tem de aparecer <b>mais para dentro</b> que a linha <span class=ui>Aviso</span>.")]),

  dict(n=9, titulo="Deixe o letreiro em cima e do tamanho da tela", img="aula11/s_labelsize_b.jpg", clipe=None,
    corpo="Com o <span class=ui>Texto</span> selecionado, na busca das <span class=ui>Propriedades</span> escreva <b>size</b>. O valor tem <b>quatro</b> números: duplo clique, <b>Ctrl + A</b>, escreva <b>1, 0, 0, 60</b> e <b>Enter</b>.<br><br>Os dois primeiros são a largura: <b>1</b> quer dizer <i>a tela inteira</i>. Os dois últimos são a altura: <b>60</b> pontos.<br><br>Agora busque <b>text</b> e, na linha <span class=ui>Text</span>, escreva <b>Pule a lava e chegue no verde</b>.",
    ck="No canto de cima do mundo 3D aparece uma faixa cinza com o seu texto dentro.",
    sos=[("Só mudou um número","Duplo clique no valor, <b>Ctrl + A</b>, e só então escreva os quatro números separados por vírgula."),
         ("Aparecem várias linhas com 'text'","Você quer a que se chama só <span class=ui>Text</span>. As outras são TextColor3, TextSize, TextScaled…"),
         ("Não vejo o letreiro","Ele só aparece na aba <span class=ui>Interface do usuário</span> ou quando o jogo roda. Siga em frente, você vai vê-lo no passo 12.")]),

  dict(n=10, titulo="Deixe a letra grande", img="aula11/s_labelscaled_b.jpg", clipe=None,
    corpo="Ainda nas <span class=ui>Propriedades</span> do <span class=ui>Texto</span>, busque <b>scaled</b> e <b>marque</b> a caixinha <span class=ui>TextScaled</span>.<br><br>Com ela marcada a letra cresce sozinha até encher o letreiro. Sem ela, o texto fica minúsculo numa tela grande.",
    ck="A caixinha <span class=ui>TextScaled</span> está marcada.",
    sos=[("Não acho","Escreva só <b>scaled</b> na busca das Propriedades."),
         ("A letra ficou gigante demais","Diminua a altura do letreiro: volte no <b>size</b> e troque o 60 por 40.")]),

  dict(n=11, titulo="Crie a lava e a chegada", img="aula11/s_cena_b.jpg", clipe="02_criar_peca.gif",
    corpo="Agora o mundo. Duas peças, do jeito de sempre — <span class=ui>Parte</span> e <span class=ui>Âncora</span> em cada uma:<br><br><b>A lava:</b> <b>size</b> = <b>60, 1, 4</b>, <b>position</b> = <b>0, 0.5, -20</b>, pintada de <b>vermelho</b>, renomeada para <b>Lava</b>.<br><br><b>A chegada:</b> <b>size</b> = <b>10, 1, 10</b>, <b>position</b> = <b>0, 0.5, -34</b>, pintada de <b>verde</b>, renomeada para <b>Chegada</b>.",
    ck="Uma faixa vermelha fina e, depois dela, uma plataforma verde quadrada.",
    sos=[("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete."),
         ("As peças caem quando eu jogo","Faltou a <span class=ui>Âncora</span> numa delas."),
         ("Perdi a peça de vista","Clique no nome dela na lista, leve o mouse ao mundo 3D e aperte <b>F</b>.")]),

  dict(n=12, titulo="Jogue só para ver o letreiro", img="aula11/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Aperte o <b>▶</b>. Olhe o <b>alto da tela</b>.<br><br>Ainda não há código nenhum: o letreiro aparece só porque está dentro do <span class=ui>StarterGui</span>.",
    ck="A faixa com <b>Pule a lava e chegue no verde</b> está no alto da tela do jogo.",
    sos=[("Não aparece nada","Confira o caminho na lista: <span class=ui>StarterGui → Aviso → Texto</span>, um dentro do outro."),
         ("Aparece mas está vazio","Faltou escrever na propriedade <span class=ui>Text</span>."),
         ("A faixa ficou no meio da tela","Busque <b>position</b> nas Propriedades do Texto e ponha <b>0, 0, 0, 0</b>.")]),

  dict(n=13, titulo="Pare o jogo", img="aula11/s_parar_b.jpg", clipe="11_parar.gif",
    corpo="Aperte o <b>quadrado vermelho</b>.",
    ck="Voltou a tela de montar.",
    sos=[("Sumiu o que eu fiz","Você construiu com o jogo rodando. Refaça com o jogo parado.")]),

  dict(n=14, titulo="Faça a chegada falar", img="aula11/p_chegada_pronto.jpg", clipe=None,
    codigo=CHEGADA, auto=(7, 8),
    corpo="Clique em <span class=ui>Chegada</span>, clique no <b>+</b>, escolha <span class=ui>Script</span>, apague a linha pronta e escreva:",
    depois="A linha do meio é a novidade, e ela é um <b>caminho</b>, lido da esquerda para a direita: <i>o jogador → a tela dele → a folha Aviso → o letreiro Texto → a palavra escrita nele</i>.<br><br><span class=ui>PlayerGui</span> é a cópia que cada jogador ganha do StarterGui. Cada um tem a sua: o seu letreiro muda, o do colega não.",
    ck="Nenhum risco vermelho.",
    sos=[("Diz que Aviso não é membro de PlayerGui","O nome na lista tem de ser exatamente <b>Aviso</b>, e o letreiro dentro dele exatamente <b>Texto</b>."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço."),
         ("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=15, titulo="Jogue e chegue no verde", img="aula11/s_jogar2_b.jpg", clipe=None,
    corpo="Aperte o <b>▶</b>, pule a lava com corrida (segure <b>W</b> e aperte a <b>barra de espaço</b> antes da borda) e pise na plataforma verde.",
    ck="No instante em que você pisa no verde, o letreiro muda para <b>VOCE CHEGOU!</b>",
    sos=[("O letreiro não muda","Três conferências: o Script está dentro da <span class=ui>Chegada</span>? Sobrou risco vermelho? Os nomes <b>Aviso</b> e <b>Texto</b> estão iguais aos do código?"),
         ("Deu erro vermelho na Saída","Leia o nome que aparece no erro — é quase sempre um nome de peça diferente do que está no código.")]),

  dict(n=16, titulo="Faça a lava falar também", img="aula11/p_lava_pronto.jpg", clipe=None,
    codigo=VOLTOU, auto=(8, 9),
    corpo="Pare o jogo. Ponha um <span class=ui>Script</span> dentro da <span class=ui>Lava</span> e escreva:",
    depois="Repare na ordem das duas linhas de dentro: primeiro o letreiro muda, <b>depois</b> o boneco morre. Se fosse ao contrário, o jogador morreria antes de conseguir ler.",
    ck="Nenhum risco vermelho.",
    sos=[("Morri mas não li nada","As duas linhas estão trocadas. A do letreiro vem <b>antes</b> da do Health."),
         ("Diz que Humanoid não existe","Alguma coisa sem boneco encostou na lava. Não atrapalha o jogo, mas se quiser calar o erro, use o <span class=ui>FindFirstChild(\"Humanoid\")</span> da Aula 2."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=17, titulo="Jogue: caia na lava e leia", img="aula11/s_jogar3_b.jpg", clipe=None,
    corpo="Aperte o <b>▶</b> e entre na lava de propósito.",
    ck="Deu tempo de ler <b>Caiu! Tente de novo.</b> antes de o boneco renascer.",
    sos=[("Não deu tempo de ler","É rápido mesmo. Ponha <span class=ui>task.wait(1)</span> numa linha entre as duas, para o letreiro ficar um segundo antes da morte."),
         ("O letreiro volta ao texto antigo quando eu renasço","É assim mesmo: ao renascer, o Roblox refaz a tela a partir do StarterGui. É por isso que o texto de partida é o do passo 9.")]),

  dict(n=18, titulo="Entenda o caminho", img="aula11/p_chegada_pronto.jpg", clipe=None,
    corpo="<b>StarterGui</b> é o molde. Ninguém vê o molde.<br><br><b>PlayerGui</b> é a cópia que cada jogador recebe quando entra. É nela que o código mexe.<br><br><b>jogador.PlayerGui.Aviso.Texto.Text</b> se lê assim, da esquerda para a direita: <i>desse jogador, pegue a tela dele; nela, a folha chamada Aviso; nela, o letreiro chamado Texto; nele, a palavra escrita</i>.<br><br>Cada ponto é um “de dentro de”. É o mesmo desenho do <span class=ui>jogador.leaderstats.Moedas.Value</span> da Aula 5.",
    ck="Você consegue dizer por que o letreiro do seu colega não muda quando você pisa no verde.",
    sos=[("Por que não muda o do colega?","Porque cada jogador tem o <b>seu</b> PlayerGui. O código só mexeu no de quem encostou.")]),

  dict(n=19, titulo="Escreva o nome de quem chegou", img="aula11/p_nome_pronto.jpg", clipe=None,
    corpo="Uma troca só, na linha do meio do script da <span class=ui>Chegada</span>:<br><br><span class=ui>jogador.PlayerGui.Aviso.Texto.Text = jogador.Name .. \" chegou!\"</span><br><br>O <span class=ui>..</span> (dois pontinhos) <b>gruda</b> dois textos. <span class=ui>jogador.Name</span> é o nome de quem está jogando.",
    ck="Ao pisar no verde, o letreiro mostra o <b>seu nome de usuário</b> seguido de “chegou!”.",
    sos=[("Ficou tudo grudado","Falta o espaço <b>antes</b> de chegou, dentro das aspas: <span class=ui>\" chegou!\"</span>."),
         ("Deu erro no ..","São dois pontos finais seguidos, com um espaço de cada lado.")]),

  dict(n=20, titulo="Salve", img="aula11/s_parar_b.jpg", clipe=None,
    corpo="Pare o jogo. <b>Ctrl + S</b> → <span class=ui>Salvar em arquivo</span> → nome <b>letreiro</b>.<br><br>Se quiser, publique: <span class=ui>Arquivo → Publicar na Roblox</span>.",
    ck="O pontinho de “não salvo” sumiu do nome da aba.",
    sos=[("Pediu para publicar","Escolha <span class=ui>Salvar em arquivo</span>."),
         ("Quero mudar a cor da faixa","Nas Propriedades do <span class=ui>Texto</span>, busque <b>background</b>: <span class=ui>BackgroundColor3</span> muda a cor e <span class=ui>BackgroundTransparency</span> em <b>1</b> deixa só a letra, sem caixa.")]),
 ],
}
