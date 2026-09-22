# -*- coding: utf-8 -*-
"""Aula 18 — Projeto livre 2 e mostra.

   As receitas sao IMPORTADAS das aulas 10 a 17, nao copiadas: copia de
   referencia envelhece, e uma pagina que ensina um codigo diferente do que
   a aula original ensina e um defeito que nao aparece em nenhum dos dois
   arquivos."""
from conteudo_a10 import BANDEIRA, LARGADA
from conteudo_a11 import CHEGADA as LETREIRO
from conteudo_a12 import MOEDA as MOEDA_SOM
from conteudo_a13 import ALAVANCA
from conteudo_a14 import VAIVEM, PORTA
from conteudo_a15 import MOLA
from conteudo_a16 import CHEGADA as CRONOMETRO, LARGADA as CRONO_LARGADA, PLACAR as PLACAR_TEMPO
from conteudo_a17 import COFRE, SALVA

SOS_ASPA = ("A aspa saiu errada (Ï, ä, ou duas aspas juntas)","A aspa do teclado brasileiro é <b>tecla muda</b>. Antes de vogal ela vira trema; no fim da linha ela às vezes dobra. O conserto é sempre o mesmo: apague o que saiu errado e digite a aspa <b>seguida da barra de espaço</b>. Sai uma aspa limpa, sem espaço.")
SOS_POPUP = ("Apareceu uma caixinha cinza com sugestões","É o editor tentando adivinhar. Aperte <b>Esc</b> para fechá-la e continue digitando. Se você apertar <b>Enter</b> com ela aberta, ele escreve a sugestão no lugar do que você ia escrever.")
SOS_END = ("Sobraram end a mais","Você digitou os que o editor já tinha escrito. Apague os extras até o código ficar igual ao da aula.")

AULA = {
 "n": 18,
 "slug": "aula18",
 "titulo": "Projeto livre 2 e mostra",
 "subtitulo": "O jogo é seu outra vez — agora com oito receitas novas na mão. Nesta página estão todas, prontas para copiar para o seu mapa.",
 "tempo": "50 minutos",
 "etiqueta": "Aula 18 · projeto livre",
 "fim": "Acabou a Aula 18, e acabou o segundo bloco. Some as duas: você já sabe fazer um jogo que mata, que perdoa, que fala, que toca, que espera você decidir, que se move, que te dá coisas na mão, que conta o tempo e que lembra de você amanhã. Isso é um jogo.",
 "avisos": [
   ("Hoje não tem passo a passo", "As outras aulas mandavam. Esta te dá as peças e você escolhe. Se travar, o quadro laranja de cada receita continua valendo."),
   ("Guarde tempo para a mostra", "Os últimos 15 minutos são para jogar o jogo dos colegas. Não deixe para publicar no fim."),
   ("Antes de digitar", "O <b>passo 2</b> desta aula prepara o editor. Não pule — sem isso o editor escreve linhas que você não pediu."),
   ("Copie do seu próprio caderno", "Todas as receitas abaixo vieram das aulas 10 a 17. Se você guardou os arquivos, pode abrir e copiar de lá."),
 ],
 "passos": [
  dict(n=1, titulo="Abra o Studio e escolha BASEPLATE", img="comum/c01_tela_inicial.jpg", clipe=None,
    corpo="Projeto novo. <b>Role a página para baixo</b> até a fileira <span class=ui>Abrir um modelo</span> e clique no primeiro, o <span class=ui>Baseplate</span>.",
    ck="Abriu o mundo cinza.",
    sos=[("Apareceu uma janelinha de Boas-vindas por cima","Clique em <span class=ui>Voltar ao início</span>, o botão da esquerda — ou no <b>✕</b> do canto."),
         ("Quero continuar um jogo antigo","Pode: <span class=ui>Arquivo → Abrir do arquivo</span> e escolha o que você salvou.")]),

  dict(n=2, titulo="Prepare o editor (uma vez em cada computador)", img="comum/c06_preparar_editor.jpg", clipe=None,
    corpo="Hoje você vai <b>digitar código</b>. O Studio vem com duas ajudas que atrapalham quem está aprendendo: ele sugere linhas inteiras e fecha parênteses e aspas sozinho. Vamos desligar as duas.<br><br>No Windows: <span class=ui>Arquivo → Configurações do Studio</span>. No Mac: <span class=ui>Roblox Studio → Configurações do Studio</span>.<br><br><b>1.</b> Na busca escreva <b>assist</b> e desmarque <span class=ui>Ativar assistente de código</span>.<br><b>2.</b> Apague a busca, escreva <b>fechamento</b> e desmarque <span class=ui>Colchetes de fechamento automáticos</span> e <span class=ui>Aspas de fechamento automáticas</span>.<br><br>Feche a janela.",
    ck="As três caixinhas estão <b>vazias</b>: assistente de código, colchetes e aspas.",
    sos=[("Não acho Configurações do Studio","No Windows é o menu <span class=ui>Arquivo</span>, bem no canto de cima à esquerda da janela."),
         ("Já está tudo desmarcado","Ótimo — este computador já foi preparado. Feche a janela e siga.")]),

  dict(n=3, titulo="Decida o que você vai fazer", img="aula18/p_exemplo.jpg", clipe=None,
    corpo="Cinco minutos, no máximo. Escolha <b>uma</b> destas três formas, ou invente:<br><br><b>Corrida contra o relógio</b> — um percurso cronometrado, com checkpoints. Quem faz o melhor tempo?<br><br><b>Sala de desafios</b> — portas que deslizam, alavancas, uma ferramenta que você precisa achar para abrir a próxima.<br><br><b>Caça com memória</b> — moedas espalhadas que ficam guardadas de um dia para o outro.<br><br>Escreva numa folha em três linhas: <i>o que o jogador faz</i>, <i>o que atrapalha</i>, <i>como ele sabe que ganhou</i>.",
    ck="Você tem as três linhas escritas no papel.",
    sos=[("Não consigo escolher","Comece pela corrida. É a mais rápida de montar e a que mais dá vontade de repetir."),
         ("Quero fazer tudo","Escolha <b>duas</b> receitas, não oito. Jogo pequeno e terminado vale mais que grande e pela metade.")]),

  dict(n=4, titulo="Monte o cenário primeiro, sem código", img="aula18/s_cena_b.jpg", clipe=None,
    corpo="Antes de mais nada, duas coisas que toda aula começa fazendo:<br><br><b>1.</b> Na lista da direita, clique na <b>setinha</b> à esquerda de <span class=ui>Workspace</span> para abrir.<br><b>2.</b> Na linha de cima, clique na aba <span class=ui>Modelo</span> — é só nela que existem <span class=ui>Parte</span>, <span class=ui>Material</span>, <span class=ui>Cor</span> e <span class=ui>Âncora</span>.<br><br>Agora quinze minutos só de blocos: crie, ancore, mude o <b>size</b> e a <b>position</b>, pinte.<br><br><b>Não ponha script nenhum agora.</b> Monte o caminho todo primeiro, ande por ele no jogo, veja se dá para atravessar.",
    ck="Você consegue atravessar o seu mapa do começo ao fim andando.",
    sos=[("Não acho o botão Parte","Você está na aba errada. Clique em <span class=ui>Modelo</span>, entre <span class=ui>Script</span> e <span class=ui>Plugins</span>."),
         ("Minhas peças caem","Faltou <span class=ui>Âncora</span>. Criou, ancorou."),
         ("Perdi uma peça de vista","Clique no nome dela na lista, leve o mouse ao mundo 3D e aperte <b>F</b>.")]),

  dict(n=5, titulo="RECEITA: o checkpoint", img="aula18/r_bandeira.jpg", clipe=None,
    codigo=BANDEIRA, auto=(7, 8),
    corpo="Uma <span class=ui>SpawnLocation</span> (pelo <b>+</b> do Workspace, buscando <b>spawn</b>), verde, com este Script dentro:",
    depois="Da Aula 10. <b>Precisa também</b> da receita do passo 6, senão o Roblox sorteia onde o jogador começa.",
    ck="Depois de tocar a bandeira, morrer te devolve nela.",
    sos=[("Continuo nascendo no começo","Você não encostou na bandeira. Passe por cima dela andando."),
         ("Às vezes começo o jogo na bandeira","Falta a receita do passo 6."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=6, titulo="RECEITA: fixar a largada", img="aula18/r_largada.jpg", clipe=None,
    codigo=LARGADA, auto=(3,),
    corpo="Este vai no <span class=ui>ServerScriptService</span>, não numa peça. Precisa de uma <span class=ui>SpawnLocation</span> chamada exatamente <b>Largada</b>:",
    depois="Da Aula 10. Sem ele, com mais de uma SpawnLocation no mundo, o nascimento de entrada é sorteado.",
    ck="Você sempre começa o jogo na Largada.",
    sos=[("Diz que Largada não existe","O nome da peça na lista tem de ser exatamente <b>Largada</b>, com L maiúsculo."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=7, titulo="RECEITA: o letreiro na tela", img="aula18/r_letreiro.jpg", clipe=None,
    codigo=LETREIRO, auto=(7, 8),
    corpo="Primeiro monte a tela: no <span class=ui>StarterGui</span>, um <span class=ui>ScreenGui</span> chamado <b>Aviso</b>, e dentro dele um <span class=ui>TextLabel</span> chamado <b>Texto</b>, com <span class=ui>TextScaled</span> marcado. Depois, o Script na peça que vai falar:",
    depois="Da Aula 11. Troque o texto entre aspas pelo que você quiser dizer.",
    ck="Ao encostar na peça, o letreiro do alto da tela muda.",
    sos=[("Diz que Aviso não é membro de PlayerGui","Os nomes na lista têm de ser exatamente <b>Aviso</b> e <b>Texto</b>."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=8, titulo="RECEITA: a moeda com som", img="aula18/r_moeda.jpg", clipe=None,
    codigo=MOEDA_SOM, auto=(12, 13),
    corpo="Uma peça amarela com um som da <span class=ui>Caixa de Ferramentas</span> dentro, chamado <b>Ping</b>, e este Script:",
    depois="Da Aula 12. Repare que a moeda some de vista <b>antes</b> de ser apagada: sem isso o som morreria junto com ela.",
    ck="A moeda some, o ping toca, e um segundo depois ela é apagada de verdade.",
    sos=[("Some mas não toca","O som tem de estar <b>dentro</b> da moeda e chamar-se <b>Ping</b>."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=9, titulo="RECEITA: a alavanca de apertar E", img="aula18/r_alavanca.jpg", clipe=None,
    codigo=ALAVANCA, auto=(11,),
    corpo="Uma peça com um <span class=ui>ProximityPrompt</span> dentro (pelo <b>+</b>, buscando <b>proximity</b>), e uma segunda peça chamada exatamente <b>Ponte</b>, que começa com <span class=ui>Transparency</span> 1 e <span class=ui>CanCollide</span> desmarcado:",
    depois="Da Aula 13. Apertar E duas vezes rápido atrapalha — o conserto está no passo 19 daquela aula.",
    ck="Chegando perto aparece o balão; apertando E a ponte aparece por cinco segundos.",
    sos=[("Não aparece balão","O <span class=ui>ProximityPrompt</span> tem de estar dentro da peça, e o <span class=ui>MaxDistance</span> não pode ser 0."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=10, titulo="RECEITA: a plataforma que vai e volta", img="aula18/r_vaivem.jpg", clipe=None,
    codigo=VAIVEM, auto=(),
    corpo="Uma peça <b>ancorada</b>, com este Script dentro. Não precisa de mais nada:",
    depois="Da Aula 14. É o único código do curso sem nenhum <span class=ui>end</span>. O <b>-1</b> quer dizer “para sempre” e o <b>true</b> quer dizer “volte no caminho”.",
    ck="A plataforma desliza de ida e volta sozinha, e leva quem estiver em cima.",
    sos=[("Ela vai e não volta","Faltou o <b>true</b> no fim do TweenInfo."),
         ("Ela vai só uma vez","Faltou o <b>-1</b>."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=11, titulo="RECEITA: a porta que desliza", img="aula18/r_porta.jpg", clipe=None,
    codigo=PORTA, auto=(15,),
    corpo="Uma peça <b>ancorada</b> com um <span class=ui>ProximityPrompt</span> dentro:",
    depois="Da Aula 14. Troque o <span class=ui>Vector3.new(0, 12, 0)</span> por <span class=ui>Vector3.new(14, 0, 0)</span> e ela desliza para o lado em vez de subir.",
    ck="Apertando E a porta sobe deslizando, espera cinco segundos e desce.",
    sos=[("Ela some em vez de deslizar","Você escreveu <span class=ui>Transparency</span> no lugar de <span class=ui>Position</span> dentro das chaves."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=12, titulo="RECEITA: a ferramenta na mão", img="aula18/r_mola.jpg", clipe=None,
    codigo=MOLA, auto=(10, 11),
    corpo="No <span class=ui>StarterPack</span>, um <span class=ui>Tool</span> com uma peça dentro chamada exatamente <b>Handle</b> e <b>desancorada</b>. O Script vai na Tool, irmão do Handle:",
    depois="Da Aula 15. O nome <b>Handle</b> não é escolha sua: é o que o Roblox procura para pôr na mão do boneco.",
    ck="A ferramenta aparece na barra de baixo, vai para a mão com a tecla 1, e clicar faz o boneco pular alto.",
    sos=[("Não aparece na barra","A peça dentro da Tool tem de se chamar <b>Handle</b>, com H maiúsculo."),
         ("Aparece mas não vai para a mão","O Handle está ancorado. Desmarque."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=13, titulo="RECEITA: o cronômetro (parte 1, o placar)", img="aula18/r_crono1.jpg", clipe=None,
    codigo=PLACAR_TEMPO, auto=(10,),
    corpo="Este vai no <span class=ui>ServerScriptService</span>. Repare que é um <span class=ui>StringValue</span>, não IntValue — o tempo tem letra no fim:",
    depois="Da Aula 16. Sem este, as duas receitas seguintes não têm onde escrever.",
    ck="Aparece uma coluna <b>Tempo</b> no placar do canto, mostrando <b>--</b>.",
    sos=[("Não aparece o placar","Confira o nome <b>leaderstats</b>, tudo minúsculo."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=14, titulo="RECEITA: o cronômetro (parte 2, largada e chegada)", img="aula18/r_crono2.jpg", clipe=None,
    codigo=CRONO_LARGADA, auto=(7, 8),
    corpo="Numa faixa chamada <b>Largada</b>, este Script liga o relógio:",
    depois="Da Aula 16. O <span class=ui>SetAttribute</span> é um bilhete colado no jogador — é assim que a chegada, que é outro script, fica sabendo a hora em que você passou aqui.",
    ck="Passar pela faixa não mostra nada ainda — o relógio está correndo por baixo.",
    sos=[("Por que não uma variável normal?","Porque largada e chegada são scripts diferentes: um não enxerga a variável do outro."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=15, titulo="RECEITA: o cronômetro (parte 3, a conta)", img="aula18/r_crono3.jpg", clipe=None,
    codigo=CRONOMETRO, auto=(11, 12, 13),
    corpo="Numa faixa chamada <b>Chegada</b>:",
    depois="Da Aula 16. O <span class=ui>math.floor</span> com o <b>* 10</b> e o <b>/ 10</b> é o truque para deixar uma casa depois da vírgula. A última linha rasga o bilhete, para a chegada não contar duas vezes.",
    ck="Ao cruzar a chegada, o placar mostra o seu tempo, como <b>14.3 s</b>.",
    sos=[("O tempo sai zerado","Você tocou na chegada sem passar pela largada."),
         ("Sai com mil casas","Faltou o <span class=ui>math.floor</span>, ou o <b>* 10</b> e o <b>/ 10</b>."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=16, titulo="RECEITA: o cofre (só se você publicar)", img="aula18/r_cofre.jpg", clipe=None,
    codigo=COFRE, auto=(15, 19, 20),
    corpo="Antes de tudo: <b>publique o jogo</b> e ligue <span class=ui>Ativar acesso da API Studio</span> em <span class=ui>Arquivo → Configurações do jogo → Segurança</span>. Sem isso este código roda e não guarda nada, sem reclamar.<br><br>Depois, no <span class=ui>ServerScriptService</span>:",
    depois="Da Aula 17. Falta a metade que <b>guarda</b> — é a receita do passo 17, e ela vai no fim <b>deste mesmo</b> script.",
    ck="O placar de Moedas aparece, e começa com o valor que estava guardado.",
    sos=[("Começa sempre em 0 e não dá erro","É a assinatura da chave desligada: sem ela o cofre não reclama, só devolve vazio."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=17, titulo="RECEITA: o cofre (a metade que guarda)", img="aula18/r_salva.jpg", clipe=None,
    codigo=SALVA, auto=(4, 5),
    corpo="No <b>fim do mesmo script</b> do passo 16, pule uma linha e acrescente:",
    depois="Da Aula 17. O <span class=ui>PlayerRemoving</span> acontece quando o jogador sai — e parar o teste, para o Roblox, é sair.",
    ck="Pegue moedas, pare o jogo, jogue de novo: o número continua lá.",
    sos=[("Diz que cofre não existe","Você pôs isto num script novo. Tem de ir no fim do <b>mesmo</b> script do passo 16."),
         SOS_END, SOS_ASPA, SOS_POPUP]),

  dict(n=18, titulo="Escolha duas receitas e ponha no seu mapa", img="aula18/s_montar_b.jpg", clipe="08_inserir_script.gif",
    corpo="<b>Duas</b>, não oito. Ponha uma, teste, conserte. Só então ponha a outra. Quem põe tudo de uma vez não descobre qual quebrou.<br><br>Volte na receita que você escolheu e faça, na ordem:<br><br><b>1.</b> <b>Monte a peça</b> que a receita descreve — aba <span class=ui>Modelo</span>, <span class=ui>Parte</span>, <span class=ui>Âncora</span>, e depois a cor e o tamanho que ela pede.<br><b>2.</b> <b>Renomeie</b> a peça, se a receita der um nome. <span class=ui>Largada</span>, <span class=ui>Ponte</span>, <span class=ui>Handle</span>, <span class=ui>Aviso</span> e <span class=ui>Texto</span> são levados a sério: o código procura esse nome exato.<br><b>3.</b> Clique na peça na lista, clique no <b>+</b> e escolha <span class=ui>Script</span>.<br><b>4.</b> <b>Apague</b> o <span class=ui>print(\"Hello world!\")</span> (clique no fim da linha e segure <b>Backspace</b>).<br><b>5.</b> <b>Digite o código da receita</b> nesse Script, sem as linhas em cinza e sem Tab.<br><b>6.</b> Volte para a aba <span class=ui>Place1</span>, aperte o <b>▶</b> e teste <b>só essa</b> receita.<br><br><b>Duas exceções:</b> as receitas dos passos 6, 13, 16 e 17 não vão numa peça — vão dentro do <span class=ui>ServerScriptService</span>.",
    ck="As duas funcionam no seu mapa, testadas uma de cada vez — e <b>nenhum Script seu está vazio</b>.",
    sos=[("Pus o Script e não acontece nada","Abra ele com dois cliques na lista. Se estiver <b>vazio</b>, ou ainda com o <span class=ui>print(\"Hello world!\")</span>, é isso: falta digitar o código da receita dentro dele."),
         ("Pus tudo e nada funciona","Apague os scripts, ponha um só, teste. Depois o próximo."),
         ("Deu erro vermelho na tela","Leia o nome que aparece no erro — quase sempre é uma peça com nome diferente do que está no código.")]),

  dict(n=19, titulo="Teste, conserte três coisas e publique", img="aula18/s_jogar_b.jpg", clipe="10_jogar.gif",
    corpo="Aperte o <b>▶</b> e jogue o seu jogo até o fim, sem trapacear. Depois faça de propósito o que um jogador chato faria: pular fora do caminho, apertar E dez vezes, morrer no meio.<br><br>Escolha as <b>três</b> coisas que mais atrapalharam e conserte só elas. Não tente deixar perfeito — tem de publicar hoje.<br><br>Depois: <span class=ui>Arquivo → Publicar na Roblox</span>, e no site deixe o jogo <b>Público</b>.",
    ck="Você tem um link que começa com <b>roblox.com/games/</b> e as três piores coisas estão consertadas.",
    sos=[("Esqueci como publica","Aula 4, passos 9 a 16."),
         ("Já publiquei antes","Então é só <span class=ui>Publicar na Roblox</span> de novo: ele atualiza sem pedir nada.")]),

  dict(n=20, titulo="Troque os links e jogue o dos colegas", img="aula18/p_exemplo.jpg", clipe=None,
    corpo="Últimos 15 minutos, e é a parte mais importante do dia.<br><br><b>1.</b> Mande o seu link para duas pessoas e peça o delas.<br><b>2.</b> Jogue os dois até o fim, se der.<br><b>3.</b> Diga para cada autor <b>uma</b> coisa que você gostou e <b>uma</b> que travou. Uma de cada — não é para fazer lista de defeitos.<br><b>4.</b> Volte ao Studio, conserte <b>uma</b> coisa que te falaram, e publique de novo.<br><br>Guarde o link num lugar que você não perca: ele é seu, e continua no ar depois que o curso acabar.",
    ck="Você jogou dois jogos, deu os dois retornos, consertou uma coisa e publicou a segunda versão.",
    sos=[("O link do colega não abre","O jogo dele ainda está privado. Ele precisa fazer o passo 15 da Aula 4."),
         ("Ninguém achou defeito no meu","Peça para a pessoa jogar de novo tentando quebrar de propósito. Sempre tem.")]),
 ],
}
