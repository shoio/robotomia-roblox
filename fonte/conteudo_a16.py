# -*- coding: utf-8 -*-
"""Aula 16 — Cronômetro e recorde."""

PLACAR = '''game.Players.PlayerAdded:Connect(function(jogador)
\tlocal pasta = Instance.new("Folder")
\tpasta.Name = "leaderstats"
\tpasta.Parent = jogador

\tlocal tempo = Instance.new("StringValue")
\ttempo.Name = "Tempo"
\ttempo.Value = "--"
\ttempo.Parent = pasta
end)'''

LARGADA = '''local largada = script.Parent

largada.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tjogador:SetAttribute("Comecou", tick())
\tend
end)'''

CHEGADA = '''local chegada = script.Parent

chegada.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tlocal comecou = jogador:GetAttribute("Comecou")
\t\tif comecou then
\t\t\tlocal segundos = math.floor((tick() - comecou) * 10) / 10
\t\t\tjogador.leaderstats.Tempo.Value = segundos .. " s"
\t\t\tjogador:SetAttribute("Comecou", nil)
\t\tend
\tend
end)'''

SOS_ASPA = ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço.")
SOS_POPUP = ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")
SOS_END = ("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula.")

AULA = {
 "n": 16,
 "slug": "aula16",
 "titulo": "Cronômetro e recorde",
 "subtitulo": "O jogo passa a medir quanto tempo você levou. E aí aparece a coisa que faz qualquer obby viciar: bater o próprio tempo.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 16 · cronômetro",
 "fim": "Acabou a Aula 16. O seu obby deixou de ser “consegui ou não” e virou “em quanto tempo”. É a mesma pista de antes — só que agora tem placar, e placar é o que faz alguém jogar dez vezes.",
 "avisos": [
   ("Projeto novo", "Esta aula começa do zero, num projeto novo."),
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Vem da Aula 5", "O placar do canto da tela é o mesmo <span class=ui>leaderstats</span> das moedas. Hoje ele guarda texto em vez de número."),
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

  dict(n=3, titulo="Abra a lista e vá para a aba MODELO", img="aula16/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique na <b>setinha</b> à esquerda de <span class=ui>Workspace</span> para abrir a lista, e depois na aba <span class=ui>Modelo</span>.",
    ck="A faixa mostra <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho a aba Modelo","Ela fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=4, titulo="Faça a faixa de largada", img="aula16/s_largada_b.jpg", clipe="02_criar_peca.gif",
    corpo="<span class=ui>Parte</span> → <span class=ui>Âncora</span>.<br><br><b>size</b> = <b>20, 1, 2</b> e <b>position</b> = <b>0, 0.5, -6</b>. Pinte de <b>branco</b> e renomeie para <b>Largada</b>.<br><br>É a linha que o jogador cruza para o relógio começar.",
    ck="Uma faixa branca fina atravessada no chão, logo à frente de onde você nasce.",
    sos=[("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete."),
         ("Nasci em cima dela","Afaste: use <b>-6</b> no terceiro número da position.")]),

  dict(n=5, titulo="Faça o percurso", img="aula16/s_percurso_b.jpg", clipe=None,
    corpo="Dez minutos, sem código nenhum. Monte um caminho entre a largada e o fim — plataformas para pular, uma lava para desviar, o que você quiser.<br><br>Duas regras: tem de dar para atravessar <b>andando e pulando</b>, e tem de ser <b>longo o bastante</b> para valer a pena cronometrar. Uns 60 passos.<br><br>Atalho: faça <b>uma</b> plataforma e duplique com botão direito → <span class=ui>Duplicar</span>, mudando a <b>position</b> de cada cópia.",
    ck="Você atravessou o seu percurso do começo ao fim, andando, pelo menos uma vez.",
    sos=[("Minhas peças caem","Faltou a <span class=ui>Âncora</span>. Criou, ancorou."),
         ("Não alcanço a próxima","O boneco pula uns 7 passos de altura e uns 10 de distância. Aproxime."),
         ("Está ficando grande demais","Pare. Percurso curto e terminado vale mais que longo e pela metade.")]),

  dict(n=6, titulo="Faça a faixa de chegada", img="aula16/s_chegada_b.jpg", clipe=None,
    corpo="Mais uma faixa, igual à primeira, no fim do percurso: <span class=ui>Parte</span> → <span class=ui>Âncora</span>, <b>size</b> = <b>20, 1, 2</b>, pintada de <b>verde</b>, renomeada para <b>Chegada</b>.<br><br>Ponha a <b>position</b> dela no fim do seu caminho — o terceiro número é o que muda.",
    ck="Uma faixa verde no fim do percurso, e na lista estão <span class=ui>Largada</span> e <span class=ui>Chegada</span>.",
    sos=[("Não sei que position usar","Clique na última peça do percurso, veja a position dela nas Propriedades, e use um valor um pouco além."),
         ("As duas faixas estão coladas","Seu percurso está curto. Não tem problema para hoje, mas fica menos divertido.")]),

  dict(n=7, titulo="Ponha o placar no ServerScriptService", img="aula16/s_sss_c.jpg", clipe=None,
    corpo="Na lista da direita ache <span class=ui>ServerScriptService</span> (algumas linhas abaixo de Workspace; role a lista se não estiver à vista), clique nele, clique no <b>+</b> e escolha <span class=ui>Script</span>.<br><br>Este script vale para o <b>jogo inteiro</b>, não para uma peça.",
    ck="Abriu o editor e o <span class=ui>Script</span> está dentro do <span class=ui>ServerScriptService</span>.",
    sos=[("Não acho ServerScriptService","Escreva <b>server</b> na caixa <span class=ui>Pesquisar</span> do alto da lista."),
         ("Esqueci como era","Está tudo na Aula 5, passos 4 e 5.")]),

  dict(n=8, titulo="Escreva o placar de tempo", img="aula16/p_placar_pronto.jpg", clipe=None,
    codigo=PLACAR, auto=(10,),
    corpo="Apague a linha pronta (clique no fim dela e segure <b>Backspace</b>) e escreva:",
    depois="É quase o placar da Aula 5, com <b>uma</b> diferença: em vez de <span class=ui>IntValue</span>, que guarda número inteiro, este é um <span class=ui>StringValue</span>, que guarda <b>texto</b>.<br><br>Precisa ser texto porque o tempo vai aparecer como <b>12.4 s</b> — com o “s” no fim. Número não guarda letra.<br><br><b>Não digite a linha em cinza.</b> E <b>não aperte Tab</b>.",
    ck="Nenhum risco vermelho.",
    sos=[("Escrevi IntValue","Não funciona: o valor vai ter letra. Tem de ser <b>StringValue</b>."),
         ("Escrevi Leaderstats com L maiúsculo","Não funciona. Tem de ser <b>leaderstats</b>, tudo minúsculo — é a Roblox que exige esse nome exato."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=9, titulo="Jogue só para ver o placar", img="aula16/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Volte para a aba <span class=ui>Place1</span> e aperte o <b>▶</b>. Olhe o <b>canto superior direito</b>.",
    ck="Apareceu um quadro com <b>Tempo</b> e, embaixo, dois tracinhos: <b>--</b>",
    sos=[("Não apareceu o placar","Quase sempre é o nome: confira se está <b>leaderstats</b>, tudo minúsculo, entre aspas."),
         ("Apareceu só o nome, sem coluna","Faltou a parte do <span class=ui>StringValue</span>. Confira as quatro últimas linhas.")]),

  dict(n=10, titulo="Pare e ponha um Script na largada", img="aula16/s_scriptl_c.jpg", clipe="08_inserir_script.gif",
    corpo="Pare o jogo. Clique em <span class=ui>Largada</span>, clique no <b>+</b> e escolha <span class=ui>Script</span>.",
    ck="O Script está dentro da <span class=ui>Largada</span>.",
    sos=[("O Script ficou fora","Arraste-o por cima da palavra <span class=ui>Largada</span> na lista.")]),

  dict(n=11, titulo="Ligue o cronômetro ao cruzar a largada", img="aula16/p_largada_pronto.jpg", clipe=None,
    codigo=LARGADA, auto=(7, 8),
    corpo="Apague a linha pronta e escreva:",
    depois="A linha do meio é a novidade: <span class=ui>jogador:SetAttribute(\"Comecou\", tick())</span>.<br><br><span class=ui>tick()</span> devolve <b>que horas são</b>, em segundos, num número enorme. Sozinho ele não serve para nada — o que vale é a <b>diferença</b> entre dois tick().<br><br><span class=ui>SetAttribute</span> é um <b>bilhete colado no jogador</b>. Aqui a gente cola um bilhete escrito <i>“Comecou”</i> com a hora da largada dentro. Quem vai ler esse bilhete é a chegada.",
    ck="Nenhum risco vermelho.",
    sos=[("Por que não uso uma variável normal?","Porque a largada e a chegada são <b>dois scripts diferentes</b>. Um não enxerga a variável do outro. O bilhete fica colado no jogador, e os dois conseguem ler."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=12, titulo="Ponha um Script na chegada", img="aula16/s_scriptc_c.jpg", clipe=None,
    corpo="Clique em <span class=ui>Chegada</span>, clique no <b>+</b> e escolha <span class=ui>Script</span>.",
    ck="O Script está dentro da <span class=ui>Chegada</span>.",
    sos=[("Já tenho um na Largada","Este é outro. Cada faixa tem o seu.")]),

  dict(n=13, titulo="Conte o tempo na chegada", img="aula16/p_chegada_pronto.jpg", clipe=None,
    codigo=CHEGADA, auto=(11, 12, 13),
    corpo="Apague a linha pronta e escreva as treze linhas. Repare que há um <span class=ui>if</span> <b>dentro</b> do outro:",
    depois="A linha da conta é a mais densa do curso, então leia devagar:<br><br><span class=ui>tick() - comecou</span> — quanto tempo passou, em segundos, com um monte de casas decimais.<br><span class=ui>* 10</span> e depois <span class=ui>/ 10</span>, com <span class=ui>math.floor</span> no meio — é o truque para deixar <b>uma</b> casa depois da vírgula. O <span class=ui>math.floor</span> joga fora as casas; multiplicar antes e dividir depois salva a primeira.<br><span class=ui>.. \" s\"</span> — gruda o “ s” no fim, com espaço.<br><br>E a última linha de dentro <b>apaga o bilhete</b>: sem ela, tocar na chegada duas vezes daria um tempo maluco.",
    ck="Nenhum risco vermelho, e são três <span class=ui>end</span>, o último com <b>)</b>.",
    sos=[("Por que o if dentro do if?","O primeiro pergunta “é um jogador?”. O segundo pergunta “ele chegou a passar pela largada?”. Sem o segundo, quem nascesse em cima da chegada quebraria a conta."),
         ("O tempo sai com mil casas","Faltou o <span class=ui>math.floor</span>, ou o <b>* 10</b> e o <b>/ 10</b>."),
         ("O tempo sai zerado","Você tocou na chegada sem passar pela largada."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=14, titulo="Corra o seu percurso", img="aula16/s_jogar2_b.jpg", clipe=None,
    corpo="Aperte o <b>▶</b>. Passe <b>por cima</b> da faixa branca, atravesse o percurso, e pise na faixa verde.<br><br>Olhe o placar no canto.",
    ck="O placar saiu de <b>--</b> e passou a mostrar o seu tempo, como <b>14.3 s</b>.",
    sos=[("O placar não muda","Confira: o Script está dentro da <span class=ui>Chegada</span>? Você passou <b>por cima</b> da largada, e não ao lado dela?"),
         ("Deu erro vermelho na Saída","Leia o nome no erro — é quase sempre <b>Tempo</b> ou <b>leaderstats</b> escrito diferente do placar."),
         ("Meu tempo deu 0.1 s","Sua largada e sua chegada estão coladas, ou você nasceu em cima da chegada.")]),

  dict(n=15, titulo="Corra de novo e tente bater", img="aula16/s_jogar3_b.jpg", clipe=None,
    corpo="Sem parar o jogo, volte para a largada e corra de novo.<br><br>O placar mostra o tempo da <b>última</b> corrida. Corra três vezes e veja o número mudar.",
    ck="Você correu pelo menos três vezes e o número mudou a cada vez.",
    sos=[("O tempo não atualiza","Você precisa cruzar a <b>largada</b> de novo antes de ir para a chegada. Sem bilhete novo, não há conta nova."),
         ("Quero ver o relógio correndo na tela","Dá — é o letreiro da Aula 11 mais um <span class=ui>while</span> da Aula 7. Boa lição de casa.")]),

  dict(n=16, titulo="Guarde o RECORDE, não só o último", img="aula16/p_recorde_pronto.jpg", clipe=None,
    corpo="Mostrar o último tempo é pouco: o que faz jogar de novo é o <b>melhor</b> tempo.<br><br>No script da <span class=ui>Chegada</span>, troque a linha que escreve no placar por estas <b>quatro</b>:<br><br><span class=ui>local recorde = jogador:GetAttribute(\"Recorde\")</span><br><span class=ui>if not recorde or segundos &lt; recorde then</span><br><span class=ui>jogador:SetAttribute(\"Recorde\", segundos)</span><br><span class=ui>jogador.leaderstats.Tempo.Value = segundos .. \" s\"</span><br><br>e feche com <b>um</b> <span class=ui>end</span> a mais depois delas.<br><br>Repare que o <span class=ui>SetAttribute</span> é o mesmo do passo 11 — muda só o nome do bilhete, que agora é Recorde. Um jogador pode carregar quantos bilhetes você quiser, cada um com o seu nome.",
    depois="A segunda linha se lê assim: <i>se ainda não existe recorde, <b>ou</b> se o tempo de agora for menor que ele</i>. O <span class=ui>not recorde</span> é o que deixa o primeiro tempo entrar — sem ele, nunca haveria um primeiro.",
    ck="O placar só muda quando você faz um tempo <b>melhor</b> que o anterior.",
    sos=[("O placar nunca muda","Falta o <span class=ui>not recorde</span> na condição: sem ele o primeiro tempo nunca entra, e aí nenhum outro entra também."),
         ("O placar muda sempre","Você escreveu <b>&gt;</b> no lugar de <b>&lt;</b>. Tempo menor é melhor."),
         ("Sobraram end a mais","Você acrescentou <b>um</b> <span class=ui>if</span>, então precisa de <b>um</b> end a mais — não dois."),
         ("Por que um bilhete e não uma variável?","Porque cada jogador tem o seu recorde. Uma variável do script seria uma só, compartilhada por todo mundo.")]),

  dict(n=17, titulo="Zere o cronômetro quando o jogador morre", img="aula16/p_zera_pronto.jpg", clipe=None,
    corpo="Se o jogador morre no meio do percurso, o bilhete continua colado — e quando ele chegar, o tempo vai incluir a morte. Errado.<br><br>No script do <span class=ui>ServerScriptService</span>, dentro do <span class=ui>PlayerAdded</span>, acrescente no fim:<br><br><span class=ui>jogador.CharacterAdded:Connect(function(corpo)</span><br><span class=ui>jogador:SetAttribute(\"Comecou\", nil)</span><br><span class=ui>end)</span><br><br>Toda vez que o boneco nasce — inclusive depois de morrer — o bilhete é rasgado. Quem quiser tempo, cruza a largada de novo.",
    ck="Morrer no meio do percurso zera o cronômetro: a próxima chegada só conta se você passar pela largada outra vez.",
    sos=[("Continua contando depois de eu morrer","A linha ficou fora do <span class=ui>PlayerAdded</span>. Ela tem de estar <b>dentro</b> dele, recuada."),
         ("O que é CharacterAdded?","É “quando o boneco deste jogador nascer”. Acontece ao entrar no jogo e a cada vez que ele renasce.")]),

  dict(n=18, titulo="Teste como se fosse outra pessoa", img="aula16/s_jogar4_b.jpg", clipe=None,
    corpo="Jogue e tente trapacear:<br><br>• ir direto para a chegada sem passar pela largada;<br>• pisar na largada e voltar, pisar de novo;<br>• morrer de propósito no meio;<br>• pisar na chegada duas vezes seguidas.<br><br>Cada um desses já tem conserto no seu código. Confira se todos funcionam.",
    ck="Nenhuma das quatro trapaças quebra o placar.",
    sos=[("Consegui quebrar","Ótimo — é para isso que serve o teste. Escreva no papel o que você fez e conserte, ou conte para o professor.")]),

  dict(n=19, titulo="Convide um colega para bater o seu tempo", img="aula16/p_cena.jpg", clipe=None,
    corpo="Publique (<span class=ui>Arquivo → Publicar na Roblox</span>, como na Aula 4), deixe o jogo <b>Público</b> e mande o link para a pessoa do lado.<br><br>Anote no caderno: <b>o seu recorde</b> e <b>o dela</b>.",
    ck="Você tem os dois tempos anotados.",
    sos=[("Esqueci como publica","Aula 4, passo 9."),
         ("O link do colega não abre","O jogo dele ainda está privado. Ele precisa fazer o passo 15 da Aula 4.")]),

  dict(n=20, titulo="Salve", img="aula16/s_parar_b.jpg", clipe=None,
    corpo="Pare o jogo. <b>Ctrl + S</b> → <span class=ui>Salvar em arquivo</span> → nome <b>cronometro</b>.",
    ck="Salvou sem erro.",
    sos=[("Pediu para publicar","Escolha <span class=ui>Salvar em arquivo</span>. Publicar é outra coisa, e você já fez no passo 19."),
         ("O recorde some quando eu saio","Some mesmo — ele só vive enquanto o jogo está no ar. Guardar de um dia para o outro é a <b>Aula 17</b>.")]),
 ],
}
