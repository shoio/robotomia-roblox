# -*- coding: utf-8 -*-
"""Aula 10 — Checkpoint: a bandeira que salva.

   A mecanica foi MEDIDA no Studio antes de a aula ser escrita:
   - RespawnLocation so obedece se a SpawnLocation estiver Enabled=true E
     Neutral=true. Com Enabled=false o Roblox ignora (medido: renasceu na
     largada, Z-3, em vez da bandeira, Z-49). Com Neutral=false, idem.
   - Com duas SpawnLocation ligadas, o nascimento de ENTRADA e SORTEADO
     (medido: 2 de 7 nascimentos cairam na bandeira). Por isso a aula tem o
     script do PlayerAdded fixando a Largada — com ele, 7 de 7 na largada."""

LAVA = '''local lava = script.Parent

lava.Touched:Connect(function(parte)
\tlocal humano = parte.Parent:FindFirstChild("Humanoid")
\tif humano then
\t\thumano.Health = 0
\tend
end)'''

BANDEIRA = '''local bandeira = script.Parent

bandeira.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tjogador.RespawnLocation = bandeira
\tend
end)'''

LARGADA = '''game.Players.PlayerAdded:Connect(function(jogador)
\tjogador.RespawnLocation = workspace.Largada
end)'''

AULA = {
 "n": 10,
 "slug": "aula10",
 "titulo": "Checkpoint: a bandeira que salva",
 "subtitulo": "Você morre e volta de onde parou, não do começo. É a peça que faltava para o seu obby ser justo.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 10 · checkpoint",
 "fim": "Acabou a Aula 10. O seu jogo agora perdoa: quem morre volta para a bandeira, não para a largada. É a diferença entre um obby que dá vontade de tentar de novo e um que dá vontade de fechar.",
 "avisos": [
   ("Projeto novo", "Esta aula começa do zero, num projeto novo. Você não precisa do arquivo da aula passada."),
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Já sabe disto", "Criar, ancorar, pintar, renomear, medir pelo painel de Propriedades e pôr um Script dentro da peça é igual às aulas passadas."),
   ("Atalhos", "Este material usa <span class=ui>Ctrl</span>, do Windows. Num Mac, troque Ctrl por <span class=ui>⌘</span>."),
 ],
 "passos": [
  dict(n=1, titulo="Abra o Studio e escolha BASEPLATE", img="comum/c01_tela_inicial.jpg", clipe=None,
    corpo="Projeto novo, como sempre. <b>Role a página para baixo</b> até a fileira <span class=ui>Abrir um modelo</span> e clique no primeiro, o <span class=ui>Baseplate</span>.",
    ck="Abriu o mundo cinza com a plataforma clara no meio.",
    sos=[("Apareceu uma janelinha de Boas-vindas por cima","Clique em <span class=ui>Voltar ao início</span>, o botão da esquerda — ou no <b>✕</b> do canto. Não clique em <span class=ui>Iniciar a introdução</span>."),
         ("Abriu o projeto antigo","Feche a aba dele no <b>x</b> e volte para o Início.")]),

  dict(n=2, titulo="Prepare o editor (uma vez em cada computador)", img="comum/c06_preparar_editor.jpg", clipe=None,
    corpo="Hoje você vai <b>digitar código</b>. O Studio vem com duas ajudas que atrapalham quem está aprendendo: ele sugere linhas inteiras e fecha parênteses e aspas sozinho. Vamos desligar as duas.<br><br>No Windows: <span class=ui>Arquivo → Configurações do Studio</span>. No Mac: <span class=ui>Roblox Studio → Configurações do Studio</span>.<br><br><b>1.</b> Na busca escreva <b>assist</b> e desmarque <span class=ui>Ativar assistente de código</span>.<br><b>2.</b> Apague a busca, escreva <b>fechamento</b> e desmarque <span class=ui>Colchetes de fechamento automáticos</span> e <span class=ui>Aspas de fechamento automáticas</span>.<br><br>Feche a janela. Fica guardado no computador — se você já fez isto numa aula passada <b>neste mesmo computador</b>, é só conferir que as caixinhas continuam vazias.",
    ck="As três caixinhas estão <b>vazias</b>: assistente de código, colchetes e aspas.",
    sos=[("Não acho Configurações do Studio","No Windows é o menu <span class=ui>Arquivo</span>, bem no canto de cima à esquerda da janela."),
         ("A busca não acha nada","Escreva só <b>assist</b>, sem acento e sem mais nada."),
         ("Já está tudo desmarcado","Ótimo — este computador já foi preparado. Feche a janela e siga."),
         ("Por que desligar?","Ligado, o editor escreve linhas que você não pediu, e o <b>Tab</b> aceita a sugestão em vez de recuar. Desligado, o que está escrito na aula é exatamente o que você digita.")]),

  dict(n=3, titulo="Abra a lista do mundo e vá para a aba MODELO", img="aula10/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Na direita fica o <span class=ui>Explorador</span>. Clique na <b>setinha</b> à esquerda de <span class=ui>Workspace</span> para abrir a lista.<br><br>Depois, na linha de cima, clique na aba <span class=ui>Modelo</span>. <b>Isto é obrigatório</b> — os botões desta aula só existem nela.",
    ck="Abaixo de Workspace apareceram <span class=ui>SpawnLocation</span> e <span class=ui>Baseplate</span>, e a faixa mostra <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho a aba Modelo","Ela fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>."),
         ("Cliquei na setinha e a lista fechou","Você clicou duas vezes. Clique uma só.")]),

  dict(n=4, titulo="Dê o nome de LARGADA para a plataforma onde você nasce", img="aula10/s_largada_b.jpg", clipe="07_renomear.gif",
    corpo="Aquela plataforma clara no meio do mundo chama-se <span class=ui>SpawnLocation</span> — é o lugar onde o seu boneco nasce. Ela já vem no Baseplate.<br><br>Botão direito nela <b>na lista da direita</b> → <span class=ui>Renomear</span> → escreva <b>Largada</b> → <b>Enter</b>.<br><br>Guarde este nome: no fim da aula o código vai procurar uma peça chamada exatamente <b>Largada</b>.",
    ck="Na lista está escrito <span class=ui>Largada</span> no lugar de SpawnLocation.",
    sos=[("Voltou para SpawnLocation","Você apertou <b>Esc</b>. Termine com <b>Enter</b>."),
         ("Não acho essa linha","Ela fica dentro de <span class=ui>Workspace</span>. Abra a setinha do Workspace."),
         ("Escrevi largada com L minúsculo","Corrija. O código vai procurar <b>Largada</b>, com L maiúsculo.")]),

  dict(n=5, titulo="Crie a lava", img="aula10/s_criar_b.jpg", clipe="02_criar_peca.gif",
    corpo="Clique em <span class=ui>Parte</span> — <b>no desenho, não na palavra embaixo dele</b>.",
    ck="Nasceu um bloco cinza e apareceu <span class=ui>Part</span> na lista.",
    sos=[("Nada aconteceu","Você clicou na palavra. Clique no desenho acima dela."),
         ("Criei duas","Aperte <b>Ctrl + Z</b>.")]),

  dict(n=6, titulo="Deixe a lava comprida e estreita", img="aula10/s_tam_b.jpg", clipe=None,
    corpo="Na busca das <span class=ui>Propriedades</span> escreva <b>size</b>. Duplo clique no valor, <b>Ctrl + A</b>, escreva <b>60, 1, 4</b> e <b>Enter</b>.<br><br>Depois busque <b>position</b> e ponha <b>0, 0.5, -20</b>.<br><br>Comprida para você não dar a volta, e <b>estreita</b> de propósito: 4 passos dá para pular com corrida. É isso que faz a travessia ser um desafio e não uma parede.<br><br>Apague a busca no fim.",
    ck="Ficou uma faixa vermelha... ainda cinza, comprida e fina, atravessando o caminho uns vinte passos à frente da largada.",
    sos=[("Só mudou um número","O campo estava com parte do texto selecionada. Duplo clique no valor, <b>Ctrl + A</b>, e só então escreva."),
         ("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete."),
         ("Não acho a caixa de busca","Fica logo abaixo do título <span class=ui>Propriedades</span>, escrita “Propriedades de filtro”."),
         ("Perdi a peça de vista","Clique no nome dela na lista, leve o mouse para o mundo 3D e aperte <b>F</b>.")]),

  dict(n=7, titulo="Pinte de vermelho", img="aula10/s_cor_e.jpg", clipe="05_cor.gif",
    corpo="Três cliques, nesta ordem:<br><br><b>1.</b> a <b>setinha</b> ao lado do círculo do botão <span class=ui>Cor</span>;<br><b>2.</b> um hexágono <b>vermelho</b>;<br><b>3.</b> o <b>círculo</b> do botão <span class=ui>Cor</span> — é esse que pinta.",
    ck="A faixa ficou vermelha.",
    sos=[("Escolhi e não pintou","Falta o terceiro clique, no círculo do botão <span class=ui>Cor</span>."),
         ("Continua sem pintar","No rodapé do painel de cores há um interruptor “Clique no objeto para aplicar a cor”. Ele fica <b>desligado</b>.")]),

  dict(n=8, titulo="Chame a peça de LAVA", img="aula10/s_nome_b.jpg", clipe="07_renomear.gif",
    corpo="Botão direito em <span class=ui>Part</span> na lista → <span class=ui>Renomear</span> → <b>Lava</b> → <b>Enter</b>.",
    ck="Na lista estão <span class=ui>Largada</span> e <span class=ui>Lava</span>.",
    sos=[("Voltou para Part","Você apertou <b>Esc</b>. Termine com <b>Enter</b>.")]),

  dict(n=9, titulo="Ponha um Script dentro da lava", img="aula10/s_script_c.jpg", clipe="08_inserir_script.gif",
    corpo="Clique em <span class=ui>Lava</span> na lista. Aparece um <b>+</b> depois do nome. Clique no <b>+</b> e escolha <span class=ui>Script</span>.",
    ck="Abriu o editor, e <span class=ui>Script</span> aparece <b>para dentro</b> de Lava na lista.",
    sos=[("O Script ficou fora da Lava","Arraste-o por cima da palavra <span class=ui>Lava</span> na lista."),
         ("Não aparece o +","Clique uma vez na linha da Lava primeiro.")]),

  dict(n=10, titulo="Escreva o código da lava", img="aula10/p_codigo_pronto.jpg", clipe=None,
    codigo=LAVA, auto=(7, 8),
    corpo="Este é o mesmo código da <b>Aula 2</b>. Apague a linha pronta (clique no fim dela e segure <b>Backspace</b>) e escreva:",
    depois="Se você guardou o arquivo da Aula 2, pode abrir e copiar. Mas escrever de novo grava melhor.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Nenhum risco vermelho, e são dois <span class=ui>end</span>, o último com <b>)</b>.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Risco vermelho no fim","Falta o <span class=ui>end)</span> da última linha — com o parêntese."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=11, titulo="Volte para o mundo e teste a travessia", img="aula10/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Clique na aba <span class=ui>Place1</span>, ao lado da aba Script. Depois aperte o <b>▶</b> azul.<br><br>Ande até a faixa vermelha e <b>pule por cima dela com corrida</b>: segure <b>W</b> e aperte a <b>barra de espaço</b> um pouco antes de chegar.<br><br>Depois entre nela de propósito, para ver que mata mesmo.",
    ck="Você conseguiu pular a lava pelo menos uma vez, e morreu ao encostar nela.",
    sos=[("Não consigo pular","Pegue mais impulso: comece a correr de longe e pule <b>antes</b> da borda, não em cima dela."),
         ("Não morro quando encosto","Três conferências: o Script está dentro da <span class=ui>Lava</span>? Sobrou risco vermelho? Você clicou fora do editor antes de jogar?"),
         ("Nasci em cima da lava","Sua lava está em cima da largada. Confira a <b>position</b>: o terceiro número tem de ser <b>-20</b>.")]),

  dict(n=12, titulo="Pare o jogo", img="aula10/s_parar_b.jpg", clipe="11_parar.gif",
    corpo="Aperte o <b>quadrado vermelho</b>.<br><br>Lembre: o que você constrói com o jogo rodando some quando o jogo para.",
    ck="Voltou a tela de montar.",
    sos=[("Sumiu o que eu fiz","Você fez com o jogo rodando. Refaça com o jogo parado.")]),

  dict(n=13, titulo="Crie a bandeira — é um tipo de peça diferente", img="aula10/s_band_c.jpg", clipe="12_inserir_spawn.gif",
    corpo="A bandeira <b>não</b> é uma Parte comum. Ela é uma <span class=ui>SpawnLocation</span>, o mesmo tipo de peça da Largada — é a única peça em que o Roblox sabe fazer alguém nascer.<br><br>Clique em <span class=ui>Workspace</span> na lista, clique no <b>+</b> e, na caixa <span class=ui>Pesquisar objeto</span>, escreva <b>spawn</b>. Clique em <span class=ui>SpawnLocation</span>.",
    ck="Apareceu uma segunda plataforma clara no mundo, e uma linha <span class=ui>SpawnLocation</span> na lista.",
    sos=[("Não acho a caixa de pesquisar","É a primeira linha do menu que abriu, no alto dele."),
         ("Entrou dentro da Lava","Você clicou no <b>+</b> da Lava. Apague com <b>Delete</b> e refaça com o <span class=ui>Workspace</span> selecionado."),
         ("Nasceu em cima da largada","É normal: ela nasce no meio do mundo. O próximo passo move.")]),

  dict(n=14, titulo="Ponha a bandeira do outro lado da lava e pinte de verde", img="aula10/s_bandcor_e.jpg", clipe=None,
    corpo="Na busca das <span class=ui>Propriedades</span> escreva <b>position</b>. Duplo clique no valor, <b>Ctrl + A</b>, escreva <b>0, 0.5, -32</b> e <b>Enter</b>.<br><br>Ela vai para <b>depois</b> da lava — só chega lá quem conseguiu pular.<br><br>Agora pinte de <b>verde</b>, com os mesmos três cliques do botão <span class=ui>Cor</span>. Verde porque é a cor de “você conseguiu”.",
    ck="A segunda plataforma está do outro lado da faixa vermelha, e está verde.",
    sos=[("Ficou em cima da lava","O terceiro número é a distância. Use <b>-32</b>, e confira que a lava está em <b>-20</b>."),
         ("Não consigo pintar","Ela precisa estar selecionada: clique no nome dela na lista antes.")]),

  dict(n=15, titulo="Chame de BANDEIRA", img="aula10/s_bandnome_b.jpg", clipe=None,
    corpo="Botão direito nela na lista → <span class=ui>Renomear</span> → <b>Bandeira</b> → <b>Enter</b>.",
    ck="Na lista estão <span class=ui>Largada</span>, <span class=ui>Lava</span> e <span class=ui>Bandeira</span>.",
    sos=[("Tenho duas SpawnLocation na lista","Uma é a Largada e a outra é a Bandeira. Se as duas ainda se chamam SpawnLocation, renomeie as duas.")]),

  dict(n=16, titulo="Ponha um Script na bandeira e escreva o código", img="aula10/p_cp_pronto.jpg", clipe=None,
    codigo=BANDEIRA, auto=(7, 8),
    corpo="Clique em <span class=ui>Bandeira</span>, clique no <b>+</b>, escolha <span class=ui>Script</span> e apague a linha pronta. Depois escreva:",
    depois="Só uma linha é nova: <span class=ui>jogador.RespawnLocation = bandeira</span>. O resto é o mesmo desenho de sempre — “quando alguém encostar, descubra de quem é o boneco, e se for de um jogador, faça isto”.",
    ck="Nenhum risco vermelho.",
    sos=[("O que é RespawnLocation?","É uma anotação que cada jogador carrega: <i>“quando eu morrer, me ponha aqui”</i>. Enquanto ninguém escreve nela, o Roblox escolhe sozinho."),
         ("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=17, titulo="Ponha um perigo DEPOIS da bandeira", img="aula10/s_dup_b.jpg", clipe=None,
    corpo="Sem alguma coisa que mate <b>depois</b> da bandeira, não dá para ver o checkpoint funcionando.<br><br>Botão direito na <span class=ui>Lava</span> da lista → <span class=ui>Duplicar</span>. A cópia nasce no mesmo lugar e <b>já vem com o script dentro</b>.<br><br>Com a cópia selecionada, busque <b>position</b> nas Propriedades e ponha <b>0, 0.5, -45</b>.",
    ck="Agora há duas faixas vermelhas: uma antes da bandeira verde e outra depois.",
    sos=[("A cópia veio sem script","Você duplicou a peça errada. Apague e duplique a <span class=ui>Lava</span> que tem o Script dentro."),
         ("As duas lavas ficaram no mesmo lugar","Você mudou a position da original. <b>Ctrl + Z</b> e faça de novo, com a <b>cópia</b> selecionada.")]),

  dict(n=18, titulo="Conserte o nascimento sorteado", img="aula10/p_sss_pronto.jpg", clipe=None,
    codigo=LARGADA, auto=(3,),
    corpo="Tem um problema, e é bom você saber dele: <b>o Roblox sorteia</b> em qual plataforma de nascimento o jogador começa. Com a Largada <b>e</b> a Bandeira no mundo, de vez em quando você já começa o jogo do outro lado da lava — o que estraga o obby.<br><br>O conserto é um script curto que manda todo mundo começar na Largada.<br><br>Na lista da direita ache <span class=ui>ServerScriptService</span> (algumas linhas abaixo de Workspace; com o Workspace aberto ele fica <b>fora da vista</b> — role a lista para baixo com a rodinha do mouse, ou feche o Workspace na setinha dele), clique nele, clique no <b>+</b>, escolha <span class=ui>Script</span>, apague a linha pronta e escreva:",
    depois="<span class=ui>PlayerAdded</span> é o mesmo evento da Aula 5: “quando um jogador entrar”. Aqui ele só escreve a anotação inicial — <i>comece na Largada</i>. Depois disso, quem muda a anotação é a bandeira.",
    ck="Nenhum risco vermelho, e o <span class=ui>Script</span> está dentro do <span class=ui>ServerScriptService</span>.",
    sos=[("Diz que Largada não existe","O nome da peça na lista tem de ser exatamente <b>Largada</b>, com L maiúsculo."),
         ("Não acho ServerScriptService","Escreva <b>server</b> na caixa <span class=ui>Pesquisar</span> do alto da lista."),
         ("Pus no lugar errado","Este script <b>não</b> vai numa peça: vai no <span class=ui>ServerScriptService</span>, porque vale para o jogo inteiro."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=19, titulo="Jogue: morra antes e depois da bandeira", img="aula10/s_jogar2_b.jpg", clipe=None,
    corpo="Volte para <span class=ui>Place1</span> e aperte o <b>▶</b>. Faça os dois testes, nesta ordem:<br><br><b>1.</b> Entre na <b>primeira</b> lava de propósito, sem ter tocado na bandeira. Você renasce na <b>largada</b>.<br><b>2.</b> Agora pule a primeira lava, <b>passe por cima da bandeira verde</b> e entre na segunda lava. Você renasce <b>na bandeira</b>.<br><br>É a aula inteira nesses dois testes.",
    ck="Na primeira morte você voltou para o começo; na segunda, depois de pisar na bandeira, você voltou para a bandeira.",
    sos=[("Nas duas vezes volto para o começo","Você não encostou na bandeira. Passe <b>por cima</b> dela, andando — olhar não conta."),
         ("Nas duas vezes volto para a bandeira","Falta o script do passo 18, ou o nome <b>Largada</b> está diferente."),
         ("Renasço e morro na hora","A bandeira está encostando na lava. Afaste: bandeira em <b>-32</b>, lavas em <b>-20</b> e <b>-45</b>.")]),

  dict(n=20, titulo="Salve", img="aula10/s_parar_b.jpg", clipe=None,
    corpo="Pare o jogo. Depois <b>Ctrl + S</b> → <span class=ui>Salvar em arquivo</span> → nome <b>checkpoint</b>.<br><br>Se quiser, publique também: <span class=ui>Arquivo → Publicar na Roblox</span>, como você aprendeu na Aula 4.",
    ck="O pontinho de “não salvo” sumiu do nome da aba.",
    sos=[("Pediu para publicar","Escolha <span class=ui>Salvar em arquivo</span>."),
         ("Quero mais bandeiras","Duplique a <span class=ui>Bandeira</span> — a cópia já vem com o script — e mude a <b>position</b> dela. Ponha uma lava entre cada duas.")]),
 ],
}
