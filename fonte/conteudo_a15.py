# -*- coding: utf-8 -*-
"""Aula 15 — Uma ferramenta na mão (Tool em StarterPack)."""

MOLA = '''local mola = script.Parent

mola.Activated:Connect(function()
\tlocal corpo = mola.Parent
\tlocal humano = corpo:FindFirstChild("Humanoid")
\tif humano then
\t\thumano.JumpHeight = 40
\t\ttask.wait(4)
\t\thumano.JumpHeight = 7.2
\tend
end)'''

LANTERNA = '''local lanterna = script.Parent
local luz = lanterna.Handle.PointLight

lanterna.Activated:Connect(function()
\tluz.Enabled = not luz.Enabled
end)'''

PREPARA = [
   ("Projeto novo", "Esta aula começa do zero, num projeto novo."),
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Um nome que não é escolha sua", "Hoje tem uma peça que <b>tem</b> de se chamar <span class=ui>Handle</span>. Não é capricho da aula: é o Roblox que procura esse nome para saber o que pôr na mão do boneco."),
   ("Atalhos", "Este material usa <span class=ui>Ctrl</span>, do Windows. Num Mac, troque Ctrl por <span class=ui>⌘</span>."),
]

P1 = dict(n=1, titulo="Abra o Studio e escolha BASEPLATE", img="comum/c01_tela_inicial.jpg", clipe=None,
    corpo="Projeto novo. <b>Role a página para baixo</b> até <span class=ui>Abrir um modelo</span> e clique no <span class=ui>Baseplate</span>.",
    ck="Abriu o mundo cinza.",
    sos=[("Apareceu uma janelinha de Boas-vindas por cima","Clique em <span class=ui>Voltar ao início</span>, o botão da esquerda — ou no <b>✕</b> do canto. Não clique em <span class=ui>Iniciar a introdução</span>."),
         ("Abriu o projeto antigo","Feche a aba dele no <b>x</b> e volte para o Início.")])

P2 = dict(n=2, titulo="Prepare o editor (uma vez em cada computador)", img="comum/c06_preparar_editor.jpg", clipe=None,
    corpo="Hoje você vai <b>digitar código</b>. O Studio vem com duas ajudas que atrapalham quem está aprendendo: ele sugere linhas inteiras e fecha parênteses e aspas sozinho. Vamos desligar as duas.<br><br>No Windows: <span class=ui>Arquivo → Configurações do Studio</span>. No Mac: <span class=ui>Roblox Studio → Configurações do Studio</span>.<br><br><b>1.</b> Na busca escreva <b>assist</b> e desmarque <span class=ui>Ativar assistente de código</span>.<br><b>2.</b> Apague a busca, escreva <b>fechamento</b> e desmarque <span class=ui>Colchetes de fechamento automáticos</span> e <span class=ui>Aspas de fechamento automáticas</span>.<br><br>Feche a janela. Fica guardado no computador — se você já fez isto numa aula passada <b>neste mesmo computador</b>, é só conferir que as caixinhas continuam vazias.",
    ck="As três caixinhas estão <b>vazias</b>: assistente de código, colchetes e aspas.",
    sos=[("Não acho Configurações do Studio","No Windows é o menu <span class=ui>Arquivo</span>, bem no canto de cima à esquerda da janela."),
         ("A busca não acha nada","Escreva só <b>assist</b>, sem acento e sem mais nada."),
         ("Já está tudo desmarcado","Ótimo — este computador já foi preparado. Feche a janela e siga."),
         ("Por que desligar?","Ligado, o editor escreve linhas que você não pediu, e o <b>Tab</b> aceita a sugestão em vez de recuar.")])

SOS_ASPA = ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço.")
SOS_POPUP = ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")
SOS_END = ("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula.")

AULA = {
 "n": 15,
 "slug": "aula15",
 "titulo": "Uma ferramenta na mão",
 "subtitulo": "O boneco passa a carregar alguma coisa — e a usar clicando. É o começo de inventário, arma, ferramenta, item.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 15 · ferramenta",
 "fim": "Acabou a Aula 15. Até hoje o jogador só andava e esbarrava. Agora ele <b>carrega</b> coisas e <b>usa</b> coisas — e é assim que quase todo jogo de Roblox funciona por dentro.",
 "avisos": PREPARA,
 "passos": [
  P1, P2,
  dict(n=3, titulo="Abra a lista e vá para a aba MODELO", img="aula15/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique na <b>setinha</b> à esquerda de <span class=ui>Workspace</span> para abrir a lista, e depois na aba <span class=ui>Modelo</span>.",
    ck="A faixa mostra <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho a aba Modelo","Ela fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=4, titulo="Ache o StarterPack na lista", img="aula15/s_pack_a.jpg", clipe=None,
    corpo="Role a lista da direita até achar <span class=ui>StarterPack</span> — algumas linhas abaixo de Workspace, perto do StarterGui.<br><br>É a <b>mochila inicial</b>: tudo que estiver aqui dentro já vem na mão de todo jogador quando ele entra.",
    ck="Você está vendo a linha <span class=ui>StarterPack</span> na lista.",
    sos=[("Tem vários nomes parecidos","Você quer o <b>StarterPack</b> — não o StarterGui nem o StarterPlayer."),
         ("Não consigo rolar","Use a rodinha do mouse em cima da lista, ou escreva <b>starterp</b> na caixa <span class=ui>Pesquisar</span> do alto dela.")]),

  dict(n=5, titulo="Crie a ferramenta", img="aula15/s_tool_c.jpg", clipe="15_inserir_tool.gif",
    corpo="Clique em <span class=ui>StarterPack</span>, clique no <b>+</b> e, na caixa <span class=ui>Pesquisar objeto</span>, escreva <b>tool</b>. Clique em <span class=ui>Tool</span>.<br><br><span class=ui>Tool</span> quer dizer <i>ferramenta</i>. Sozinha ela ainda é invisível: falta dar um corpo para ela.",
    ck="Dentro de <span class=ui>StarterPack</span> apareceu <span class=ui>Tool</span>.",
    sos=[("Entrou no lugar errado","Arraste-a por cima da palavra <span class=ui>StarterPack</span> na lista."),
         ("Não vejo nada no mundo 3D","É esperado. Ferramenta só aparece quando o jogo roda, na barra de baixo.")]),

  dict(n=6, titulo="Chame a ferramenta de MOLA", img="aula15/s_toolnome_b.jpg", clipe=None,
    corpo="Botão direito nela → <span class=ui>Renomear</span> → <b>Mola</b> → <b>Enter</b>.<br><br>Este nome aparece <b>para o jogador</b>, na barrinha de itens embaixo da tela. Escolha um nome que faça sentido.",
    ck="Na lista está <span class=ui>Mola</span>, dentro de StarterPack.",
    sos=[("Voltou para Tool","Você apertou <b>Esc</b>. Termine com <b>Enter</b>.")]),

  dict(n=7, titulo="Dê um corpo para a ferramenta — e o nome tem de ser HANDLE", img="aula15/s_handle_b.jpg", clipe=None,
    corpo="Clique na <span class=ui>Mola</span>, clique no <b>+</b> e escolha <span class=ui>Part</span>.<br><br>Agora renomeie essa peça para <b>Handle</b> — <b>exatamente assim</b>, com H maiúsculo, em inglês.<br><br>Este é o único nome do curso que você <b>não</b> escolhe. O Roblox procura uma peça chamada <span class=ui>Handle</span> dentro da Tool para saber o que pôr na mão do boneco. Com qualquer outro nome, a ferramenta não aparece.",
    ck="Dentro de <span class=ui>Mola</span> há uma peça chamada <span class=ui>Handle</span>.",
    sos=[("Escrevi handle com h minúsculo","Não funciona. Tem de ser <b>Handle</b>."),
         ("Escrevi Cabo, em português","Não funciona. Este nome é do Roblox, não seu."),
         ("A peça nasceu longe","Não importa: quando o jogo roda, ela vai para a mão do boneco.")]),

  dict(n=8, titulo="Deixe o Handle pequeno — e NÃO ancore", img="aula15/s_handleprop_b.jpg", clipe=None,
    corpo="Com o <span class=ui>Handle</span> selecionado, nas <span class=ui>Propriedades</span>: <b>size</b> = <b>1, 3, 1</b>. Pinte de <b>verde</b>.<br><br><b>Atenção, e é o contrário de tudo que você aprendeu:</b> o Handle <b>não</b> pode estar ancorado. Busque <b>anchored</b> e confira que a caixinha está <b>desmarcada</b>.<br><br>Faz sentido: peça ancorada é peça <i>presa no lugar</i>. A mão do boneco não consegue carregar uma coisa presa no ar.",
    ck="O Handle é um bastãozinho verde, e a caixinha <span class=ui>Anchored</span> está <b>desmarcada</b>.",
    sos=[("Ancorei sem pensar","Desmarque. É o reflexo de todas as aulas passadas — aqui ele atrapalha."),
         ("A peça cai no chão quando eu jogo","Se ela está dentro da Tool e se chama Handle, ela vai para a mão. Se caiu, confira o nome.")]),

  dict(n=9, titulo="Jogue e pegue a mola", img="aula15/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Aperte o <b>▶</b>.<br><br>Olhe a <b>barra embaixo da tela</b>: apareceu um quadradinho escrito <b>Mola</b>. Aperte a tecla <b>1</b> — o boneco pega o bastão na mão.",
    ck="O boneco está segurando o bastão verde, e o item Mola aparece aceso na barra de baixo.",
    sos=[("Não aparece nada na barra","A Tool tem de estar dentro do <span class=ui>StarterPack</span>, e a peça dentro dela tem de se chamar <b>Handle</b>."),
         ("Aparece mas não vai para a mão","Confira se o Handle está <b>desancorado</b>."),
         ("O bastão está atravessado","Normal. Dá para arrumar depois com a propriedade <span class=ui>GripPos</span> da Tool — fica de lição de casa.")]),

  dict(n=10, titulo="Pare e ponha um Script na Mola", img="aula15/s_script_c.jpg", clipe="08_inserir_script.gif",
    corpo="Pare o jogo. Clique na <span class=ui>Mola</span> — na Tool, <b>não</b> no Handle — clique no <b>+</b> e escolha <span class=ui>Script</span>.",
    ck="Dentro de <span class=ui>Mola</span> estão o <span class=ui>Handle</span> e o <span class=ui>Script</span>, lado a lado.",
    sos=[("Pus dentro do Handle","Arraste-o por cima da palavra <span class=ui>Mola</span>. Ele tem de ser irmão do Handle, não filho.")]),

  dict(n=11, titulo="Escreva o código da mola", img="aula15/p_mola_pronto.jpg", clipe=None,
    codigo=MOLA, auto=(10, 11),
    corpo="Apague a linha pronta (clique no fim dela e segure <b>Backspace</b>) e escreva as onze linhas:",
    depois="<span class=ui>Activated</span> é o evento novo: acontece quando o jogador <b>clica com a ferramenta na mão</b>. Repare que ele não recebe nada entre os parênteses — quem usou é sempre quem está segurando.<br><br>E <span class=ui>mola.Parent</span> é o <b>boneco</b>: quando a ferramenta está na mão, ela mora dentro do personagem. É por isso que dá para achar o Humanoid a partir dela.<br><br><b>Não digite as linhas em cinza.</b> E <b>não aperte Tab</b>.",
    ck="Nenhum risco vermelho.",
    sos=[("Diz que Humanoid é nil","A ferramenta está na mochila, não na mão. O código só funciona depois de o jogador apertar 1."),
         ("Nada acontece quando eu clico","Confira se o Script está dentro da <b>Mola</b> e não do Handle."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=12, titulo="Jogue e salte", img="aula15/s_jogar2_b.jpg", clipe=None,
    corpo="Aperte o <b>▶</b>, aperte <b>1</b> para pegar a mola e <b>clique</b> com o mouse.<br><br>Pule nos quatro segundos seguintes.",
    ck="Depois de clicar, o boneco pula muito mais alto por quatro segundos, e depois volta ao normal.",
    sos=[("Não pulo mais alto","Você clicou sem a ferramenta na mão? Aperte <b>1</b> primeiro."),
         ("Fiquei pulando alto para sempre","A última linha, que devolve o <b>7.2</b>, ficou fora do bloco ou não foi escrita."),
         ("Quero pular ainda mais","Aumente o <b>40</b>. Mas cuidado: acima de 100 o boneco sai da tela.")]),

  dict(n=13, titulo="Entenda: Activated e Touched", img="aula15/p_mola_pronto.jpg", clipe=None,
    corpo="Você já tem três jeitos de o código acordar, e cada um serve para uma coisa:<br><br><b>Touched</b> — alguém <b>esbarrou</b> na peça. Serve para armadilha e para moeda.<br><b>Triggered</b> — alguém chegou perto e <b>apertou E</b>. Serve para porta, alavanca, comprar.<br><b>Activated</b> — alguém <b>clicou</b> com a ferramenta na mão. Serve para usar item.<br><br>Os três têm a mesma forma: <span class=ui>alguma_coisa.Evento:Connect(function() ... end)</span>. Muda só quem avisa.",
    ck="Você consegue dizer qual dos três usaria para uma poção que o jogador bebe quando quiser.",
    sos=[("Qual eu usaria?","<b>Activated</b> — a poção é um item na mão, e beber é escolha do jogador.")]),

  dict(n=14, titulo="Faça uma segunda ferramenta: a lanterna", img="aula15/s_lanterna_b.jpg", clipe=None,
    corpo="Agora com menos ajuda. Repita o caminho do começo:<br><br><b>1.</b> No <span class=ui>StarterPack</span>, <b>+</b> → <span class=ui>Tool</span>. Renomeie para <b>Lanterna</b>.<br><b>2.</b> Dentro dela, <b>+</b> → <span class=ui>Part</span>, renomeada para <b>Handle</b>, <b>size</b> = <b>1, 1, 3</b>, <b>desancorada</b>, pintada de <b>branco</b>.<br><b>3.</b> Dentro do <b>Handle</b>, <b>+</b> → busque <b>pointlight</b> → <span class=ui>PointLight</span>.<br><b>4.</b> Nas Propriedades do PointLight: <span class=ui>Brightness</span> = <b>5</b>, <span class=ui>Range</span> = <b>30</b>, e <b>desmarque</b> o <span class=ui>Enabled</span>.",
    ck="Na lista: <span class=ui>StarterPack → Lanterna → Handle → PointLight</span>, com o Enabled desmarcado.",
    sos=[("O PointLight entrou na Tool, não no Handle","Arraste-o por cima da palavra <span class=ui>Handle</span>."),
         ("A luz já está acesa","Desmarque o <span class=ui>Enabled</span>. Ela tem de começar apagada.")]),

  dict(n=15, titulo="Escreva o código da lanterna", img="aula15/p_lanterna_pronto.jpg", clipe=None,
    codigo=LANTERNA, auto=(6,),
    corpo="Ponha um <span class=ui>Script</span> dentro da <span class=ui>Lanterna</span> (irmão do Handle) e escreva as seis linhas:",
    depois="A linha do meio é a mais curta e a mais esperta do curso: <span class=ui>luz.Enabled = not luz.Enabled</span>.<br><br><span class=ui>not</span> quer dizer <b>o contrário</b>. Então ela lê assim: <i>a luz passa a ser o contrário do que ela é agora</i>. Se estava apagada, acende; se estava acesa, apaga. Um clique liga, o outro desliga — sem nenhum <span class=ui>if</span>.",
    ck="Nenhum risco vermelho.",
    sos=[("Diz que PointLight não é membro de Handle","Ele tem de estar dentro do <b>Handle</b>, não da Tool."),
         ("Só liga, nunca desliga","Você escreveu <span class=ui>= true</span> no lugar de <span class=ui>= not luz.Enabled</span>."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=16, titulo="Escureça o mundo para ver a lanterna", img="aula15/s_escuro_b.jpg", clipe=None,
    corpo="Com sol a pino você não vê luz nenhuma. Na lista da direita, clique em <span class=ui>Lighting</span> (algumas linhas abaixo de Workspace).<br><br>Nas <span class=ui>Propriedades</span>, busque <b>clocktime</b> e ponha <b>0</b> — meia-noite.",
    ck="O mundo ficou escuro.",
    sos=[("Não acho Lighting","Está na mesma fileira do StarterGui e do StarterPack, na lista da direita."),
         ("Ficou escuro demais","Busque <b>brightness</b> no Lighting e aumente um pouco, ou use ClockTime <b>5</b>.")]),

  dict(n=17, titulo="Jogue com as duas ferramentas", img="aula15/s_jogar3_b.jpg", clipe=None,
    corpo="Aperte o <b>▶</b>. Agora há <b>dois</b> quadradinhos na barra de baixo.<br><br>Aperte <b>1</b> e <b>2</b> para trocar de ferramenta. Com a lanterna na mão, clique: acende. Clique de novo: apaga.",
    ck="As duas ferramentas aparecem na barra, você troca entre elas, e a lanterna acende e apaga a cada clique.",
    sos=[("Só aparece uma","As duas têm de estar dentro do <span class=ui>StarterPack</span>, cada uma com o seu <b>Handle</b>."),
         ("A luz acende mas não ilumina nada","Aumente o <span class=ui>Range</span> do PointLight para 60."),
         ("Troco de ferramenta e a mola continua ligada","É esperado: o pulo alto dura quatro segundos, não depende de qual item está na mão.")]),

  dict(n=18, titulo="Ponha a ferramenta no chão, para o jogador achar", img="aula15/s_chao_b.jpg", clipe=None,
    corpo="Ferramenta que já vem na mochila é fácil demais. Vamos esconder uma.<br><br><b>1.</b> Na lista, <b>arraste</b> a <span class=ui>Lanterna</span> de dentro do StarterPack para dentro do <span class=ui>Workspace</span>.<br><b>2.</b> Clique no <span class=ui>Handle</span> dela e ponha <b>position</b> = <b>0, 3, -20</b>.<br><br>Agora ela fica largada no chão do mundo. Quem quiser, encosta nela e pega.",
    ck="A lanterna sumiu da barra de baixo e está boiando no mundo, uns passos à frente.",
    sos=[("Não consigo arrastar","Clique e segure em cima do nome, arraste até a palavra <span class=ui>Workspace</span> e solte."),
         ("Ela cai no chão e some","Normal, é desancorada. Suba a position para <b>0, 3, -20</b>."),
         ("Encosto e não pego","Ferramenta no Workspace se pega andando por cima dela. Se não pegar, confira se o Handle continua desancorado.")]),

  dict(n=19, titulo="Teste como se fosse outra pessoa", img="aula15/s_jogar4_b.jpg", clipe=None,
    corpo="Jogue e faça o que um jogador chato faria:<br><br>• clicar sem nenhuma ferramenta na mão;<br>• clicar dez vezes seguidas na mola;<br>• largar a ferramenta (tecla <b>Backspace</b>) e tentar pegá-la de novo.<br><br>Anote o que ficar estranho e conserte uma coisa.",
    ck="Você achou pelo menos um comportamento esquisito e consertou um.",
    sos=[("Clicando dez vezes fico pulando alto para sempre","É o mesmo problema da alavanca da Aula 13: cada clique começa a contagem de novo. Uma solução: desabilitar a ferramenta durante os quatro segundos, com <span class=ui>mola.Enabled = false</span> e depois <b>true</b>."),
         ("Larguei e não acho mais","Ela caiu no chão onde você estava. Olhe no chão, ou pare e jogue de novo.")]),

  dict(n=20, titulo="Salve", img="aula15/s_parar_b.jpg", clipe=None,
    corpo="Pare o jogo. <b>Ctrl + S</b> → <span class=ui>Salvar em arquivo</span> → nome <b>ferramenta</b>.<br><br>Se quiser, publique: <span class=ui>Arquivo → Publicar na Roblox</span>.",
    ck="Salvou sem erro.",
    sos=[("Pediu para publicar","Escolha <span class=ui>Salvar em arquivo</span>."),
         ("Quero uma ferramenta com desenho de verdade","Na Caixa de Ferramentas, aba <span class=ui>Modelos</span>, busque <b>sword</b> ou <b>flashlight</b>: muitos já vêm prontos, com Handle e tudo. Abra e veja por dentro — você vai reconhecer as peças.")]),
 ],
}
