# -*- coding: utf-8 -*-
"""Aula 6 — Botão e porta."""

CODIGO = '''local botao = script.Parent
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

AULA = {
 "n": 6, "slug": "aula6",
 "titulo": "Botão e porta",
 "subtitulo": "Você pisa num lugar e outra coisa, longe dali, acontece. É o primeiro script que mexe numa peça que não é a dele.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 6 · uma peça controla outra",
 "fim": "Acabou a Aula 6. Até agora o seu script só mexia na peça onde ele mora. Agora ele alcança qualquer peça do mundo — e é assim que se faz porta, alavanca, armadilha e elevador.",
 "avisos": [
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Projeto novo", "Começa do zero. Você vai fazer duas peças: uma porta e um botão."),
   ("O nome importa", "A porta precisa se chamar exatamente <span class=ui>Porta</span>. O script procura por esse nome — errou a letra, não acha."),
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

  dict(n=3, titulo="Vá para a aba MODELO", img="aula6/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique em <span class=ui>Modelo</span>.",
    ck="Aparecem <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho","Fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=4, titulo="Crie a porta", img="aula6/s_porta_b.jpg", clipe="02_criar_porta.gif",
    corpo="Clique no <b>desenho</b> do botão <span class=ui>Parte</span>. Leve a câmera até ela (clique no nome na lista, mouse no mundo 3D, tecla <b>F</b>, depois <b>S</b> para afastar).",
    ck="A peça está no meio da tela.",
    sos=[("Nada aconteceu","Você clicou na palavra, não no desenho.")]),

  dict(n=5, titulo="Ancore", img="aula6/s_anc_porta_b.jpg", clipe="03_ancorar.gif",
    corpo="Clique em <span class=ui>Âncora</span>. Criou, ancorou.",
    ck="O botão ficou aceso.",
    sos=[("Não sei se ancorou","Busque <b>anchor</b> nas Propriedades.")]),

  dict(n=6, titulo="Deixe com cara de porta", img="aula6/s_tam_porta_b.jpg", clipe="04_tamanho.gif",
    corpo="Na busca das <span class=ui>Propriedades</span> escreva <b>size</b>. Duplo clique no valor, <b>Ctrl + A</b>, escreva <b>12, 14, 1</b> e <b>Enter</b>.<br><br>Alta, larga e fininha — uma parede com buraco de passagem.<br><br>Depois apague a busca.",
    ck="A peça virou uma placa alta e fina, em pé.",
    sos=[("Só mudou um número","Faltou o <b>Ctrl + A</b>."),
         ("Ficou deitada","Você trocou a ordem. São <b>largura, altura, espessura</b>: 12, 14, 1."),
         ("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete.")]),

  dict(n=7, titulo="Pinte de vermelho", img="aula6/s_cor_porta_e.jpg", clipe="05_cor_porta.gif",
    corpo="Setinha do <span class=ui>Cor</span> → hexágono vermelho → clique no <b>círculo do botão Cor</b>.",
    ck="A porta ficou vermelha.",
    sos=[("Não pintou","Falta o clique no círculo do botão Cor.")]),

  dict(n=8, titulo="Chame de PORTA — com P maiúsculo", img="aula6/s_nome_porta_b.jpg", clipe="06_renomear_porta.gif",
    corpo="Botão direito na peça, na lista → <span class=ui>Renomear</span> → <b>Porta</b> → Enter.<br><br><b>Este nome é levado a sério.</b> Daqui a pouco o script vai procurar uma peça chamada exatamente <span class=ui>Porta</span>. Com <i>porta</i> minúsculo, ou <i>Porta1</i>, ele não acha.",
    ck="Na lista está escrito <span class=ui>Porta</span>, com P maiúsculo.",
    sos=[("Escrevi errado","Botão direito → Renomear de novo. Vale a pena conferir letra por letra.")]),

  dict(n=9, titulo="Afaste a porta", img="aula6/p_cena.jpg", clipe=None,
    corpo="Na busca das <span class=ui>Propriedades</span> escreva <b>position</b>. Na primeira linha <span class=ui>Position</span>, duplo clique no valor, <b>Ctrl + A</b>, escreva <b>0, 7, -20</b> e <b>Enter</b>.<br><br>Isso põe a porta a vinte passos de distância do lugar onde você nasce.",
    ck="A porta pulou para longe, e você continua vendo a plataforma clara de nascimento.",
    sos=[("Aparecem três linhas Position","Use a <b>primeira</b>, a que está embaixo de <span class=ui>CFrame</span>."),
         ("A porta sumiu da tela","Ela foi para longe mesmo. Clique nela na lista e aperte <b>F</b>, depois <b>S</b> algumas vezes."),
         ("Ela ficou enterrada no chão","O número do meio é a altura. Aumente: <b>0, 7, -20</b>."),
         ("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete.")]),

  dict(n=10, titulo="Crie o botão", img="aula6/s_botao_b.jpg", clipe="07_criar_botao.gif",
    corpo="Clique de novo no <b>desenho</b> do <span class=ui>Parte</span>. Ancore.<br><br>Depois, pelas <span class=ui>Propriedades</span>: <b>size</b> = <b>5, 1, 5</b> e <b>position</b> = <b>0, 0.5, -8</b>.<br><br>Fica uma plaquinha baixa no chão, entre você e a porta.",
    ck="Tem uma peça baixa e quadrada no caminho, e a porta vermelha mais adiante.",
    sos=[("A peça nova ficou dentro da porta","Confira o position: <b>0, 0.5, -8</b>. O -8 é mais perto que o -20 da porta."),
         ("Esqueci de ancorar","Clique nela e em <span class=ui>Âncora</span>. Botão que cai não funciona.")]),

  dict(n=11, titulo="Pinte o botão de verde", img="aula6/s_cor_botao_e.jpg", clipe="08_cor_botao.gif",
    corpo="Mesma coisa: setinha do <span class=ui>Cor</span> → verde → círculo do botão Cor.<br><br>Verde porque ele convida a pisar.",
    ck="A plaquinha ficou verde.",
    sos=[("Pintei a porta sem querer","<b>Ctrl + Z</b>, clique na peça certa e repita.")]),

  dict(n=12, titulo="Chame de BOTAO", img="aula6/s_nome_botao_b.jpg", clipe=None,
    corpo="Botão direito → <span class=ui>Renomear</span> → <b>Botao</b> (sem acento) → Enter.<br><br>Sem acento porque nome de peça com acento dá problema em algumas partes do Roblox. Fica a dica para a vida.",
    ck="Na lista estão os dois: <span class=ui>Porta</span> e <span class=ui>Botao</span>.",
    sos=[("Posso pôr acento?","Melhor não. Use <b>Botao</b>.")]),

  dict(n=13, titulo="Coloque o Script dentro do BOTÃO", img="aula6/s_script_c.jpg", clipe="09_inserir_script.gif",
    corpo="Clique em <span class=ui>Botao</span> na lista, clique no <b>+</b> e escolha <span class=ui>Script</span>.<br><br><b>Repare bem:</b> o script vai no <b>botão</b>, não na porta. Quem sente o pé é o botão; a porta só obedece.",
    ck="O <span class=ui>Script</span> está para dentro de <span class=ui>Botao</span> e o editor abriu.",
    sos=[("Pus na porta sem querer","Apague com <b>Delete</b> e refaça com o Botao selecionado."),
         ("Não aparece o +","Clique uma vez na linha primeiro.")]),

  dict(n=14, titulo="Escreva o código", img="aula6/p_codigo_pronto.jpg", clipe=None,
    codigo=CODIGO, auto=(12, 13),
    corpo="Apague a linha pronta (clique no fim dela e segure <b>Backspace</b>) e escreva:",
    depois="A novidade está na <b>linha 2</b>. Todo o resto você já viu na aula da lava.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Nenhum risco vermelho.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Risco vermelho na linha 2","Confira: <span class=ui>workspace</span> é minúsculo, e <span class=ui>Porta</span> tem P maiúsculo — igualzinho ao nome que você deu."),
         ("Risco vermelho no fim","Faltou um <span class=ui>end</span> ou o <span class=ui>)</span>."),
         ("Diz que Porta não existe","O nome da peça está diferente do nome no código. Um dos dois está errado."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever."),
         ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço.")]),

  dict(n=15, titulo="Entenda a linha nova", img="aula6/p_codigo_pronto.jpg", clipe=None,
    corpo="<b>local porta = workspace.Porta</b><br><br><span class=ui>workspace</span> é o mundo inteiro — tudo que existe no seu jogo. O ponto quer dizer “de dentro dele”. Então a linha lê assim: <b>“procure no mundo a peça chamada Porta e chame ela de porta”</b>.<br><br>Antes você só usava <span class=ui>script.Parent</span>, que é “a peça onde eu moro”. Agora você consegue pegar <b>qualquer</b> peça, esteja onde estiver.<br><br>É por isso que o nome tem que bater exatamente. O Roblox procura pelo nome, não adivinha.",
    ck="Você consegue explicar a diferença entre <span class=ui>script.Parent</span> e <span class=ui>workspace.Porta</span>.",
    sos=[("E se eu tiver duas peças chamadas Porta?","Ele pega uma só, e você não escolhe qual. Nomes repetidos dão confusão — use Porta1, Porta2.")]),

  dict(n=16, titulo="Jogue e pise no botão", img="aula6/p_porta_aberta.jpg", clipe="10_jogar.gif",
    corpo="Volte para <span class=ui>Place1</span>, aperte o <b>▶</b> e ande até a plaquinha verde.<br><br>No instante em que você pisa, a porta vermelha lá na frente desaparece. Três segundos depois ela volta.",
    ck="A porta sumiu enquanto você estava no botão, e voltou sozinha.",
    sos=[("Piso e não acontece nada","Três conferências: o Script está dentro do <b>Botao</b>? O nome da porta é <b>Porta</b>? Sobrou risco vermelho?"),
         ("A porta some mas eu não consigo atravessar","Faltou <span class=ui>porta.CanCollide = false</span>. Transparente ainda barra."),
         ("A porta some e não volta","Faltam as duas últimas linhas, que desfazem."),
         ("Erro escrito em vermelho na tela","Leia o nome que ele reclama. Quase sempre é a peça Porta com o nome diferente.")]),

  dict(n=17, titulo="Atravesse", img="aula6/p_porta_aberta.jpg", clipe=None,
    corpo="Agora o desafio de verdade: pise no botão e <b>corra</b> até passar pela porta antes dos três segundos acabarem.<br><br>Se não der tempo, é só mudar o <span class=ui>task.wait(3)</span> para <span class=ui>task.wait(5)</span>.",
    ck="Você passou para o outro lado com a porta fechando atrás.",
    sos=[("Impossível, é muito rápido","Aumente o tempo, ou ponha o botão mais perto da porta."),
         ("Fiquei preso dentro da porta","Ela voltou com você em cima. Não é bug, é o jogo. Saia e tente de novo.")]),

  dict(n=18, titulo="Faça o contrário", img="aula6/p_cena.jpg", clipe=None,
    corpo="Troque só os quatro valores das linhas de dentro do <span class=ui>if</span>. Elas ficam assim, nesta ordem:<br><br><span class=ui>porta.Transparency = 0</span><br><span class=ui>porta.CanCollide = true</span><br><span class=ui>task.wait(3)</span><br><span class=ui>porta.Transparency = 1</span><br><span class=ui>porta.CanCollide = false</span><br><br>Ou seja: onde estava <b>1</b> ponha <b>0</b>, onde estava <b>0</b> ponha <b>1</b>, e troque cada <b>false</b> por <b>true</b> e cada <b>true</b> por <b>false</b>.<br><br>Antes de jogar, a porta precisa começar invisível: clique nela na lista e, na busca das <span class=ui>Propriedades</span>, ponha <b>Transparency</b> = <b>1</b> e desmarque <b>CanCollide</b>.<br><br>Agora a porta <b>aparece</b> quando você pisa, em vez de sumir. Vira armadilha.",
    ck="A porta começa invisível e aparece quando você pisa no botão.",
    sos=[("Me perdi nos números","0 é sólida e visível, 1 é invisível. true é “dá para esbarrar”, false é “atravessa”."),
         ("Quero voltar como estava","<b>Ctrl + Z</b> no editor desfaz o que você digitou.")]),

  dict(n=19, titulo="Coloque uma segunda porta", img="aula6/p_cena.jpg", clipe=None,
    corpo="Duplique a porta (botão direito na <span class=ui>Porta</span> da lista → <span class=ui>Duplicar</span>), renomeie a cópia para <b>Porta2</b> e mude a <b>position</b> dela para <b>10, 7, -20</b>, para ficar ao lado da primeira.<br><br>No script, clique no fim da <b>linha 2</b>, aperte <b>Enter</b> e escreva:<br><br><span class=ui>local porta2 = workspace.Porta2</span><br><br>Depois, dentro do <span class=ui>if</span>, escreva uma linha da <span class=ui>porta2</span> embaixo de cada linha da <span class=ui>porta</span> — quatro linhas novas no total:<br><br><span class=ui>porta2.Transparency = 1</span>, <span class=ui>porta2.CanCollide = false</span>, e depois do <span class=ui>task.wait(3)</span> as duas que desfazem: <span class=ui>porta2.Transparency = 0</span> e <span class=ui>porta2.CanCollide = true</span>.<br><br>Um botão, duas portas.",
    ck="As duas portas somem juntas quando você pisa no botão.",
    sos=[("Só uma some","Você esqueceu de repetir alguma linha para a porta2."),
         ("Diz que Porta2 não existe","O nome da cópia na lista tem que ser exatamente <b>Porta2</b>.")]),

  dict(n=20, titulo="Salve", img="aula6/s_parar_b.jpg", clipe=None,
    corpo="<b>Ctrl + S</b> → <b>Salvar em arquivo</b> → nome <b>porta</b>.<br><br>E publique, se quiser: <span class=ui>Arquivo → Publicar na Roblox</span>.",
    ck="Salvou sem erro.",
    sos=[("Esqueci como publica","Aula 4, passo 9.")]),
 ],
}
