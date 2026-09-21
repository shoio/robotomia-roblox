# -*- coding: utf-8 -*-
"""Aula 7 — O martelo que gira."""

CODIGO = '''local martelo = script.Parent

while true do
\tmartelo.CFrame = martelo.CFrame * CFrame.Angles(0, 0.05, 0)
\ttask.wait(0.03)
end'''

AULA = {
 "n": 7, "slug": "aula7",
 "titulo": "O martelo que gira",
 "subtitulo": "Uma barra que roda sem parar e derruba quem estiver na frente. Hoje o código aprende a repetir.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 7 · repetição",
 "fim": "Acabou a Aula 7. Você escreveu um laço: um pedaço de código que roda para sempre. É o que faz porta automática, esteira, dia e noite — qualquer coisa que se mexe sozinha.",
 "avisos": [
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor: desligar o assistente de código e o fechamento automático. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Projeto novo", "Começa do zero, com uma peça só."),
   ("Cuidado com o laço", "<span class=ui>while true do</span> repete <b>para sempre</b>. Sem o <span class=ui>task.wait</span> lá dentro, o Studio trava. Essa linha não é opcional."),
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

  dict(n=3, titulo="Vá para a aba MODELO", img="aula7/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique em <span class=ui>Modelo</span>.",
    ck="Aparecem <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.",
    sos=[("Não acho","Fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=4, titulo="Crie a peça", img="aula7/s_criar_b.jpg", clipe="02_criar_peca.gif",
    corpo="Clique no <b>desenho</b> do <span class=ui>Parte</span>. Depois clique no nome na lista, ponha o mouse no mundo 3D e aperte <b>F</b>, depois <b>S</b> algumas vezes.",
    ck="A peça está no meio da tela.",
    sos=[("Nada aconteceu","Você clicou na palavra, não no desenho.")]),

  dict(n=5, titulo="Ancore", img="aula7/s_ancora_b.jpg", clipe="03_ancorar.gif",
    corpo="Clique em <span class=ui>Âncora</span>.<br><br>Hoje a âncora é ainda mais importante: a peça vai girar, e peça girando sem âncora sai voando.",
    ck="O botão ficou aceso.",
    sos=[("Não sei se ancorou","Busque <b>anchor</b> nas Propriedades.")]),

  dict(n=6, titulo="Faça uma barra comprida", img="aula7/s_tam_b.jpg", clipe="04_tamanho.gif",
    corpo="Busca das <span class=ui>Propriedades</span> → <b>size</b> → duplo clique no valor → <b>Ctrl + A</b> → <b>26, 1, 2</b> → Enter.<br><br>Depois busque <b>position</b> e ponha <b>0, 4, -14</b>: a barra fica na altura da cintura, uns passos à frente de onde você nasce.",
    ck="Tem uma barra comprida e fina flutuando na sua frente.",
    sos=[("Só mudou um número","Faltou o <b>Ctrl + A</b> antes de escrever."),
         ("A barra ficou no chão","O número do meio é a altura. Use <b>0, 4, -14</b>."),
         ("Aparecem três linhas Position","Use a primeira, embaixo de <span class=ui>CFrame</span>."),
         ("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete.")]),

  dict(n=7, titulo="Pinte", img="aula7/s_cor_e.jpg", clipe="05_cor.gif",
    corpo="Setinha do <span class=ui>Cor</span> → amarelo → clique no <b>círculo do botão Cor</b>.<br><br>Amarelo é cor de aviso. Combina com uma coisa que vai te derrubar.",
    ck="A barra ficou amarela.",
    sos=[("Não pintou","Falta o clique no círculo do botão Cor.")]),

  dict(n=8, titulo="Chame de MARTELO", img="aula7/s_nome_b.jpg", clipe="07_renomear.gif",
    corpo="Botão direito na peça, na lista → <span class=ui>Renomear</span> → <b>Martelo</b> → Enter.",
    ck="Na lista está <span class=ui>Martelo</span>.",
    sos=[("Voltou o nome antigo","Termine com <b>Enter</b>.")]),

  dict(n=9, titulo="Ponha o Script dentro dele", img="aula7/s_script_c.jpg", clipe="08_inserir_script.gif",
    corpo="Clique em <span class=ui>Martelo</span> na lista, clique no <b>+</b> e escolha <span class=ui>Script</span>.",
    ck="O <span class=ui>Script</span> está para dentro de <span class=ui>Martelo</span> e o editor abriu.",
    sos=[("Ficou fora","Arraste-o por cima da palavra <span class=ui>Martelo</span> na lista.")]),

  dict(n=10, titulo="Apague a linha pronta", img="aula7/p_editor_nasce.jpg", clipe=None,
    corpo="Apague o <span class=ui>print(\"Hello world!\")</span> inteiro: clique no fim da linha e segure <b>Backspace</b>.",
    ck="A linha 1 está vazia.",
    sos=[("Sumiu a aba do script","Duplo clique no <span class=ui>Script</span> na lista.")]),

  dict(n=11, titulo="Escreva o laço", img="aula7/p_codigo_pronto.jpg", clipe=None,
    codigo=CODIGO, auto=(6,),
    corpo="Seis linhas. As duas do meio entram para dentro — o editor faz isso sozinho.",
    depois="Repare que este código <b>não tem Touched</b>. Ele não espera nada acontecer — ele age sozinho, o tempo todo.<br><br><b>Não digite as linhas em cinza.</b> O editor escreve os <span class=ui>end</span> sozinho quando você aperta Enter. E <b>não aperte Tab</b> — ele já empurra as linhas para dentro.",
    ck="Nenhum risco vermelho, e o editor desenhou a linha vertical ligando o <span class=ui>while</span> ao <span class=ui>end</span>.",
    sos=[("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula."),
         ("Risco vermelho no fim","Falta o <span class=ui>end</span>. Este laço termina com <b>end</b> sozinho, sem parêntese — diferente dos anteriores."),
         ("Escrevi CFrame errado","São dois maiúsculos: <b>C</b> e <b>F</b>. <span class=ui>CFrame.Angles</span> também."),
         ("O editor completa sozinho","Aperte <b>Esc</b> para dispensar a sugestão."),
         ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")]),

  dict(n=12, titulo="Entenda o laço", img="aula7/p_codigo_pronto.jpg", clipe=None,
    corpo="<b>while true do … end</b> — “<b>enquanto for verdade</b>, faça isto”. E <span class=ui>true</span> é sempre verdade. Então: <b>faça isto para sempre</b>.<br><br>Tudo que estiver entre o <span class=ui>do</span> e o <span class=ui>end</span> se repete sem parar.<br><br><b>martelo.CFrame = martelo.CFrame * CFrame.Angles(0, 0.05, 0)</b> — “pegue onde a peça está e gire um tiquinho”. O <span class=ui>0.05</span> é o tamanho do tiquinho.<br><br><b>task.wait(0.03)</b> — espere trinta milésimos de segundo antes de repetir.",
    ck="Você sabe dizer qual linha faz o martelo girar mais rápido.",
    sos=[("Qual muda a velocidade?","Duas: aumentar o <b>0.05</b> gira mais por vez; diminuir o <b>0.03</b> repete mais vezes por segundo.")]),

  dict(n=13, titulo="Por que o task.wait é obrigatório", img="aula7/p_codigo_pronto.jpg", clipe=None,
    corpo="Um laço <span class=ui>while true</span> sem espera roda <b>milhões de vezes por segundo</b>. O computador não dá conta e o Studio <b>congela</b>.<br><br>O <span class=ui>task.wait</span> é o que dá um respiro. É a linha mais importante do código de hoje, e é a que todo mundo esquece.<br><br><b>Não teste sem ela.</b> Se travar, feche o Studio pelo gerenciador de tarefas e perca tudo o que não salvou.",
    ck="Você tem o <span class=ui>task.wait(0.03)</span> dentro do laço, antes do <span class=ui>end</span>.",
    sos=[("Já travou aqui","Feche o Studio à força e abra de novo. Da próxima vez, salve antes de testar um laço.")]),

  dict(n=14, titulo="Jogue", img="aula7/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Volte para <span class=ui>Place1</span> e aperte o <b>▶</b>.<br><br>A barra amarela começa a girar sozinha, sem você fazer nada.",
    ck="A barra está girando em volta do próprio meio, sem parar.",
    sos=[("Não gira","Confira se o Script está dentro do Martelo e se não sobrou risco vermelho."),
         ("O Studio travou","Faltou o <span class=ui>task.wait</span>. Feche à força e refaça."),
         ("A barra caiu","Faltou ancorar.")]),

  dict(n=15, titulo="Tome uma paulada", img="aula7/s_jogar_c.jpg", clipe=None,
    corpo="Ande até a barra e deixe ela te acertar.<br><br>Você é arremessado. Não precisou de nenhum código para isso: no Roblox, peça sólida que se mexe empurra o que estiver na frente.",
    ck="Você foi jogado longe pela barra.",
    sos=[("Ela atravessa meu boneco","A peça está com <span class=ui>CanCollide</span> desligado. Marque a caixinha nas Propriedades."),
         ("Ela passa por cima da minha cabeça","Diminua a altura: position <b>0, 3, -14</b>.")]),

  dict(n=16, titulo="Mude a velocidade", img="aula7/p_codigo_pronto.jpg", clipe=None,
    corpo="Pare o jogo. Troque o <span class=ui>0.05</span> por <span class=ui>0.2</span> e jogue de novo.<br><br>Depois volte para <span class=ui>0.01</span>. Sinta a diferença.",
    ck="Você testou pelo menos duas velocidades diferentes.",
    sos=[("Ficou rápido demais e não dá para passar","É esse o ponto. Escolha um número que dê para atravessar com esforço."),
         ("Mudei e nada aconteceu","Você mudou com o jogo rodando. Pare, mude, jogue de novo.")]),

  dict(n=17, titulo="Gire para o outro lado", img="aula7/p_codigo_pronto.jpg", clipe=None,
    corpo="Ponha um sinal de menos: <span class=ui>CFrame.Angles(0, -0.05, 0)</span>.<br><br>O martelo passa a girar no sentido contrário.",
    ck="A barra gira para o outro lado.",
    sos=[("Não mudou nada","Você esqueceu de parar e jogar de novo.")]),

  dict(n=18, titulo="Gire em outro eixo", img="aula7/p_codigo_pronto.jpg", clipe=None,
    corpo="Na linha do <span class=ui>CFrame</span>, tire o <b>0.05</b> do meio e ponha no lugar do <b>primeiro</b> número. A linha fica assim:<br><br><span class=ui>martelo.CFrame = martelo.CFrame * CFrame.Angles(0.05, 0, 0)</span><br><br>Agora a barra cambalhota para a frente, em vez de girar como um relógio.<br><br>O primeiro número gira num eixo diferente. Experimente mudar qual dos três números não é zero e veja o que acontece com cada um.",
    ck="Você descobriu, testando, o que cada um dos três números faz.",
    sos=[("Todos parecem iguais","Teste um de cada vez, com os outros dois em zero. A diferença fica clara."),
         ("A peça sumiu","Ela girou para um lugar estranho. Pare o jogo — ela volta ao normal.")]),

  dict(n=19, titulo="Dois martelos", img="aula7/p_cena.jpg", clipe=None,
    corpo="Com o jogo parado: botão direito no <span class=ui>Martelo</span> → <span class=ui>Duplicar</span>. Mude a <b>position</b> da cópia para <b>0, 4, -26</b>.<br><br>A cópia já vem com o script dentro e gira sozinha. Agora são dois obstáculos em fila.",
    ck="Dois martelos girando, um depois do outro.",
    sos=[("Os dois giram igualzinho","Mude o número de um deles para eles ficarem fora de sincronia. Fica bem mais difícil."),
         ("A cópia não gira","Você duplicou antes de pôr o script. Apague e duplique o que tem o Script dentro.")]),

  dict(n=20, titulo="Salve", img="aula7/s_parar_b.jpg", clipe=None,
    corpo="<b>Ctrl + S</b> → <b>Salvar em arquivo</b> → nome <b>martelo</b>.<br><br>Com laço no jogo, salve <b>antes</b> de testar. Sempre.",
    ck="Salvou sem erro.",
    sos=[("Por que antes de testar?","Porque laço mal escrito congela o Studio, e aí só fechando à força.")]),
 ],
}
