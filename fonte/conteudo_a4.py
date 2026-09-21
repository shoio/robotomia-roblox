# -*- coding: utf-8 -*-
"""Aula 4 — Publicar o seu jogo."""

AULA = {
 "n": 4, "slug": "aula4",
 "titulo": "Publicar o seu jogo",
 "subtitulo": "Hoje o seu jogo sai do seu computador e vai para a Roblox, com nome, descrição e um link que você manda para quem quiser.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 4 · no ar",
 "fim": "Acabou a Aula 4. O seu jogo existe na Roblox de verdade — e a partir de agora, toda vez que você melhorar alguma coisa, é só publicar de novo.",
 "avisos": [
   ("Antes da aula", "Você precisa de uma conta Roblox e estar conectado no Studio. Se não estiver, chame o professor no começo da aula — não no meio."),
   ("Projeto novo", "Começa do zero. A primeira metade da aula é construir alguma coisa simples; a segunda é publicar."),
   ("Cuidado com um interruptor", "No passo 9 tem um interruptor que vem ligado e manda os dados do seu jogo para a Roblox treinar inteligência artificial. A gente desliga."),
 ],
 "passos": [
  dict(n=1, titulo="Abra o Studio e escolha BASEPLATE", img="comum/c01_tela_inicial.jpg", clipe=None,
    corpo="Projeto novo. <b>Role a página</b> até <span class=ui>Abrir um modelo</span> e clique no <span class=ui>Baseplate</span>.<br><br>Antes de qualquer coisa, olhe o canto superior direito: tem que aparecer a sua fotinho de perfil. Se aparecer <b>Entrar</b>, você não está conectado — chame o professor agora.",
    ck="Abriu o mundo cinza <b>e</b> a sua foto de perfil está no canto superior direito.",
    sos=[("Aparece Entrar no canto","Clique em <b>Entrar</b> e use a sua conta Roblox. Sem isso não dá para publicar."),
         ("Esqueci a senha","Chame o professor. Não dá para seguir esta aula sem conta."),
         ("Apareceu uma janelinha de Boas-vindas por cima","Clique em <span class=ui>Voltar ao início</span>, o botão da esquerda — ou no <b>✕</b> do canto. Não clique em <span class=ui>Iniciar a introdução</span>.")]),

  dict(n=2, titulo="Vá para a aba MODELO", img="aula4/s_aba_b.jpg", clipe="01_aba_modelo.gif",
    corpo="Clique em <span class=ui>Modelo</span> na linha de abas.",
    ck="Aparecem <span class=ui>Parte</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span> na faixa.",
    sos=[("Não acho","Fica entre <span class=ui>Script</span> e <span class=ui>Plugins</span>.")]),

  dict(n=3, titulo="Crie uma peça", img="aula4/s_criar_b.jpg", clipe="02_criar_peca.gif",
    corpo="Clique no <b>desenho</b> do botão <span class=ui>Parte</span>.",
    ck="Nasceu um bloco e apareceu <span class=ui>Part</span> na lista.",
    sos=[("Nada aconteceu","Você clicou na palavra, não no desenho.")]),

  dict(n=4, titulo="Leve a câmera até ela", img="aula4/p_camera.jpg", clipe=None,
    corpo="Clique em <span class=ui>Part</span> na lista, ponha o mouse sobre o mundo 3D e aperte <b>F</b>. Depois <b>S</b> algumas vezes para afastar.",
    ck="A peça está no meio da tela.",
    sos=[("F não funcionou","O mouse tem que estar sobre o mundo 3D.")]),

  dict(n=5, titulo="Ancore", img="aula4/s_ancora_b.jpg", clipe="03_ancorar.gif",
    corpo="Clique em <span class=ui>Âncora</span>. Criou, ancorou.",
    ck="O botão ficou aceso.",
    sos=[("Não sei se ancorou","Busque <b>anchor</b> nas Propriedades: a caixinha fica marcada.")]),

  dict(n=6, titulo="Faça um palco", img="aula4/s_tam_b.jpg", clipe="04_tamanho.gif",
    corpo="Na busca das <span class=ui>Propriedades</span> escreva <b>size</b>. Clique duas vezes no valor, aperte <b>Ctrl + A</b> e escreva <b>20, 1, 20</b>. <b>Enter</b>.<br><br>Depois apague a busca para o painel voltar ao normal.",
    ck="Virou uma placa larga.",
    sos=[("Só mudou um número","Faltou o <b>Ctrl + A</b> antes de escrever."),
         ("O painel só mostra uma linha","Apague o texto da caixa de busca."),
         ("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete.")]),

  dict(n=7, titulo="Pinte", img="aula4/s_cor_e.jpg", clipe="05_cor.gif",
    corpo="Setinha do <span class=ui>Cor</span> → escolha um hexágono → clique no <b>círculo do botão Cor</b>.<br><br>Escolha a cor que você quiser. É o seu jogo.",
    ck="A placa mudou de cor.",
    sos=[("Não pintou","Falta o clique no círculo do botão Cor.")]),

  dict(n=8, titulo="Dê um nome para a peça", img="aula4/s_nome_b.jpg", clipe="07_renomear.gif",
    corpo="Botão direito na peça, na lista → <span class=ui>Renomear</span> → <b>Palco</b> → Enter.<br><br>Se sobrar tempo, faça mais peças e monte alguma coisa. O que você publicar é o que os outros vão ver.",
    ck="Na lista está <span class=ui>Palco</span>.",
    sos=[("Voltou o nome antigo","Termine com <b>Enter</b>, não Esc.")]),

  dict(n=9, titulo="Abra a janela de publicar", img="aula4/s_pub_b.jpg", clipe="08_publicar.gif",
    corpo="No canto superior esquerdo, clique em <span class=ui>Arquivo</span> e depois em <span class=ui>Publicar na Roblox</span>.<br><br>Abre uma janela com <span class=ui>Nome</span>, <span class=ui>Descrição</span> e alguns interruptores.",
    ck="Apareceu a janela <b>Publicar experiência</b>.",
    sos=[("Não tem menu Arquivo na minha tela","No Windows ele fica no canto de cima à esquerda da janela do Studio. Se não achar, aperte <b>Ctrl + Shift + S</b>."),
         ("Pediu para entrar na conta","Você não está conectado. Entre com a sua conta e repita."),
         ("Abriu 'Salvar em arquivo'","Esse é outro. Você quer <b>Publicar na Roblox</b>, que sobe para a internet.")]),

  dict(n=10, titulo="Escreva o nome e a descrição", img="aula4/d_preenchido.jpg", clipe=None,
    corpo="Clique na <b>caixa branca</b> ao lado de <span class=ui>Nome</span> — não na palavra Nome — e escreva o nome do seu jogo.<br><br>Depois clique na caixa da <span class=ui>Descrição</span> e escreva uma frase dizendo o que é. Isso é o que aparece para quem achar o seu jogo.",
    ck="As duas caixas têm o seu texto, e o contador embaixo do nome mudou de 0.",
    sos=[("Digito e não aparece nada","Você clicou no rótulo. Clique dentro da <b>caixa</b>, à direita dele."),
         ("O nome já vinha escrito","Vinha “Experiência sem título”. Apague com <b>Ctrl + A</b> e escreva o seu."),
         ("Sumiu tudo do meu mundo!","<b>Ctrl + Z</b> várias vezes até tudo voltar. Isso acontece quando o <b>Ctrl + A</b> pega a <b>lista de peças</b> em vez do campo de texto, e aí o Delete apaga as peças. Depois do Ctrl + A, <b>digite</b> os números — nunca aperte Delete.")]),

  dict(n=11, titulo="DESLIGUE o compartilhamento de dados", img="aula4/d_preenchido.jpg", clipe=None,
    corpo="Lá embaixo tem <span class=ui>Compartilhamento de dados</span>, com um interruptor <b>verde (ligado)</b>.<br><br>Ele diz que os dados do seu jogo vão ser usados para treinar a inteligência artificial da Roblox. <b>Clique nele para desligar.</b> Fica cinza.<br><br>Você pode ligar depois se quiser. Desligado é a escolha da escola.",
    ck="O interruptor de <span class=ui>Compartilhamento de dados</span> está <b>cinza</b>.",
    sos=[("Cliquei e não mudou","Clique no interruptor mesmo, aquele riscozinho arredondado, não no texto ao lado."),
         ("E o de Criação em equipe?","Esse pode deixar ligado. Ele salva o seu jogo na nuvem, o que é bom.")]),

  dict(n=12, titulo="Clique em CRIAR", img="aula4/p_publicado.jpg", clipe=None,
    corpo="Clique no botão azul <span class=ui>Criar</span>, no canto de baixo.<br><br>Demora alguns segundos. O Studio sobe o seu mundo para a internet.",
    ck="A janela fechou sozinha <b>e</b> o nome da aba lá em cima mudou — não é mais <span class=ui>Place1</span>, agora tem o seu nome de usuário.",
    sos=[("Deu erro de conexão","Tente de novo. Se insistir, o problema é a internet da escola bloqueando a Roblox — avise o professor."),
         ("Ficou carregando muito tempo","Espere até um minuto. Publicar da primeira vez é lento."),
         ("Cliquei em Cancelar sem querer","Abra <span class=ui>Arquivo → Publicar na Roblox</span> de novo. Nada se perdeu.")]),

  dict(n=13, titulo="Confira que subiu", img="aula4/p_publicado.jpg", clipe=None,
    corpo="Olhe a aba no alto da tela. Antes estava <span class=ui>Place1</span>; agora está escrito <b>Lugar de</b> e o seu nome de usuário.<br><br>Isso quer dizer: este arquivo não vive mais só no computador. Ele tem um endereço na Roblox.",
    ck="A aba tem o seu nome de usuário.",
    sos=[("Continua Place1","A publicação não terminou. Refaça o passo 12.")]),

  dict(n=14, titulo="Abra o seu jogo no site da Roblox", img="aula4/p_publicado.jpg", clipe=None,
    corpo="Agora saia do Studio por um instante. No navegador, entre na sua conta da Roblox e vá direto para <b>create.roblox.com/dashboard/creations</b>. (Pelo menu também dá: <span class=ui>Criar</span>, ou <span class=ui>Create</span> em inglês — mas o nome desse botão muda de tempos em tempos, e o endereço não.)<br><br>Você vai ver a lista das suas experiências. A que você acabou de publicar está lá, com o nome que você escreveu.",
    ck="O seu jogo aparece na lista de experiências do site.",
    sos=[("Não acho a página Criar","O endereço direto é <b>create.roblox.com/dashboard/creations</b>."),
         ("Minha experiência não está na lista","Atualize a página (F5). Pode demorar um minuto."),
         ("A escola bloqueia o site da Roblox","Então faça este passo em casa. O jogo já está publicado de qualquer jeito.")]),

  dict(n=15, titulo="Deixe o jogo público", img="aula4/p_publicado.jpg", clipe=None,
    corpo="No site, clique nos <b>três pontinhos</b> do seu jogo e depois em <b>Configurar</b>.<br><br>Procure <b>Permissões</b> (ou <i>Privacidade</i>) e escolha <b>Público</b>. Salve.<br><br>Enquanto estiver <b>Privado</b>, só você consegue entrar. Público quer dizer que qualquer pessoa com o link joga.",
    ck="A página mostra o seu jogo como <b>Público</b>.",
    sos=[("Não deixa mudar para público","A Roblox exige que a conta tenha e-mail confirmado. Confirme o e-mail e volte."),
         ("Quero que só a turma jogue","Deixe privado e use <b>Convidar</b> para liberar os colegas, um por um.")]),

  dict(n=16, titulo="Copie o link", img="aula4/p_publicado.jpg", clipe=None,
    corpo="Ainda no site, abra a página do seu jogo e copie o endereço que está na barra do navegador.<br><br>É esse link que você manda para um amigo, para a sua mãe, para quem quiser.",
    ck="Você tem um endereço que começa com <b>roblox.com/games/</b>.",
    sos=[("O link não abre para o meu amigo","Ou o jogo ainda está privado, ou ele não tem conta Roblox.")]),

  dict(n=17, titulo="Jogue o jogo de um colega", img="aula4/p_publicado.jpg", clipe=None,
    corpo="Troque o link com a pessoa do lado. Abra o jogo dela, clique em <b>Jogar</b> e entre.<br><br>Repare: você está entrando no jogo de outra pessoa, pela internet, igual a qualquer jogo da Roblox.",
    ck="Você entrou no jogo de um colega e andou lá dentro.",
    sos=[("Fica carregando e não entra","O jogo do colega ainda está privado."),
         ("Abre o Studio em vez do jogo","Você clicou em Editar. Clique no botão verde <b>Jogar</b>.")]),

  dict(n=18, titulo="Mude alguma coisa e publique de novo", img="aula4/s_cor_e.jpg", clipe=None,
    corpo="Volte para o Studio, mude a cor do seu palco, e faça <span class=ui>Arquivo → Publicar na Roblox</span> de novo.<br><br>Desta vez não pede nome nenhum: ele só atualiza o que já está no ar.<br><br><b>É assim daqui para a frente.</b> Toda aula você melhora o jogo e publica de novo.",
    ck="Publicou sem abrir a janela de nome, e o site mostra a mudança quando você entra de novo.",
    sos=[("Abriu a janela pedindo nome de novo","Você clicou em <b>Publicar na Roblox como</b>. Use <b>Publicar na Roblox</b>, sem o “como”."),
         ("O jogo não mudou","Saia do jogo e entre de novo. O jogo já aberto continua com a versão antiga.")]),

  dict(n=19, titulo="Salve no computador também", img="aula4/p_publicado.jpg", clipe=None,
    corpo="<b>Ctrl + S</b> → <b>Salvar em arquivo</b>, com o nome <b>meu jogo</b>.<br><br>Ter os dois é o certo: a cópia na Roblox e a cópia no seu computador.",
    ck="O arquivo está salvo e o jogo está no ar.",
    sos=[("Já não está salvo na nuvem?","Está, mas a cópia no computador é sua e não depende de internet.")]),
 ],
}
