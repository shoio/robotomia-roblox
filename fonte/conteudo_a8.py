# -*- coding: utf-8 -*-
"""Aula 8 — Loja: gaste as moedas."""

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

LOJA = '''local loja = script.Parent
local preco = 3

loja.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tlocal moedas = jogador.leaderstats.Moedas
\t\tif moedas.Value >= preco then
\t\t\tmoedas.Value = moedas.Value - preco
\t\t\tparte.Parent.Humanoid.WalkSpeed = 50
\t\tend
\tend
end)'''

AULA = {
 "n": 8, "slug": "aula8",
 "titulo": "Loja: gaste as moedas",
 "subtitulo": "Três moedas compram velocidade. Se você não tiver as três, não leva — e é o código que decide.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 8 · o código decide",
 "fim": "Acabou a Aula 8. Você escreveu um código que <b>decide</b>: faz uma coisa se tiver dinheiro, e outra se não tiver. Isso se chama condição, e é o que separa um jogo de uma animação.",
 "avisos": [
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Projeto novo", "Começa do zero. A primeira metade refaz o placar e a moeda da Aula 5 — vai rápido, você já sabe."),
   ("O conceito de hoje", "<span class=ui>if … then … else … end</span>: o código olha para um número e escolhe o que fazer."),
   ("Atalhos", "Este material usa <span class=ui>Ctrl</span>, do Windows. Num Mac, troque Ctrl por <span class=ui>⌘</span>."),
 ],
 "passos": [
  dict(n=1, titulo="Abra o Studio e escolha BASEPLATE", img="comum/c01_tela_inicial.jpg", clipe=None,
    corpo="Projeto novo. <b>Role a página para baixo</b> até a fileira <span class=ui>Abrir um modelo</span> e clique no primeiro, o <span class=ui>Baseplate</span>.",
    ck="Abriu o mundo cinza.",
    sos=[("Abriu o projeto antigo","Feche a aba e volte para o Início."),
         ("Apareceu uma janelinha de Boas-vindas por cima","Clique em <span class=ui>Voltar ao início</span>, o botão da esquerda — ou no <b>✕</b> do canto. Não clique em <span class=ui>Iniciar a introdução</span>.")]),

  dict(n=2, titulo="Prepare o editor (uma vez em cada computador)", img="comum/c06_preparar_editor.jpg", clipe=None,
    corpo="Hoje você vai <b>digitar código</b>. O Studio vem com duas ajudas que atrapalham quem está aprendendo: ele sugere linhas inteiras e fecha parênteses e aspas sozinho. Vamos desligar as duas.<br><br>No Windows: <span class=ui>Arquivo → Configurações do Studio</span>. No Mac: <span class=ui>Roblox Studio → Configurações do Studio</span>.<br><br><b>1.</b> Na busca escreva <b>assist</b> e desmarque <span class=ui>Ativar assistente de código</span>.<br><b>2.</b> Apague a busca, escreva <b>fechamento</b> e desmarque <span class=ui>Colchetes de fechamento automáticos</span> e <span class=ui>Aspas de fechamento automáticas</span>.<br><br>Feche a janela. Fica guardado no computador — se você já fez isto numa aula passada <b>neste mesmo computador</b>, é só conferir que as caixinhas continuam vazias.",
    ck="As três caixinhas estão <b>vazias</b>: assistente de código, colchetes e aspas.",
    sos=[("Não acho Configurações do Studio","No Windows é o menu <span class=ui>Arquivo</span>, bem no canto de cima à esquerda da janela."),
         ("A busca não acha nada","Escreva só <b>assist</b>, sem acento e sem mais nada."),
         ("Já está tudo desmarcado","Ótimo — este computador já foi preparado. Feche a janela e siga."),
         ("Por que desligar?","Ligado, o editor escreve linhas que você não pediu, e o <b>Tab</b> aceita a sugestão em vez de recuar. Desligado, o que está escrito na aula é exatamente o que você digita.")]),

  dict(n=3, titulo="Vá para a aba MODELO", img="aula8/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique em <span class=ui>Modelo</span>.",
    ck="Aparecem <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho","Fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=4, titulo="Refaça o placar", img="aula8/s_placar_c.jpg", clipe="02_script_placar.gif",
    corpo="Na lista da direita ache <span class=ui>ServerScriptService</span> (algumas linhas abaixo de <span class=ui>Workspace</span>; role a lista se não estiver à vista), clique nele, clique no <b>+</b> e escolha <span class=ui>Script</span>.",
    ck="Abriu o editor e o <span class=ui>Script</span> está dentro do <span class=ui>ServerScriptService</span>.",
    sos=[("Não acho ServerScriptService","Escreva <b>server</b> na caixa <span class=ui>Pesquisar</span> do Explorador."),
         ("Esqueci como era","Está tudo na Aula 5, passos 4 e 5.")]),

  dict(n=5, titulo="Escreva o placar", img="aula8/p_placar_pronto.jpg", clipe=None,
    codigo=PLACAR, auto=(10,),
    corpo="O mesmo código da Aula 5. Apague a linha pronta (clique no fim dela e segure <b>Backspace</b>) e escreva:",
    depois="Se você guardou o arquivo da Aula 5, pode abrir lá e copiar. Mas escrever de novo grava melhor.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Nenhum risco vermelho.",
    sos=[
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço."),
         ("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Leaderstats não funciona","É <b>leaderstats</b>, tudo minúsculo, entre aspas."),
         ("Risco vermelho no fim","Falta o <span class=ui>end)</span>."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=6, titulo="Crie a moeda", img="aula8/s_moeda_b.jpg", clipe="03_criar_moeda.gif",
    corpo="Volte para a aba <span class=ui>Place1</span>. Clique no <b>desenho</b> do <span class=ui>Parte</span>, depois leve a câmera até ela (<b>F</b>, depois <b>S</b>).",
    ck="Nasceu um bloco no meio da tela.",
    sos=[("Nada aconteceu","Você clicou na palavra, não no desenho.")]),

  dict(n=7, titulo="Ancore e posicione", img="aula8/s_anc_moeda_b.jpg", clipe="04_ancorar.gif",
    corpo="Clique em <span class=ui>Âncora</span>.<br><br>Depois, na busca das <span class=ui>Propriedades</span>, escreva <b>position</b>. Duplo clique no valor, <b>Ctrl + A</b>, escreva <b>0, 3, -6</b> e <b>Enter</b> — a moeda fica logo à frente de onde você nasce. Depois apague a busca.",
    ck="A moeda flutua um pouco à frente da plataforma de nascimento.",
    sos=[("Aparecem três linhas Position","Use a primeira, embaixo de <span class=ui>CFrame</span>."),
         ("A moeda ficou no chão","O número do meio é a altura. Use <b>3</b>.")]),

  dict(n=8, titulo="Pinte de amarelo e chame de MOEDA", img="aula8/s_nome_moeda_b.jpg", clipe="05_cor_moeda.gif",
    corpo="Setinha do <span class=ui>Cor</span> → amarelo → clique no <b>círculo do botão Cor</b>.<br><br>Depois botão direito na peça → <span class=ui>Renomear</span> → <b>Moeda</b> → Enter.",
    ck="Uma peça amarela chamada <span class=ui>Moeda</span> na lista.",
    sos=[("Não pintou","Falta o clique no círculo do botão Cor.")]),

  dict(n=9, titulo="Ponha o script na moeda", img="aula8/p_moeda_pronto.jpg", clipe="07_script_moeda.gif",
    codigo=MOEDA, auto=(8, 9),
    corpo="Clique em <span class=ui>Moeda</span>, clique no <b>+</b>, escolha <span class=ui>Script</span>, apague a linha pronta e escreva:",
    depois="Também é o mesmo da Aula 5. Cada moeda vale um ponto e se apaga depois.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Nenhum risco vermelho.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("GetPlayerFromCharacter dá erro","Confira as maiúsculas: G, P, F, C."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=10, titulo="Faça três moedas", img="aula8/p_cena.jpg", clipe=None,
    corpo="Botão direito na <span class=ui>Moeda</span> → <span class=ui>Duplicar</span>, duas vezes.<br><br>Mude a <b>position</b> das cópias para <b>3, 3, -6</b> e <b>-3, 3, -6</b>, para ficarem lado a lado.<br><br>Você vai precisar de três moedas para comprar na loja.",
    ck="Três moedas amarelas em fila, e três <span class=ui>Moeda</span> na lista.",
    sos=[("As cópias ficaram uma dentro da outra","Mude a position de cada uma. O primeiro número é para os lados."),
         ("A cópia não soma ponto","Você duplicou antes de pôr o script. Apague e duplique a que tem o Script dentro.")]),

  dict(n=11, titulo="Crie a loja", img="aula8/s_loja_b.jpg", clipe="08_criar_loja.gif",
    corpo="Mais uma peça: <span class=ui>Parte</span> → <span class=ui>Âncora</span>.<br><br>Depois <b>size</b> = <b>6, 1, 6</b> e <b>position</b> = <b>10, 0.5, -6</b>. Fica uma plataforma quadrada, do lado.",
    ck="Tem uma plataforma baixa ao lado das moedas.",
    sos=[("Ficou em cima das moedas","O primeiro número do position é para os lados. Use <b>10</b>."),
         ("Esqueci de ancorar","Clique nela e em <span class=ui>Âncora</span>.")]),

  dict(n=12, titulo="Pinte de verde e chame de LOJA", img="aula8/s_nome_loja_b.jpg", clipe="09_cor_loja.gif",
    corpo="Setinha do <span class=ui>Cor</span> → verde → círculo do botão Cor.<br><br>Botão direito → <span class=ui>Renomear</span> → <b>Loja</b> → Enter.",
    ck="Uma plataforma verde chamada <span class=ui>Loja</span>.",
    sos=[("Pintei a peça errada","<b>Ctrl + Z</b> e repita na certa.")]),

  dict(n=13, titulo="Ponha o script na loja", img="aula8/p_editor_loja.jpg", clipe=None,
    corpo="Clique em <span class=ui>Loja</span>, clique no <b>+</b> e escolha <span class=ui>Script</span>. Apague a linha pronta (fim da linha + <b>Backspace</b>).<br><br>Este é o código importante da aula. Vem no próximo passo.",
    ck="O editor abriu vazio, com o <span class=ui>Script</span> dentro da <span class=ui>Loja</span>.",
    sos=[("Ficou fora da Loja","Arraste-o por cima da palavra <span class=ui>Loja</span> na lista.")]),

  dict(n=14, titulo="Escreva a loja", img="aula8/p_loja_pronto.jpg", clipe=None,
    codigo=LOJA, auto=(11, 12, 13),
    corpo="Treze linhas. Repare que existe um <span class=ui>if</span> <b>dentro</b> do outro:",
    depois="O primeiro <span class=ui>if</span> pergunta “é um jogador?”. O segundo pergunta “ele tem dinheiro?”. São <b>três</b> <span class=ui>end</span> no fim, e o último com <span class=ui>)</span>.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Nenhum risco vermelho, e o editor desenhou as linhas verticais dos dois <span class=ui>if</span>.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Risco vermelho no fim","Conte os <span class=ui>end</span>: são três, e o último é <span class=ui>end)</span>."),
         ("A indentação saiu diferente","O editor recua sozinho. Não use Tab — ele serve para outra coisa. Se ficou torto, apague a linha e escreva de novo."),
         ("O que é >= ?","É “maior ou igual”. Dois símbolos, sem espaço entre eles."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=15, titulo="Entenda a decisão", img="aula8/p_loja_pronto.jpg", clipe=None,
    corpo="<b>local preco = 3</b> — guarda o número 3 com o nome <span class=ui>preco</span>. Assim, se você quiser mudar o preço, muda num lugar só.<br><br><b>if moedas.Value >= preco then</b> — “se o que ele tem for <b>maior ou igual</b> ao preço…”. É aqui que o código decide.<br><br><b>moedas.Value = moedas.Value - preco</b> — cobra: tira 3 do que ele tinha.<br><br><b>Humanoid.WalkSpeed = 50</b> — entrega o produto. A velocidade normal é 16; 50 é correr muito.<br><br>E se não tiver as três moedas? <b>Nada acontece.</b> O código simplesmente pula tudo que está dentro do <span class=ui>if</span>.",
    ck="Você consegue dizer o que acontece ao pisar na loja com 2 moedas.",
    sos=[("Por que usar preco em vez de 3 direto?","Porque aparece duas vezes. Com um nome só, você muda o preço num lugar e vale nos dois.")]),

  dict(n=16, titulo="Jogue: tente comprar sem dinheiro", img="aula8/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Volte para <span class=ui>Place1</span> e aperte o <b>▶</b>.<br><br>Vá <b>direto</b> para a plataforma verde, sem pegar moeda nenhuma. Pise nela.",
    ck="Nada acontece. Você continua na mesma velocidade e o placar continua em 0.",
    sos=[("Ficou rápido mesmo sem moeda","O <span class=ui>>=</span> está errado, ou o preço está 0. Confira a linha do <span class=ui>if</span>."),
         ("Deu erro vermelho na tela","Provavelmente o placar. Confira o <span class=ui>leaderstats</span> no script do ServerScriptService.")]),

  dict(n=17, titulo="Agora pegue as três moedas", img="aula8/s_jogar_c.jpg", clipe=None,
    corpo="Pegue as três moedas — o placar vai para 3 — e volte para a plataforma verde.",
    ck="O placar caiu de 3 para 0 <b>e</b> o seu boneco ficou visivelmente mais rápido.",
    sos=[("O placar zerou mas não fiquei rápido","Confira a linha do <span class=ui>WalkSpeed</span>: é <b>parte.Parent.Humanoid.WalkSpeed</b>."),
         ("Fiquei rápido mas o placar não mudou","Faltou a linha que subtrai o preço."),
         ("Peguei só duas moedas e funcionou","O preço no código não é 3. Confira a linha 2.")]),

  dict(n=18, titulo="Mude o preço", img="aula8/p_loja_pronto.jpg", clipe=None,
    corpo="Pare o jogo. Troque <span class=ui>local preco = 3</span> por <span class=ui>local preco = 1</span> e jogue de novo.<br><br>Uma moeda já compra. Depois experimente <b>10</b> — aí não dá para comprar com as três moedas que existem.",
    ck="Você viu o mesmo código se comportar de dois jeitos, só mudando um número.",
    sos=[("Mudei e nada","Você mudou com o jogo rodando. Pare, mude, jogue.")]),

  dict(n=19, titulo="Venda outra coisa", img="aula8/p_cena.jpg", clipe=None,
    corpo="Troque a linha do <span class=ui>WalkSpeed</span> por uma destas:<br><br><span class=ui>parte.Parent.Humanoid.JumpHeight = 25</span> — pulo alto<br><span class=ui>parte.Parent.Humanoid.MaxHealth = 200</span> — mais vida<br><br>Se escolher a vida, escreva também <span class=ui>parte.Parent.Humanoid.Health = 200</span> na linha de baixo: só o <span class=ui>MaxHealth</span> aumenta a barra, mas deixa o resto dela vazio.<br><br>Ou duplique a Loja, mude o nome e o preço, e faça <b>duas</b> lojas com produtos diferentes.",
    ck="A sua loja vende alguma coisa que não é velocidade.",
    sos=[("JumpHeight não funciona","Escreva com J e H maiúsculos, exatamente assim."),
         ("As duas lojas fazem a mesma coisa","Você duplicou e não mudou o script da cópia.")]),

  dict(n=20, titulo="Salve", img="aula8/s_parar_b.jpg", clipe=None,
    corpo="<b>Ctrl + S</b> → <b>Salvar em arquivo</b> → nome <b>loja</b>.<br><br>E publique, se quiser: <span class=ui>Arquivo → Publicar na Roblox</span>.",
    ck="Salvou sem erro.",
    sos=[("Esqueci como publica","Aula 4, passo 9.")]),
 ],
}
