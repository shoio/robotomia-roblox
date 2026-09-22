# -*- coding: utf-8 -*-
"""Aula 12 — Som.

   O som vem da Caixa de Ferramentas, NAO de um numero de SoundId digitado:
   id de audio sai do ar sem aviso e a aula quebraria sozinha. Pela Caixa o
   aluno tambem aprende a procurar outro quando o que ele usou sumir."""

MOEDA = '''local moeda = script.Parent
local ping = moeda.Ping

moeda.Touched:Connect(function(parte)
\tlocal humano = parte.Parent:FindFirstChild("Humanoid")
\tif humano then
\t\tping:Play()
\t\tmoeda.Transparency = 1
\t\tmoeda.CanCollide = false
\t\ttask.wait(1)
\t\tmoeda:Destroy()
\tend
end)'''

AULA = {
 "n": 12,
 "slug": "aula12",
 "titulo": "Som",
 "subtitulo": "Música de fundo e um “ping” quando você pega a moeda. É o que separa uma maquete de um jogo.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 12 · som",
 "fim": "Acabou a Aula 12. O seu jogo tem trilha e tem resposta: quem joga escuta que acertou. Repare que a música não precisou de uma linha de código — bastou marcar duas caixinhas.",
 "avisos": [
   ("Projeto novo", "Esta aula começa do zero, num projeto novo."),
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Fone ou caixinha", "Se a turma toda tocar som ao mesmo tempo vira barulho. Combine com o professor: fone, ou cada um testa na sua vez."),
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

  dict(n=3, titulo="Abra a lista e vá para a aba MODELO", img="aula12/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique na <b>setinha</b> à esquerda de <span class=ui>Workspace</span> para abrir a lista, e depois na aba <span class=ui>Modelo</span>.",
    ck="A faixa mostra <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho a aba Modelo","Ela fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=4, titulo="Abra a Caixa de Ferramentas", img="aula12/s_caixa_b.jpg", clipe="13_caixa_ferramentas.gif",
    corpo="Aba <span class=ui>Ver</span>, botão <span class=ui>Caixa de Ferramentas</span>.<br><br>Abre um painel na esquerda com coisas prontas da Roblox: modelos, imagens e — o que interessa hoje — <b>áudio</b>.<br><br>É daqui que o som vem. A gente <b>não</b> digita número de som nenhum: número de áudio sai do ar sem avisar, e aí a aula quebraria sozinha daqui a uns meses.",
    ck="Apareceu um painel novo na esquerda da tela, com uma caixa de busca no alto.",
    sos=[("Não acho o botão","Ele está na aba <span class=ui>Ver</span>, não na Modelo. Volte para a Modelo depois."),
         ("Abriu e tapou o mundo 3D","Normal. Você pode fechá-lo no <b>x</b> quando terminar de pegar os sons.")]),

  dict(n=5, titulo="Vá para os ÁUDIOS e ache uma música", img="aula12/s_audio_b.jpg", clipe=None,
    corpo="No alto do painel há uma lista de categorias — <span class=ui>Modelos</span>, <span class=ui>Imagens</span>, <span class=ui>Áudio</span>… Escolha <span class=ui>Áudio</span>.<br><br>Na busca escreva <b>calm music</b> e aperte <b>Enter</b>. Aparecem vários. Passe o mouse em cima de um e clique no <b>▶</b> pequeno para ouvir antes de escolher.",
    ck="Você está vendo uma lista de áudios e conseguiu ouvir pelo menos um.",
    sos=[("Não sai som nenhum","Confira o volume do computador. No Mac, confira também se o Studio não está mudo no mixer."),
         ("A busca não traz nada","Escreva em <b>inglês</b>: <b>music</b>, <b>coin</b>, <b>jump</b>. A biblioteca é em inglês."),
         ("Aparece um cadeado no áudio","Esse não dá para usar. Escolha outro.")]),

  dict(n=6, titulo="Ponha a música no Workspace", img="aula12/s_musica_b.jpg", clipe=None,
    corpo="<b>Primeiro</b> clique em <span class=ui>Workspace</span> na lista da direita. <b>Depois</b> clique no áudio que você escolheu, no painel da esquerda.<br><br>Ele entra <b>dentro</b> do que estava selecionado. Por isso a ordem importa.",
    ck="Dentro de <span class=ui>Workspace</span> apareceu uma linha nova com um ícone de alto-falante.",
    sos=[("Entrou dentro de outra coisa","Arraste-o por cima da palavra <span class=ui>Workspace</span> na lista, ou apague e refaça com o Workspace selecionado."),
         ("Não entrou nada","Clique uma vez só no áudio. Duplo clique às vezes só toca a prévia.")]),

  dict(n=7, titulo="Chame de MUSICA e ligue as duas caixinhas", img="aula12/s_musicaprop_b.jpg", clipe=None,
    corpo="Botão direito nele → <span class=ui>Renomear</span> → <b>Musica</b> (sem acento) → <b>Enter</b>.<br><br>Agora, nas <span class=ui>Propriedades</span>:<br><b>1.</b> busque <b>looped</b> e <b>marque</b> <span class=ui>Looped</span> — quando acabar, recomeça.<br><b>2.</b> apague a busca, escreva <b>playing</b> e <b>marque</b> <span class=ui>Playing</span> — começa tocando.<br><br>Sem acento no nome porque nome de peça com acento dá problema em algumas partes do Roblox.",
    ck="As duas caixinhas, <span class=ui>Looped</span> e <span class=ui>Playing</span>, estão marcadas.",
    sos=[("A música começou a tocar agora, no Studio","É esperado — o <span class=ui>Playing</span> vale já na hora de montar. Desmarque enquanto trabalha, e marque de novo antes de salvar."),
         ("Não acho Looped","Escreva só <b>loop</b> na busca das Propriedades.")]),

  dict(n=8, titulo="Jogue e escute", img="aula12/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Aperte o <b>▶</b>.<br><br>Repare: <b>não escrevemos uma linha de código</b>. Marcar duas caixinhas bastou.",
    ck="A música toca e recomeça sozinha quando acaba.",
    sos=[("Não escuto nada","Confira se o <span class=ui>Playing</span> ficou marcado, e o volume do computador."),
         ("A música está baixa","Nas Propriedades do som, busque <b>volume</b> e ponha <b>1</b>.")]),

  dict(n=9, titulo="Pare o jogo", img="aula12/s_parar_b.jpg", clipe="11_parar.gif",
    corpo="Aperte o <b>quadrado vermelho</b>.",
    ck="Voltou a tela de montar.",
    sos=[("A música continua tocando","Desmarque o <span class=ui>Playing</span> enquanto você monta.")]),

  dict(n=10, titulo="Crie a moeda", img="aula12/s_moeda_b.jpg", clipe="02_criar_peca.gif",
    corpo="Aba <span class=ui>Modelo</span> → <span class=ui>Parte</span> → <span class=ui>Âncora</span>.<br><br>Depois, nas <span class=ui>Propriedades</span>: <b>size</b> = <b>2, 2, 2</b> e <b>position</b> = <b>0, 3, -8</b>. Pinte de <b>amarelo</b> e renomeie para <b>Moeda</b>.",
    ck="Um cubo amarelo flutuando uns passos à frente de onde você nasce.",
    sos=[("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete."),
         ("A moeda cai quando eu jogo","Faltou a <span class=ui>Âncora</span>.")]),

  dict(n=11, titulo="Ponha um “ping” DENTRO da moeda", img="aula12/s_ping_b.jpg", clipe=None,
    corpo="Na Caixa de Ferramentas, aba <span class=ui>Áudio</span>, busque <b>coin</b> e ouça alguns. Escolha um curtinho.<br><br><b>Primeiro</b> clique na <span class=ui>Moeda</span> na lista da direita. <b>Depois</b> clique no áudio.<br><br>Ele tem de entrar <b>dentro</b> da Moeda — assim o som sai <b>de onde a moeda está</b>, e fica mais alto quanto mais perto você chega.",
    ck="Na lista, o som aparece <b>para dentro</b> da <span class=ui>Moeda</span>.",
    sos=[("Entrou no Workspace","Arraste-o por cima da palavra <span class=ui>Moeda</span> na lista."),
         ("Qual a diferença de ficar dentro?","Som dentro de uma peça tem lugar no mundo: ele aumenta quando você se aproxima. Som solto no Workspace toca igual em qualquer canto.")]),

  dict(n=12, titulo="Chame o som de PING", img="aula12/s_pingnome_b.jpg", clipe=None,
    corpo="Botão direito nele → <span class=ui>Renomear</span> → <b>Ping</b> → <b>Enter</b>.<br><br>E <b>não</b> marque o Playing deste: ele só deve tocar quando alguém pegar a moeda.",
    ck="Dentro da Moeda está um som chamado <span class=ui>Ping</span>, com o Playing <b>desmarcado</b>.",
    sos=[("O ping fica tocando sozinho","Você marcou o <span class=ui>Playing</span> dele. Desmarque.")]),

  dict(n=13, titulo="Ponha um Script na moeda", img="aula12/s_script_c.jpg", clipe="08_inserir_script.gif",
    corpo="Clique na <span class=ui>Moeda</span>, clique no <b>+</b> e escolha <span class=ui>Script</span>.",
    ck="Abriu o editor, e dentro da Moeda estão agora o <span class=ui>Ping</span> e o <span class=ui>Script</span>.",
    sos=[("O Script ficou fora da Moeda","Arraste-o por cima da palavra <span class=ui>Moeda</span> na lista.")]),

  dict(n=14, titulo="Escreva o código da moeda", img="aula12/p_codigo_pronto.jpg", clipe=None,
    codigo=MOEDA, auto=(12, 13),
    corpo="Apague a linha pronta (clique no fim dela e segure <b>Backspace</b>) e escreva as treze linhas:",
    depois="<b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Nenhum risco vermelho, e são dois <span class=ui>end</span>, o último com <b>)</b>.",
    sos=[("Diz que Ping não é membro de Moeda","O som dentro da moeda tem de se chamar exatamente <b>Ping</b>, com P maiúsculo."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço."),
         ("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=15, titulo="Entenda por que a moeda demora a sumir", img="aula12/p_codigo_pronto.jpg", clipe=None,
    corpo="Esta é a parte importante da aula de hoje.<br><br>Se o código fosse <span class=ui>ping:Play()</span> e logo <span class=ui>moeda:Destroy()</span>, <b>não sairia som nenhum</b>: o som mora dentro da moeda, e apagar a moeda apaga o som junto, no mesmo instante.<br><br>Por isso a moeda primeiro <b>some de vista</b> — <span class=ui>Transparency = 1</span> e <span class=ui>CanCollide = false</span> —, o som toca por um segundo, e só então ela é apagada de verdade.<br><br>Para o jogador, ela sumiu na hora. Para o código, ela ficou um segundo a mais, invisível, só segurando o som.",
    ck="Você consegue explicar por que não dá para apagar a moeda na hora.",
    sos=[("Por que não pôr o som no Workspace?","Daria, mas aí o som tocaria igual de qualquer distância, e você teria um só para todas as moedas.")]),

  dict(n=16, titulo="Jogue e pegue a moeda", img="aula12/s_jogar2_b.jpg", clipe=None,
    corpo="Aperte o <b>▶</b> e ande até o cubo amarelo.",
    ck="Ao encostar: a moeda some, o <b>ping</b> toca, e a música de fundo continua.",
    sos=[("A moeda some mas não toca nada","Confira o nome <b>Ping</b> e se o som está <b>dentro</b> da Moeda."),
         ("Toca mas a moeda não some","Confira as duas últimas linhas de dentro: <span class=ui>task.wait(1)</span> e <span class=ui>moeda:Destroy()</span>."),
         ("Toca cortado","Aumente o <span class=ui>task.wait(1)</span> para <b>2</b>, ou escolha um som mais curto.")]),

  dict(n=17, titulo="Pare e faça três moedas", img="aula12/p_cena.jpg", clipe=None,
    corpo="Com o jogo <b>parado</b>: botão direito na <span class=ui>Moeda</span> → <span class=ui>Duplicar</span>, duas vezes.<br><br>Mude a <b>position</b> das cópias para <b>4, 3, -8</b> e <b>-4, 3, -8</b>.<br><br>Cada cópia já vem com o som <b>e</b> o script dentro.",
    ck="Três cubos amarelos lado a lado, e todos tocam ao serem pegos.",
    sos=[("A cópia não toca","Você duplicou a peça errada. Apague e duplique a <span class=ui>Moeda</span> que tem o Ping e o Script dentro."),
         ("Ficaram uma dentro da outra","Mude a position de cada uma. O primeiro número é para os lados.")]),

  dict(n=18, titulo="Mexa no volume e na distância", img="aula12/p_cena.jpg", clipe=None,
    corpo="Clique num <span class=ui>Ping</span> e, nas <span class=ui>Propriedades</span>:<br><br><b>Volume</b> — de 0 a 10. Comece em <b>1</b>.<br><b>RollOffMaxDistance</b> — de quantos passos de longe ainda dá para ouvir. Ponha <b>30</b> e depois <b>200</b>, e escute a diferença no jogo.<br><br>Faça o mesmo com a <span class=ui>Musica</span>: música de fundo costuma ficar em volume <b>0.3</b>, baixinha, para não cansar.",
    ck="Você testou pelo menos dois volumes diferentes e ouviu a diferença.",
    sos=[("Não acho RollOff","Escreva <b>roll</b> na busca das Propriedades."),
         ("A música está abafando o ping","Baixe o volume da <span class=ui>Musica</span>, não aumente o do Ping.")]),

  dict(n=19, titulo="Ponha um som de morte", img="aula12/p_cena.jpg", clipe=None,
    corpo="Agora sozinho, com a receita que você já tem:<br><br><b>1.</b> Faça uma lava (<span class=ui>Parte</span>, <span class=ui>Âncora</span>, <b>size</b> 40, 1, 4, <b>position</b> 0, 0.5, -20, vermelha, nome <b>Lava</b>).<br><b>2.</b> Ponha um áudio de queda dentro dela (busque <b>fall</b> ou <b>hurt</b>) e chame de <b>Grito</b>.<br><b>3.</b> Ponha um Script na Lava com o código da Aula 2, e acrescente <span class=ui>lava.Grito:Play()</span> <b>antes</b> da linha do <span class=ui>Health = 0</span>.",
    ck="Ao encostar na lava, toca o som e o boneco morre.",
    sos=[("Não toca","O som tem de estar dentro da <span class=ui>Lava</span> e chamar-se exatamente <b>Grito</b>."),
         ("Toca depois de eu morrer","A linha do <span class=ui>Play()</span> tem de vir <b>antes</b> da linha do Health.")]),

  dict(n=20, titulo="Salve", img="aula12/s_parar_b.jpg", clipe=None,
    corpo="Pare o jogo, confira que a <span class=ui>Musica</span> está com <span class=ui>Playing</span> marcado, e <b>Ctrl + S</b> → <span class=ui>Salvar em arquivo</span> → nome <b>som</b>.",
    ck="Salvou sem erro.",
    sos=[("Publiquei e o som não toca para os outros","Áudio da Caixa de Ferramentas funciona publicado. Se um deles não tocar, é porque saiu do ar: troque por outro."),
         ("Quero um som só meu","Dá para enviar o seu próprio áudio, mas passa por moderação e demora. Fica para outro dia.")]),
 ],
}
