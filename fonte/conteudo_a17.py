# -*- coding: utf-8 -*-
"""Aula 17 — O progresso fica salvo (DataStore).

   ATENCAO: esta aula so roda com o jogo PUBLICADO e com 'Ativar acesso da
   API Studio' ligado nas configuracoes do jogo. Isso tem de ser testado na
   maquina da escola ANTES de dar a aula."""

COFRE = '''local DataStoreService = game:GetService("DataStoreService")
local cofre = DataStoreService:GetDataStore("MinhasMoedas")

game.Players.PlayerAdded:Connect(function(jogador)
\tlocal pasta = Instance.new("Folder")
\tpasta.Name = "leaderstats"
\tpasta.Parent = jogador

\tlocal moedas = Instance.new("IntValue")
\tmoedas.Name = "Moedas"
\tmoedas.Parent = pasta

\tlocal deu, guardado = pcall(function()
\t\treturn cofre:GetAsync(jogador.UserId)
\tend)

\tif deu and guardado then
\t\tmoedas.Value = guardado
\tend
end)'''

SALVA = '''game.Players.PlayerRemoving:Connect(function(jogador)
\tpcall(function()
\t\tcofre:SetAsync(jogador.UserId, jogador.leaderstats.Moedas.Value)
\tend)
end)'''

MOEDA = '''local moeda = script.Parent

moeda.Touched:Connect(function(parte)
\tlocal jogador = game.Players:GetPlayerFromCharacter(parte.Parent)
\tif jogador then
\t\tjogador.leaderstats.Moedas.Value = jogador.leaderstats.Moedas.Value + 1
\t\tmoeda:Destroy()
\tend
end)'''

SOS_ASPA = ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço.")
SOS_POPUP = ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")
SOS_END = ("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula.")

AULA = {
 "n": 17,
 "slug": "aula17",
 "titulo": "O progresso fica salvo",
 "subtitulo": "Você sai do jogo, volta amanhã, e as suas moedas continuam lá. É a aula mais difícil do curso — e a que mais muda o que o seu jogo é.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 17 · guardar",
 "fim": "Acabou a Aula 17. Todos os jogos que você fez até hoje esqueciam tudo ao fechar. Este não esquece. É a diferença entre um brinquedo e um jogo que a pessoa volta para jogar.",
 "avisos": [
   ("Esta aula precisa de internet e de conta", "Diferente de todas as outras: o cofre fica <b>nos computadores da Roblox</b>, não no seu. Sem publicar e sem ligar o acesso, nada funciona — e é isso que os passos 3 e 4 resolvem."),
   ("Projeto novo", "Esta aula começa do zero, num projeto novo."),
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático."),
   ("Atalhos", "Este material usa <span class=ui>Ctrl</span>, do Windows. Num Mac, troque Ctrl por <span class=ui>⌘</span>."),
 ],
 "passos": [
  dict(n=1, titulo="Abra o Studio e escolha BASEPLATE", img="comum/c01_tela_inicial.jpg", clipe=None,
    corpo="Projeto novo. <b>Role a página para baixo</b> até <span class=ui>Abrir um modelo</span> e clique no <span class=ui>Baseplate</span>.<br><br>Antes de qualquer coisa, olhe o canto superior direito: tem de aparecer a <b>sua fotinho de perfil</b>. Se aparecer <span class=ui>Entrar</span>, você não está conectado — chame o professor agora, porque hoje sem conta não dá.",
    ck="Abriu o mundo cinza e a sua foto de perfil está no canto superior direito.",
    sos=[("Apareceu uma janelinha de Boas-vindas por cima","Clique em <span class=ui>Voltar ao início</span>, o botão da esquerda — ou no <b>✕</b> do canto."),
         ("Estou como Entrar","Clique em <span class=ui>Entrar</span> e faça login. Sem conta, a aula de hoje não roda.")]),

  dict(n=2, titulo="Prepare o editor (uma vez em cada computador)", img="comum/c06_preparar_editor.jpg", clipe=None,
    corpo="Hoje você vai <b>digitar código</b>. O Studio vem com duas ajudas que atrapalham quem está aprendendo: ele sugere linhas inteiras e fecha parênteses e aspas sozinho. Vamos desligar as duas.<br><br>No Windows: <span class=ui>Arquivo → Configurações do Studio</span>. No Mac: <span class=ui>Roblox Studio → Configurações do Studio</span>.<br><br><b>1.</b> Na busca escreva <b>assist</b> e desmarque <span class=ui>Ativar assistente de código</span>.<br><b>2.</b> Apague a busca, escreva <b>fechamento</b> e desmarque <span class=ui>Colchetes de fechamento automáticos</span> e <span class=ui>Aspas de fechamento automáticas</span>.<br><br>Feche a janela.",
    ck="As três caixinhas estão <b>vazias</b>: assistente de código, colchetes e aspas.",
    sos=[("Não acho Configurações do Studio","No Windows é o menu <span class=ui>Arquivo</span>, bem no canto de cima à esquerda da janela."),
         ("Já está tudo desmarcado","Ótimo — este computador já foi preparado. Feche a janela e siga.")]),

  dict(n=3, titulo="PUBLIQUE antes de programar", img="aula17/s_publicar_b.jpg", clipe=None,
    corpo="Hoje a ordem é ao contrário das outras aulas: <b>publicar vem primeiro</b>.<br><br>O cofre onde as moedas vão ficar guardadas mora nos computadores da Roblox, e ele só existe para um jogo que <b>tem endereço lá</b>. Num arquivo que só vive no seu computador, não há cofre nenhum.<br><br><span class=ui>Arquivo → Publicar na Roblox</span>. Dê um nome, <b>desligue o Compartilhamento de dados</b> e clique em <span class=ui>Criar</span>. Igual à Aula 4.",
    ck="O nome da aba lá em cima deixou de ser <span class=ui>Place1</span> e passou a ter o seu nome de usuário.",
    sos=[("Esqueci como publica","Aula 4, passos 9 a 12."),
         ("Deu erro ao publicar","Confira a internet e se você está conectado na sua conta."),
         ("Por que publicar antes?","Porque o cofre pertence ao <b>jogo publicado</b>. Sem publicar, o código roda mas não acha cofre nenhum, e você ia passar a aula caçando um erro que não é seu.")]),

  dict(n=4, titulo="LIGUE o acesso da API — sem isto nada funciona", img="aula17/s_api_b.jpg", clipe=None,
    corpo="Este é o passo que mais faz gente perder a aula inteira. Preste atenção.<br><br><span class=ui>Arquivo → Configurações do jogo</span> (em inglês, <i>Game Settings</i>). Na lista da esquerda, escolha <span class=ui>Segurança</span>.<br><br><b>Ligue</b> a chave <span class=ui>Ativar acesso da API Studio</span> (<i>Enable Studio Access to API Services</i>). Clique em <span class=ui>Salvar</span>.<br><br>Ela existe por segurança: sem ela, um projeto aberto no Studio não consegue mexer nos dados de verdade do jogo. Como hoje é exatamente isso que a gente quer, a chave tem de estar ligada.",
    ck="A chave <span class=ui>Ativar acesso da API Studio</span> está ligada e você clicou em Salvar.",
    sos=[("Não acho Configurações do jogo","É o menu <span class=ui>Arquivo</span>, algumas linhas abaixo de <span class=ui>Publicar na Roblox</span>."),
         ("Não acho a chave","Ela está na página <span class=ui>Segurança</span> da janela, não na primeira."),
         ("A chave não liga","Quase sempre é porque o jogo ainda não foi publicado. Faça o passo 3 primeiro."),
         ("Continua não ligando","Pode ser bloqueio da conta ou da rede da escola. Chame o professor: sem esta chave a aula não roda, e existe um plano B.")]),

  dict(n=5, titulo="Abra a lista e vá para a aba MODELO", img="aula17/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique na <b>setinha</b> à esquerda de <span class=ui>Workspace</span> para abrir a lista, e depois na aba <span class=ui>Modelo</span>.",
    ck="A faixa mostra <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho a aba Modelo","Ela fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=6, titulo="Ponha o script do cofre no ServerScriptService", img="aula17/s_sss_c.jpg", clipe=None,
    corpo="Na lista da direita ache <span class=ui>ServerScriptService</span>, clique nele, clique no <b>+</b> e escolha <span class=ui>Script</span>.<br><br>Tem de ser aqui, e por um motivo sério: este é o único lugar cujo código roda <b>no servidor</b>. Cofre que o jogador consegue mexer não é cofre.",
    ck="Abriu o editor e o <span class=ui>Script</span> está dentro do <span class=ui>ServerScriptService</span>.",
    sos=[("Não acho ServerScriptService","Escreva <b>server</b> na caixa <span class=ui>Pesquisar</span> do alto da lista."),
         ("Posso pôr numa peça?","Não. Numa peça o código roda igual, mas o cofre recusaria — e é bom que recuse.")]),

  dict(n=7, titulo="Escreva a primeira metade: abrir o cofre e ler", img="aula17/p_cofre_pronto.jpg", clipe=None,
    codigo=COFRE, auto=(15, 19, 20),
    corpo="Apague a linha pronta (clique no fim dela e segure <b>Backspace</b>) e escreva as vinte linhas. É o código mais longo do curso — vá devagar, uma linha de cada vez.",
    depois="Você já conhece o miolo: é o <span class=ui>leaderstats</span> da Aula 5, igualzinho. O que é novo são as pontas.<br><br><b>As duas primeiras linhas</b> pedem o cofre à Roblox e dão um nome a ele: <span class=ui>MinhasMoedas</span>. Esse nome é a etiqueta da gaveta — se você trocar depois, abre uma gaveta vazia.<br><br><b>O <span class=ui>pcall</span></b> é a novidade importante, e o passo 9 explica.<br><br><b>Não digite as linhas em cinza.</b> E <b>não aperte Tab</b>.",
    ck="Nenhum risco vermelho, e o código tem cinco <span class=ui>end</span> ao todo, contando os de dentro.",
    sos=[("Me perdi nos end","Conte os blocos que abrem: o <span class=ui>PlayerAdded</span>, o <span class=ui>pcall</span> e o <span class=ui>if</span>. Cada um fecha com um end; os dois primeiros fecham com <b>end)</b>, porque estão dentro de parênteses."),
         ("Diz que DataStoreService não existe","Confira a escrita: <b>DataStoreService</b>, com D, S e S maiúsculos, tudo colado."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=8, titulo="Escreva a segunda metade: guardar ao sair", img="aula17/p_salva_pronto.jpg", clipe=None,
    codigo=SALVA, auto=(4, 5),
    corpo="Agora, <b>no fim do mesmo script</b>, pule uma linha e acrescente mais cinco:",
    depois="<span class=ui>PlayerRemoving</span> é o contrário do <span class=ui>PlayerAdded</span>: acontece quando o jogador <b>está saindo</b>. É o último instante em que dá para guardar.<br><br>Repare que o <span class=ui>cofre</span> aqui é o mesmo lá de cima — está no mesmo arquivo, então as duas partes enxergam a mesma gaveta.",
    ck="O script inteiro agora tem duas partes: uma que começa com <span class=ui>PlayerAdded</span> e outra com <span class=ui>PlayerRemoving</span>.",
    sos=[("Diz que cofre não existe","Você pôs a segunda parte num script <b>novo</b>. Ela tem de ir no fim do <b>mesmo</b> script."),
         ("Escrevi PlayerRemoved","É <b>PlayerRemoving</b>, com ING no fim."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=9, titulo="Entenda o pcall — a rede de segurança", img="aula17/p_salva_pronto.jpg", clipe=None,
    corpo="Todo o resto do curso acontece <b>dentro</b> do seu computador: pintar uma peça nunca falha.<br><br>Falar com o cofre é diferente: é pela <b>internet</b>. Pode cair a rede, a Roblox pode estar ocupada, o pedido pode demorar demais. E quando uma linha dá erro, o Roblox <b>para o script inteiro</b> ali.<br><br><span class=ui>pcall</span> quer dizer <i>chamada protegida</i>. Ele embrulha a linha perigosa e diz: <i>“tenta; se der errado, não quebre tudo — só me avise”</i>.<br><br>Por isso a resposta vem em duas partes: <span class=ui>local deu, guardado = pcall(...)</span>. O <span class=ui>deu</span> é <b>true</b> ou <b>false</b> — se conseguiu falar com o cofre. O <span class=ui>guardado</span> é o que veio de lá.<br><br>E por isso o <span class=ui>if deu and guardado then</span>: só usa o valor se as <b>duas</b> coisas deram certo.",
    ck="Você consegue dizer o que aconteceria com o placar de um jogador se a internet caísse e não houvesse pcall.",
    sos=[("O que aconteceria?","O script pararia na linha do cofre, o <span class=ui>leaderstats</span> ficaria pela metade, e o jogador entraria sem placar nenhum."),
         ("Por que guardado pode ser nada?","Porque na primeira vez que a pessoa joga, não há nada guardado. Aí o <span class=ui>guardado</span> vem vazio e o placar começa em 0, que é o certo.")]),

  dict(n=10, titulo="Faça a moeda", img="aula17/s_moeda_b.jpg", clipe="02_criar_peca.gif",
    corpo="Volte para a aba <span class=ui>Place1</span>. <span class=ui>Parte</span> → <span class=ui>Âncora</span>.<br><br><b>size</b> = <b>2, 2, 2</b>, <b>position</b> = <b>0, 3, -8</b>, pintada de <b>amarelo</b>, renomeada para <b>Moeda</b>.",
    ck="Um cubo amarelo flutuando à frente de onde você nasce.",
    sos=[("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete."),
         ("A moeda cai","Faltou a <span class=ui>Âncora</span>.")]),

  dict(n=11, titulo="Ponha o script da moeda", img="aula17/p_moeda_pronto.jpg", clipe=None,
    codigo=MOEDA, auto=(8, 9),
    corpo="Clique na <span class=ui>Moeda</span>, clique no <b>+</b>, escolha <span class=ui>Script</span>, apague a linha pronta e escreva:",
    depois="É o mesmo código da Aula 5, sem uma linha sequer de diferença. O que mudou não foi a moeda — foi o placar, que agora vem do cofre.",
    ck="Nenhum risco vermelho.",
    sos=[("Diz que leaderstats não existe","O script do cofre não rodou. Volte no passo 6 e confira se ele está no <span class=ui>ServerScriptService</span> e sem risco vermelho."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=12, titulo="Faça cinco moedas", img="aula17/p_cena.jpg", clipe=None,
    corpo="Botão direito na <span class=ui>Moeda</span> → <span class=ui>Duplicar</span>, quatro vezes.<br><br>Mude a <b>position</b> de cada cópia: <b>4, 3, -8</b> · <b>-4, 3, -8</b> · <b>8, 3, -8</b> · <b>-8, 3, -8</b>.",
    ck="Cinco cubos amarelos em fila.",
    sos=[("Ficaram uma dentro da outra","Mude a position de cada uma. O primeiro número é para os lados."),
         ("Uma cópia não funciona","Você duplicou a peça errada. Apague e duplique a <span class=ui>Moeda</span> que tem o Script dentro.")]),

  dict(n=13, titulo="Jogue e pegue as cinco", img="aula17/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Aperte o <b>▶</b> e pegue todas as moedas. O placar vai a <b>5</b>.<br><br>Agora <b>pare o jogo</b> no quadrado vermelho. É a hora da verdade do próximo passo.",
    ck="O placar chegou a 5 e você parou o jogo.",
    sos=[("Não aparece o placar","Confira o nome <b>leaderstats</b>, tudo minúsculo, no script do cofre."),
         ("Deu erro vermelho falando de DataStore","Quase certo que é a chave do passo 4. Volte lá e confira se ela ficou ligada e se você clicou em Salvar.")]),

  dict(n=14, titulo="A prova: jogue de novo", img="aula17/s_jogar2_b.jpg", clipe=None,
    corpo="Aperte o <b>▶</b> outra vez, sem mexer em nada.<br><br>Olhe o placar <b>antes</b> de pegar qualquer moeda.",
    ck="O placar já começa em <b>5</b>. As moedas voltaram porque o mundo recomeça — mas o número não, porque ele veio do cofre.",
    sos=[("Começou em 0","Três conferências, nesta ordem: (1) a chave do passo 4 está ligada? (2) o jogo foi publicado no passo 3? (3) o <span class=ui>PlayerRemoving</span> está no fim do <b>mesmo</b> script?"),
         ("Começou em 0 e não deu erro nenhum","É a assinatura da chave desligada: sem ela o cofre não reclama, só devolve vazio."),
         ("Começou em 5 mas depois voltou a 0","Você mudou o nome do cofre no <span class=ui>GetDataStore</span>. O nome é a etiqueta da gaveta.")]),

  dict(n=15, titulo="Entenda por que é preciso SAIR para salvar", img="aula17/p_salva_pronto.jpg", clipe=None,
    corpo="Repare no que aconteceu: o número só foi guardado quando você <b>parou</b> o jogo — porque parar, para o Roblox, é o jogador saindo, e é aí que o <span class=ui>PlayerRemoving</span> acontece.<br><br>Isso tem um risco de verdade: se o jogo cair, ou se a internet do jogador morrer no meio, ele <b>nunca sai direito</b> — e o progresso da última partida se perde.<br><br>Jogos grandes resolvem isso salvando <b>de tempos em tempos</b>, não só na saída. Você já sabe fazer isso: é um <span class=ui>while true do</span> com <span class=ui>task.wait(60)</span>, da Aula 7.",
    ck="Você consegue dizer por que salvar só na saída não é suficiente num jogo de verdade.",
    sos=[("Quero fazer o salvamento de minuto em minuto","Ótimo desafio para casa. Cuidado com um detalhe: o cofre tem limite de quantas vezes por minuto dá para escrever. De 60 em 60 segundos está seguro.")]),

  dict(n=16, titulo="Guarde também o recorde de tempo", img="aula17/p_dois_pronto.jpg", clipe=None,
    corpo="Um cofre pode guardar <b>mais de uma coisa</b>. O jeito mais simples é usar uma segunda gaveta.<br><br>No começo do script, acrescente uma linha:<br><span class=ui>local cofreTempo = DataStoreService:GetDataStore(\"MeuTempo\")</span><br><br>E repita o desenho que você já tem: um <span class=ui>StringValue</span> chamado <b>Tempo</b> dentro do leaderstats, um <span class=ui>pcall</span> com <span class=ui>cofreTempo:GetAsync</span> ao entrar, e outro com <span class=ui>SetAsync</span> ao sair.<br><br>Se você fez a Aula 16, aproveite o cronômetro dela: agora o recorde sobrevive ao dia seguinte.",
    ck="O placar mostra duas colunas, <b>Moedas</b> e <b>Tempo</b>, e as duas voltam como estavam.",
    sos=[("Posso usar o mesmo cofre para os dois?","Pode, guardando uma tabela — mas é assunto de outro ano. Duas gavetas é mais simples e funciona igual."),
         ("O Tempo não volta","Confira se você escreveu <span class=ui>cofreTempo</span> nos dois lugares: no GetAsync e no SetAsync.")]),

  dict(n=17, titulo="Teste como se fosse outra pessoa", img="aula17/s_jogar3_b.jpg", clipe=None,
    corpo="Jogue, pare e jogue de novo várias vezes, fazendo coisas diferentes:<br><br>• pegar moedas e parar <b>na hora</b>, sem esperar;<br>• entrar e sair sem pegar nada;<br>• pegar tudo, morrer, e sair.<br><br>Anote se em alguma delas o número se perdeu.",
    ck="Você testou pelo menos três idas e voltas e o número bateu em todas.",
    sos=[("Numa delas perdi o progresso","Anote exatamente o que você fez antes de sair — essa é a informação que vale. Quase sempre é sair rápido demais depois de pegar a última moeda.")]),

  dict(n=18, titulo="Jogue de VERDADE, pelo site", img="aula17/s_site_b.jpg", clipe=None,
    corpo="O teste definitivo não é no Studio: é no jogo publicado.<br><br><b>1.</b> Publique de novo: <span class=ui>Arquivo → Publicar na Roblox</span> (não pede nome desta vez, só atualiza).<br><b>2.</b> No site, deixe o jogo <b>Público</b> (Aula 4, passo 15).<br><b>3.</b> Abra o link, jogue, pegue moedas, <b>feche o jogo</b> e abra de novo.",
    ck="Você entrou pelo site, pegou moedas, fechou, entrou de novo e o número estava lá.",
    sos=[("Funciona no Studio mas não no site","Ao contrário do normal — no site o cofre funciona <b>sem</b> a chave do passo 4. Se falhou lá, confira se você publicou <b>depois</b> de escrever o código."),
         ("Não consigo abrir pelo site","O jogo ainda está privado. Aula 4, passo 15.")]),

  dict(n=19, titulo="Convide um colega e compare os cofres", img="aula17/p_cena.jpg", clipe=None,
    corpo="Mande o seu link para a pessoa do lado e peça para ela jogar.<br><br>Repare numa coisa importante: <b>o cofre dela é outro</b>. As moedas dela não se misturam com as suas, mesmo sendo o mesmo jogo — porque a chave da gaveta é o <span class=ui>jogador.UserId</span>, que é diferente para cada pessoa.",
    ck="Vocês dois jogaram o mesmo jogo e cada um tem o seu próprio número de moedas.",
    sos=[("As moedas dele apareceram no meu placar","Aí você guardou pelo nome do jogo e não pelo <span class=ui>UserId</span>. Confira as duas linhas do GetAsync e do SetAsync."),
         ("O que é UserId?","É o número da conta da pessoa na Roblox. Não muda nunca, nem se ela trocar de nome — por isso ele serve de chave, e o nome não serviria.")]),

  dict(n=20, titulo="Salve", img="aula17/s_parar_b.jpg", clipe=None,
    corpo="Pare o jogo. <b>Ctrl + S</b> → <span class=ui>Salvar em arquivo</span> → nome <b>cofre</b>.<br><br>Guarde também o <b>link</b> do seu jogo: daqui para a frente ele tem memória, e vale a pena voltar nele.",
    ck="Arquivo salvo e link guardado.",
    sos=[("Pediu para publicar","Escolha <span class=ui>Salvar em arquivo</span>. Publicar você já fez."),
         ("Quero apagar o que está guardado para testar do zero","Troque o nome no <span class=ui>GetDataStore</span> — por exemplo <b>MinhasMoedas2</b>. É uma gaveta nova, vazia.")]),
 ],
}
