# -*- coding: utf-8 -*-
"""Aula 9 — Projeto livre e mostra."""

LAVA = '''local lava = script.Parent

lava.Touched:Connect(function(parte)
\tlocal humano = parte.Parent:FindFirstChild("Humanoid")
\tif humano then
\t\thumano.Health = 0
\tend
end)'''

SUME = '''local piso = script.Parent

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

PORTA = '''local botao = script.Parent
local porta = workspace.Porta

botao.Touched:Connect(function(parte)
\tlocal humano = parte.Parent:FindFirstChild("Humanoid")
\tif humano then
\t\tporta.Transparency = 1
\t\tporta.CanCollide = false
\t\ttask.wait(3)
\t\tporta.Transparency = 0
\t\tporta.CanCollide = true
\tend
end)'''

MARTELO = '''local martelo = script.Parent

while true do
\tmartelo.CFrame = martelo.CFrame * CFrame.Angles(0, 0.05, 0)
\ttask.wait(0.03)
end'''

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
 "n": 9, "slug": "aula9",
 "titulo": "Projeto livre e mostra",
 "subtitulo": "Hoje o jogo é seu. Nesta página estão todas as receitas do curso — escolha as que quiser e monte o que você imaginou.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 9 · o jogo é seu",
 "fim": "Acabou o curso. Você sabe construir, fazer o Roblox reagir ao jogador, contar pontos, criar obstáculos que se mexem, fazer o código decidir — e publicar tudo isso num link. O resto é ideia sua.",
 "avisos": [
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Hoje não tem passo a passo", "As outras aulas mandavam. Esta te dá as peças e você escolhe. Se travar, o quadro laranja de cada receita continua valendo."),
   ("Guarde tempo para a mostra", "Os últimos 15 minutos são para jogar o jogo dos colegas. Não deixe para publicar no fim."),
   ("Copie do seu próprio caderno", "Todas as receitas abaixo vieram das aulas 2 a 8. Se você guardou os arquivos, pode abrir e copiar de lá."),
 ],
 "passos": [
  dict(n=1, titulo="Abra o Studio e escolha BASEPLATE", img="comum/c01_tela_inicial.jpg", clipe=None,
    corpo="Projeto novo. <b>Role a página para baixo</b> até a fileira <span class=ui>Abrir um modelo</span> e clique no primeiro, o <span class=ui>Baseplate</span>.",
    ck="Abriu o mundo cinza.",
    sos=[("Quero continuar um jogo antigo","Pode: <span class=ui>Arquivo → Abrir do arquivo</span> e escolha o que você salvou."),
         ("Apareceu uma janelinha de Boas-vindas por cima","Clique em <span class=ui>Voltar ao início</span>, o botão da esquerda — ou no <b>✕</b> do canto. Não clique em <span class=ui>Iniciar a introdução</span>.")]),

  dict(n=2, titulo="Prepare o editor (uma vez em cada computador)", img="comum/c06_preparar_editor.jpg", clipe=None,
    corpo="Hoje você vai <b>digitar código</b>. O Studio vem com duas ajudas que atrapalham quem está aprendendo: ele sugere linhas inteiras e fecha parênteses e aspas sozinho. Vamos desligar as duas.<br><br>No Windows: <span class=ui>Arquivo → Configurações do Studio</span>. No Mac: <span class=ui>Roblox Studio → Configurações do Studio</span>.<br><br><b>1.</b> Na busca escreva <b>assist</b> e desmarque <span class=ui>Ativar assistente de código</span>.<br><b>2.</b> Apague a busca, escreva <b>fechamento</b> e desmarque <span class=ui>Colchetes de fechamento automáticos</span> e <span class=ui>Aspas de fechamento automáticas</span>.<br><br>Feche a janela. Fica guardado no computador — se você já fez isto numa aula passada <b>neste mesmo computador</b>, é só conferir que as caixinhas continuam vazias.",
    ck="As três caixinhas estão <b>vazias</b>: assistente de código, colchetes e aspas.",
    sos=[("Não acho Configurações do Studio","No Windows é o menu <span class=ui>Arquivo</span>, bem no canto de cima à esquerda da janela."),
         ("A busca não acha nada","Escreva só <b>assist</b>, sem acento e sem mais nada."),
         ("Já está tudo desmarcado","Ótimo — este computador já foi preparado. Feche a janela e siga."),
         ("Por que desligar?","Ligado, o editor escreve linhas que você não pediu, e o <b>Tab</b> aceita a sugestão em vez de recuar. Desligado, o que está escrito na aula é exatamente o que você digita.")]),

  dict(n=3, titulo="Decida o que você vai fazer", img="aula9/p_exemplo.jpg", clipe=None,
    corpo="Cinco minutos, no máximo. Escolha <b>uma</b> destas três formas, ou invente:<br><br><b>Percurso</b> — do começo ao fim sem cair. Lava, plataformas que somem, martelos.<br><br><b>Caça ao tesouro</b> — espalhe moedas pelo mapa e conte quem pega mais.<br><br><b>Sala de desafios</b> — portas com botão, cada uma abre a próxima.<br><br>Escreva numa folha em três linhas: <i>o que o jogador faz</i>, <i>o que atrapalha</i>, <i>como ele ganha</i>.",
    ck="Você tem as três linhas escritas no papel.",
    sos=[("Não consigo escolher","Comece pelo percurso. É o mais rápido de montar e o mais fácil de testar."),
         ("Quero fazer tudo","Escolha dois obstáculos, não seis. Jogo pequeno e terminado vale mais que grande e pela metade.")]),

  dict(n=4, titulo="Monte o cenário primeiro, sem código", img="aula9/s_tam_lava_b.jpg", clipe="04_tamanho.gif",
    corpo="Antes de mais nada, duas coisas que toda aula começa fazendo:<br><br><b>1.</b> Na lista da direita, clique na <b>setinha</b> à esquerda de <span class=ui>Workspace</span> para abrir.<br><b>2.</b> Na linha de cima, clique na aba <span class=ui>Modelo</span> — é só nela que existem <span class=ui>Parte</span>, <span class=ui>Material</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.<br><br>Agora quinze minutos só de blocos: crie, ancore, mude o <b>size</b> e a <b>position</b>, pinte.<br><br><b>Não ponha script nenhum agora.</b> Monte o caminho todo primeiro, ande por ele no jogo, veja se dá para atravessar. Depois é que vêm as armadilhas.",
    ck="Você consegue atravessar o seu mapa do começo ao fim andando.",
    sos=[("Não acho o botão Parte","Você está na aba errada. Clique em <span class=ui>Modelo</span>, entre <span class=ui>Script</span> e <span class=ui>Plugins</span>."),
         ("Minhas peças caem","Faltou <span class=ui>Âncora</span>. Criou, ancorou."),
         ("Não consigo pular de uma para outra","Estão longe demais. O boneco pula uns 7 passos de altura e uns 10 de distância."),
         ("Perdi uma peça de vista","Clique no nome dela na lista e aperte <b>F</b>.")]),

  dict(n=5, titulo="RECEITA: a peça que mata", img="aula9/s_cor_lava_e.jpg", clipe="05_cor.gif",
    codigo=LAVA, auto=(7, 8),
    corpo="Vermelha, material <span class=ui>Neon</span>, com este <span class=ui>Script</span> dentro:",
    depois="Da Aula 2. Serve para lava, espinho, água venenosa — qualquer coisa que não se pode encostar.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Você morre ao encostar nela.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Não morro","O Script está <b>dentro</b> da peça? Sobrou risco vermelho?"),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço.")]),

  dict(n=6, titulo="RECEITA: a plataforma que some", img="aula9/s_anc_lava_b.jpg", clipe=None,
    codigo=SUME, auto=(11, 12),
    corpo="Uma peça normal com este <span class=ui>Script</span> dentro:",
    depois="Da Aula 3. Mude o <span class=ui>task.wait(2)</span> para deixar mais fácil ou mais difícil.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Você pisa, ela some, você cai, ela volta.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Fica transparente mas não caio","Faltou a linha do <span class=ui>CanCollide</span>."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço.")]),

  dict(n=7, titulo="RECEITA: o placar", img="aula9/s_placar_c.jpg", clipe=None,
    codigo=PLACAR, auto=(10,),
    corpo="Este vai no <span class=ui>ServerScriptService</span>, <b>não</b> numa peça:",
    depois="Da Aula 5. Sem ele, nenhuma moeda funciona.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Aparece o quadro com <b>Moedas</b> no canto da tela do jogo.",
    sos=[
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço."),
         ("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Não aparece","É <b>leaderstats</b>, tudo minúsculo."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=8, titulo="RECEITA: a moeda", img="aula9/s_cor_moeda_e.jpg", clipe=None,
    codigo=MOEDA, auto=(8, 9),
    corpo="Peça amarela com este <span class=ui>Script</span> dentro. <b>Precisa do placar do passo 7.</b>",
    depois="Da Aula 5. Faça uma, ponha o script, e só então duplique — a cópia já vem com o script.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="A moeda some e o número sobe.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("O número não muda","Falta o placar."),
         ("As cópias não somam","Você duplicou antes de pôr o script."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=9, titulo="RECEITA: botão e porta", img="aula9/p_exemplo.jpg", clipe=None,
    codigo=PORTA, auto=(12, 13),
    corpo="Duas peças: uma chamada exatamente <b>Porta</b>, e outra com este <span class=ui>Script</span> dentro.",
    depois="Da Aula 6. O script vai no <b>botão</b>, não na porta.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Pisar no botão faz a porta sumir por três segundos.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Diz que Porta não existe","O nome da peça tem que ser exatamente <b>Porta</b>, com P maiúsculo."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço.")]),

  dict(n=10, titulo="RECEITA: o martelo que gira", img="aula9/p_exemplo.jpg", clipe=None,
    codigo=MARTELO, auto=(6,),
    corpo="Uma barra comprida e ancorada, com este <span class=ui>Script</span> dentro:",
    depois="Da Aula 7. <b>Salve antes de testar:</b> laço mal escrito congela o Studio.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="A barra gira sozinha e derruba quem passa.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("O Studio travou","Faltou o <span class=ui>task.wait</span> dentro do laço."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=11, titulo="RECEITA: a loja", img="aula9/p_exemplo.jpg", clipe=None,
    codigo=LOJA, auto=(11, 12, 13),
    corpo="Uma plataforma com este <span class=ui>Script</span>. <b>Precisa do placar e de moedas.</b>",
    depois="Da Aula 8. Mude o <span class=ui>preco</span> e o que ela vende.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Com moedas suficientes você fica rápido e o placar desconta.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Compro sem ter moeda","Confira o <span class=ui>>=</span> e o valor do <span class=ui>preco</span>."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=12, titulo="Escolha duas receitas e ponha no seu mapa", img="aula9/p_exemplo.jpg", clipe="08_inserir_script.gif",
    corpo="<b>Duas</b>, não seis. Ponha uma, teste, conserte. Só então ponha a outra. Quem põe tudo de uma vez não descobre qual quebrou.<br><br>Volte na receita que você escolheu e faça, na ordem:<br><br><b>1.</b> <b>Monte a peça</b> que a receita descreve — aba <span class=ui>Modelo</span>, botão <span class=ui>Parte</span>, <span class=ui>Âncora</span>, e depois a cor, o material e o tamanho que ela pede.<br><b>2.</b> <b>Renomeie</b> a peça, se a receita der um nome. O da porta (<span class=ui>Porta</span>) e o do placar são levados a sério: o código procura por esse nome exato.<br><b>3.</b> Clique na peça na lista da direita, clique no <b>+</b> e escolha <span class=ui>Script</span> — é o gesto da animação ao lado.<br><b>4.</b> <b>Apague</b> o <span class=ui>print(\"Hello world!\")</span> (clique no fim da linha e segure <b>Backspace</b>).<br><b>5.</b> <b>Digite o código da receita</b> nesse Script, sem as linhas em cinza e sem Tab. É este passo que a animação não mostra, e é o que faz a coisa funcionar.<br><b>6.</b> Volte para a aba <span class=ui>Place1</span>, aperte o <b>▶</b> e teste <b>só essa</b> receita. Só depois comece a segunda.<br><br><b>Uma exceção:</b> a receita do <b>placar</b> (passo 7) não vai numa peça — o Script dela vai dentro do <span class=ui>ServerScriptService</span>, lá na lista da direita. E as receitas da <b>moeda</b> e da <b>loja</b> só funcionam se o placar já estiver lá.",
    ck="As duas funcionam no seu mapa, testadas uma de cada vez — e <b>nenhum Script seu está vazio</b>: cada um tem o código da sua receita, sem risco vermelho.",
    sos=[("Pus o Script e não acontece nada","Abra ele com dois cliques na lista. Se estiver <b>vazio</b>, ou ainda com o <span class=ui>print(\"Hello world!\")</span>, é isso: falta digitar o código da receita dentro dele."),
         ("Pus tudo e nada funciona","Apague os scripts, ponha um só, teste. Depois o próximo."),
         ("Deu erro vermelho na tela","Leia o nome que aparece no erro — quase sempre é uma peça com nome diferente do que está no código.")]),

  dict(n=13, titulo="Teste como se fosse outra pessoa", img="aula9/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Aperte o <b>▶</b> e jogue o seu jogo <b>até o fim</b>, sem trapacear.<br><br>Depois faça de propósito o que um aluno chato faria: pular fora do caminho, ficar parado em cima da lava, voltar para trás.",
    ck="Você chegou ao fim pelo menos uma vez, e sabe onde o jogo quebra.",
    sos=[("É impossível de terminar","Afaste menos as plataformas ou aumente os tempos de espera."),
         ("Dá para pular o percurso todo","Ponha paredes nas laterais, ou lava embaixo.")]),

  dict(n=14, titulo="Conserte as três piores coisas", img="aula9/s_jogar_c.jpg", clipe=None,
    corpo="Escolha as <b>três</b> que mais atrapalharam no teste e conserte só elas.<br><br>Não tente deixar perfeito. Tem que publicar hoje.",
    ck="As três estão consertadas e você testou de novo.",
    sos=[("Tudo está ruim","Escolha as três que atrapalharam mais. Perfeito não existe.")]),

  dict(n=15, titulo="Publique", img="aula9/s_parar_b.jpg", clipe=None,
    corpo="<span class=ui>Arquivo → Publicar na Roblox</span>. Nome, descrição, e <b>desligue o Compartilhamento de dados</b>.<br><br>Depois, no site, deixe o jogo <b>Público</b>.",
    ck="Você tem um link que começa com <b>roblox.com/games/</b>.",
    sos=[("Esqueci como era","Aula 4, passos 9 a 16."),
         ("Já publiquei antes","Então é só <span class=ui>Publicar na Roblox</span> de novo: ele atualiza sem pedir nada.")]),

  dict(n=16, titulo="Dê um nome que dê vontade de clicar", img="aula9/s_parar_b.jpg", clipe=None,
    corpo="<i>Jogo do Pedro</i> não convida ninguém. <i>Não pise no vermelho</i> convida.<br><br>Na descrição, escreva em uma frase o que a pessoa tem que fazer.",
    ck="O nome diz o que é o jogo, sem precisar abrir.",
    sos=[("Não sei o que escrever","Use a primeira das três linhas que você escreveu no papel, no passo 3.")]),

  dict(n=17, titulo="Troque o link com dois colegas", img="aula9/p_exemplo.jpg", clipe=None,
    corpo="Mande o seu link para duas pessoas e peça o delas.",
    ck="Você tem dois links de colegas abertos.",
    sos=[("O link do colega não abre","O jogo dele ainda está privado. Ele precisa fazer o passo 15 da Aula 4.")]),

  dict(n=18, titulo="Jogue o jogo dos dois", img="aula9/p_exemplo.jpg", clipe=None,
    corpo="Jogue até o fim, se der. E diga para cada um <b>uma</b> coisa que você gostou e <b>uma</b> que travou.<br><br>Uma de cada. Não é para fazer lista de defeitos.",
    ck="Você jogou os dois e falou uma coisa boa e uma travada para cada autor.",
    sos=[("Não consegui passar","Isso é informação útil. Diga exatamente onde travou.")]),

  dict(n=19, titulo="Conserte uma coisa que te falaram", img="aula9/s_jogar_b.jpg", clipe=None,
    corpo="Volte ao Studio, conserte <b>uma</b> das coisas que os colegas apontaram, e publique de novo.<br><br>Isso é o que acontece em jogo de verdade: alguém joga, reclama, você arruma.",
    ck="Você publicou uma segunda versão.",
    sos=[("Não deu tempo","Anote o que falaram. Conserta na próxima.")]),

  dict(n=20, titulo="Salve e guarde o link", img="aula9/s_parar_b.jpg", clipe=None,
    corpo="<b>Ctrl + S</b> → <b>Salvar em arquivo</b>.<br><br>E copie o link do seu jogo para um lugar que você não perca — ele é seu, e continua no ar depois que o curso acabar.",
    ck="Arquivo salvo e link guardado.",
    sos=[("Perdi o link","Entre em <b>create.roblox.com</b> com a sua conta. Está tudo lá.")]),
 ],
}
