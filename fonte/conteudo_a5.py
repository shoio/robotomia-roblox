# -*- coding: utf-8 -*-
"""Aula 5 — Moedas e placar."""

PLACAR = '''game.Players.PlayerAdded:Connect(function(jogador)
\tlocal pasta = Instance.new("Folder")
\tpasta.Name = "leaderstats"
\tpasta.Parent = jogador

\tlocal moedas = Instance.new("IntValue")
\tmoedas.Name = "Moedas"
\tmoedas.Value = 0
\tmoedas.Parent = pasta
end)'''

MOEDA = '''local moeda = script.Parent

moeda.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tjogador.leaderstats.Moedas.Value = jogador.leaderstats.Moedas.Value + 1
\t\tmoeda:Destroy()
\tend
end)'''

AULA = {
 "n": 5, "slug": "aula5",
 "titulo": "Moedas e placar",
 "subtitulo": "Um número na tela que sobe quando você encosta na moeda — e a moeda some.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 5 · dois scripts",
 "fim": "Acabou a Aula 5. Você fez dois scripts conversarem: um cria o placar, o outro soma nele. É assim que todo jogo com pontuação funciona.",
 "avisos": [
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Projeto novo", "Começa do zero. Hoje são <b>dois</b> scripts, em lugares diferentes."),
   ("A palavra mais importante", "<span class=ui>leaderstats</span>, tudo junto e tudo minúsculo. É esse nome exato que faz o placar aparecer. Com uma letra diferente, nada acontece."),
   ("Atalhos", "Este material usa <span class=ui>Ctrl</span>, do Windows. Num Mac, troque Ctrl por <span class=ui>⌘</span>."),
 ],
 "passos": [
  dict(n=1, titulo="Abra o Studio e escolha BASEPLATE", img="comum/c01_tela_inicial.jpg", clipe=None,
    corpo="Projeto novo, como sempre. <b>Role a página para baixo</b> até <span class=ui>Abrir um modelo</span> e clique no <span class=ui>Baseplate</span>.",
    ck="Abriu o mundo cinza com a plataforma clara.",
    sos=[("Abriu o projeto antigo","Feche a aba e volte para o Início."),
         ("Apareceu uma janelinha de Boas-vindas por cima","Clique em <span class=ui>Voltar ao início</span>, o botão da esquerda — ou no <b>✕</b> do canto. Não clique em <span class=ui>Iniciar a introdução</span>.")]),

  dict(n=2, titulo="Prepare o editor (uma vez em cada computador)", img="comum/c06_preparar_editor.jpg", clipe=None,
    corpo="Hoje você vai <b>digitar código</b>. O Studio vem com duas ajudas que atrapalham quem está aprendendo: ele sugere linhas inteiras e fecha parênteses e aspas sozinho. Vamos desligar as duas.<br><br>No Windows: <span class=ui>Arquivo → Configurações do Studio</span>. No Mac: <span class=ui>Roblox Studio → Configurações do Studio</span>.<br><br><b>1.</b> Na busca escreva <b>assist</b> e desmarque <span class=ui>Ativar assistente de código</span>.<br><b>2.</b> Apague a busca, escreva <b>fechamento</b> e desmarque <span class=ui>Colchetes de fechamento automáticos</span> e <span class=ui>Aspas de fechamento automáticas</span>.<br><br>Feche a janela. Fica guardado no computador — se você já fez isto numa aula passada <b>neste mesmo computador</b>, é só conferir que as caixinhas continuam vazias.",
    ck="As três caixinhas estão <b>vazias</b>: assistente de código, colchetes e aspas.",
    sos=[("Não acho Configurações do Studio","No Windows é o menu <span class=ui>Arquivo</span>, bem no canto de cima à esquerda da janela."),
         ("A busca não acha nada","Escreva só <b>assist</b>, sem acento e sem mais nada."),
         ("Já está tudo desmarcado","Ótimo — este computador já foi preparado. Feche a janela e siga."),
         ("Por que desligar?","Ligado, o editor escreve linhas que você não pediu, e o <b>Tab</b> aceita a sugestão em vez de recuar. Desligado, o que está escrito na aula é exatamente o que você digita.")]),

  dict(n=3, titulo="Vá para a aba MODELO", img="aula5/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique em <span class=ui>Modelo</span>.",
    ck="Aparecem <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho","Fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=4, titulo="Ache o ServerScriptService na lista", img="aula5/s_placar_a.jpg", clipe=None,
    corpo="Na lista da direita, procure <span class=ui>ServerScriptService</span>. Num projeto novo ele costuma já estar à vista, algumas linhas <b>abaixo</b> de <span class=ui>Workspace</span> — se não estiver, role a lista para baixo com a rodinha do mouse.<br><br>É uma caixa onde ficam scripts que valem para o <b>jogo inteiro</b> — não para uma peça só. O placar é assim: é do jogo, não de um bloco.",
    ck="Você está vendo a linha <span class=ui>ServerScriptService</span> na lista.",
    sos=[("Não consigo rolar a lista","Use a rodinha do mouse em cima da lista, ou escreva <b>server</b> na caixa <span class=ui>Pesquisar</span> no alto dela."),
         ("Tem vários nomes parecidos","Você quer o <b>ServerScriptService</b>, não o ServerStorage.")]),

  dict(n=5, titulo="Coloque um Script nele", img="aula5/s_placar_c.jpg", clipe="02_script_placar.gif",
    corpo="Clique uma vez em <span class=ui>ServerScriptService</span>. Aparece um <b>+</b> depois do nome. Clique no <b>+</b> e escolha <span class=ui>Script</span>.",
    ck="Abriu o editor, e o <span class=ui>Script</span> aparece para dentro do <span class=ui>ServerScriptService</span>.",
    sos=[("Não aparece o +","Clique uma vez na linha primeiro."),
         ("O Script foi para outro lugar","Apague com <b>Delete</b> e refaça com o ServerScriptService selecionado.")]),

  dict(n=6, titulo="Apague a linha pronta", img="aula5/p_editor_nasce.jpg", clipe=None,
    corpo="Como sempre, o script nasce com <span class=ui>print(\"Hello world!\")</span>. Apague a linha inteira: clique no fim dela e segure <b>Backspace</b> até a linha 1 ficar vazia.",
    ck="A linha 1 está vazia.",
    sos=[("Sumiu a tela do script","Duplo clique no <span class=ui>Script</span> na lista.")]),

  dict(n=7, titulo="Escreva o placar", img="aula5/p_placar_pronto.jpg", clipe=None,
    codigo=PLACAR, auto=(10,),
    corpo="Este é o código que cria o placar. Nove linhas:",
    depois="Cuidado com três coisas: <span class=ui>leaderstats</span> é tudo minúsculo e entre aspas; <span class=ui>IntValue</span> tem I e V maiúsculos; e o <span class=ui>Moedas</span> entre aspas é o nome que vai aparecer na tela.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Nenhum risco vermelho.",
    sos=[
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço."),
         ("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Risco vermelho no fim","Falta o <span class=ui>end)</span> da última linha — com o parêntese."),
         ("Escrevi Leaderstats com L maiúsculo","Não funciona. Tem que ser <b>leaderstats</b>, tudo minúsculo. É a Roblox que exige esse nome exato."),
         ("O editor completa sozinho","Aperte <b>Esc</b> para dispensar a sugestão."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=8, titulo="Entenda o placar", img="aula5/p_placar_pronto.jpg", clipe=None,
    corpo="<b>game.Players.PlayerAdded</b> — “quando um jogador entrar no jogo”.<br><br><b>Instance.new(\"Folder\")</b> — cria uma pasta nova, do nada. <span class=ui>Instance.new</span> é como o código fabrica coisas.<br><br><b>pasta.Name = \"leaderstats\"</b> — a pasta ganha esse nome. <b>É esse nome que a Roblox procura</b> para desenhar o placar na tela. Qualquer outro nome e não aparece nada.<br><br><b>Instance.new(\"IntValue\")</b> — cria um número. <i>Int</i> é número inteiro: 0, 1, 2. Sem vírgula.<br><br><b>moedas.Parent = pasta</b> — põe o número dentro da pasta. É a pasta dentro do jogador, e o número dentro da pasta.",
    ck="Você consegue explicar por que a pasta tem que se chamar leaderstats.",
    sos=[("O que é Parent de novo?","É “quem está segurando”. Aqui você está dizendo onde cada coisa nova vai morar.")]),

  dict(n=9, titulo="Volte para o mundo e jogue", img="aula5/s_jogo1_b.jpg", clipe="04_jogar_placar.gif",
    corpo="Clique na aba <span class=ui>Place1</span> e depois no <b>▶</b>.<br><br>Olhe o canto superior direito da tela do jogo.",
    ck="Apareceu um quadro escrito <b>Pessoas</b> e <b>Moedas</b>, com o seu nome e um <b>0</b>.",
    sos=[("Não apareceu o placar","Quase sempre é o nome: confira se está <b>leaderstats</b>, tudo minúsculo, entre aspas."),
         ("Apareceu só o nome, sem coluna","Faltou a parte do <span class=ui>IntValue</span>. Confira as quatro últimas linhas."),
         ("O quadro some","Clique no <b>x</b> dele sem querer fecha. Saia e entre no jogo de novo.")]),

  dict(n=10, titulo="Pare o jogo", img="aula5/s_jogo1_c.jpg", clipe=None,
    corpo="Quadrado vermelho. Agora vamos fazer a moeda.",
    ck="Voltou a tela de montar.",
    sos=[("Continuo no jogo","Aperte o quadrado, não o ▶.")]),

  dict(n=11, titulo="Crie a moeda", img="aula5/s_moeda_b.jpg", clipe="05_criar_moeda.gif",
    corpo="Clique no <b>desenho</b> do botão <span class=ui>Parte</span>.",
    ck="Nasceu um bloco e apareceu <span class=ui>Part</span> na lista.",
    sos=[("Nada aconteceu","Você clicou na palavra, não no desenho.")]),

  dict(n=12, titulo="Leve a câmera e ancore", img="aula5/s_anc_moeda_b.jpg", clipe="06_ancorar.gif",
    corpo="Clique em <span class=ui>Part</span> na lista, mouse no mundo 3D, tecla <b>F</b>, depois <b>S</b> algumas vezes.<br><br>Com a peça selecionada, clique em <span class=ui>Âncora</span>. Moeda que cai não serve.",
    ck="A peça está no meio da tela e o botão <span class=ui>Âncora</span> está aceso.",
    sos=[("F não fez nada","O mouse tem que estar sobre o mundo 3D.")]),

  dict(n=13, titulo="Pinte de amarelo", img="aula5/s_cor_e.jpg", clipe="07_cor.gif",
    corpo="Setinha do <span class=ui>Cor</span> → hexágono amarelo → clique no <b>círculo do botão Cor</b>.",
    ck="A peça ficou amarela.",
    sos=[("Não pintou","Falta o clique no círculo do botão Cor.")]),

  dict(n=14, titulo="Chame de MOEDA", img="aula5/s_nome_b.jpg", clipe="08_renomear.gif",
    corpo="Botão direito na peça, na lista → <span class=ui>Renomear</span> → <b>Moeda</b> → Enter.",
    ck="Na lista está <span class=ui>Moeda</span>.",
    sos=[("Voltou o nome antigo","Termine com <b>Enter</b>.")]),

  dict(n=15, titulo="Ponha um Script dentro da Moeda", img="aula5/s_scriptmoeda_c.jpg", clipe="09_script_moeda.gif",
    corpo="Clique em <span class=ui>Moeda</span> na lista, clique no <b>+</b> e escolha <span class=ui>Script</span>.<br><br>Repare: este script é <b>da peça</b>. O outro era do jogo inteiro. São coisas diferentes.",
    ck="O <span class=ui>Script</span> aparece para dentro de <span class=ui>Moeda</span>, e o editor abriu.",
    sos=[("Ficou fora da Moeda","Arraste-o por cima da palavra <span class=ui>Moeda</span> na lista."),
         ("Abriu o script errado","Feche as abas de script lá em cima e dê duplo clique no Script que está dentro da Moeda.")]),

  dict(n=16, titulo="Escreva o código da moeda", img="aula5/p_moeda_pronto.jpg", clipe=None,
    codigo=MOEDA, auto=(8, 9),
    corpo="Apague a linha pronta (clique no fim dela e segure <b>Backspace</b>) e escreva:",
    depois="<b>GetPlayerFromCharacter</b> é uma palavra só, com quatro maiúsculas. Copie com calma.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Nenhum risco vermelho, e são dois <span class=ui>end</span>, o último com <span class=ui>)</span>.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Risco vermelho em GetPlayerFromCharacter","Confira as maiúsculas: G, P, F, C."),
         ("Risco no fim","Falta um <span class=ui>end</span> ou o parêntese final."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=17, titulo="Entenda a moeda", img="aula5/p_moeda_pronto.jpg", clipe=None,
    corpo="<b>GetPlayerFromCharacter(parte.Parent)</b> — “descubra <b>qual jogador</b> é esse boneco”. Na aula da lava a gente só perguntava se era um boneco; agora precisamos saber <b>de quem</b> é, para somar no placar certo.<br><br><b>jogador.leaderstats.Moedas.Value + 1</b> — pega o número que está lá e põe um a mais. Repare no caminho: jogador → pasta → número → valor.<br><br><b>moeda:Destroy()</b> — a moeda se apaga. Por isso você não pega a mesma moeda duas vezes.",
    ck="Você sabe dizer o que aconteceria sem a linha do <span class=ui>Destroy</span>.",
    sos=[("O que aconteceria sem o Destroy?","A moeda ficaria lá e o número subiria sem parar enquanto você encostasse.")]),

  dict(n=18, titulo="Jogue e pegue a moeda", img="aula5/p_moeda_pega.jpg", clipe="10_jogar_moeda.gif",
    corpo="Volte para <span class=ui>Place1</span> e aperte o <b>▶</b>.<br><br>Ande até a moeda amarela e encoste nela.",
    ck="A moeda sumiu <b>e</b> o número do placar virou <b>1</b>.",
    sos=[("A moeda some mas o número não muda","O placar não existe. Volte ao passo 7 e confira o <span class=ui>leaderstats</span>."),
         ("O número muda mas a moeda fica","Faltou o <span class=ui>moeda:Destroy()</span>."),
         ("Não acontece nada","Confira se o Script está <b>dentro</b> da Moeda, e se não sobrou risco vermelho.")]),

  dict(n=19, titulo="Faça um monte de moedas", img="aula5/s_jogo2_d.jpg", clipe=None,
    corpo="Com o jogo <b>parado</b>: botão direito na <span class=ui>Moeda</span> → <span class=ui>Duplicar</span>. Depois use a ferramenta <span class=ui>Mover</span> (segundo botão da faixa, o das setas) e arraste a cópia <b>pela seta</b>.<br><br>Faça cinco ou seis, espalhadas. Cada cópia já vem com o script dentro e vale um ponto.",
    ck="Você pegou várias moedas em sequência e o número foi somando: 1, 2, 3…",
    sos=[("A cópia não soma","Você duplicou antes de pôr o script. Apague e duplique a Moeda que <b>tem</b> o Script dentro."),
         ("As moedas ficaram no mesmo lugar","A cópia nasce em cima da original. Arraste-a pela seta.")]),

  dict(n=20, titulo="Salve", img="aula5/s_jogo2_d.jpg", clipe=None,
    corpo="<b>Ctrl + S</b> → <b>Salvar em arquivo</b> → nome <b>moedas</b>.<br><br>Se quiser, publique também: <span class=ui>Arquivo → Publicar na Roblox</span>, como você aprendeu na aula passada.",
    ck="Salvou sem erro.",
    sos=[("Quero publicar mas esqueci como","Volte na Aula 4, passo 9.")]),
 ],
}
