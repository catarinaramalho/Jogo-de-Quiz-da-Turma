#Programa Principal
#Funções importadas de bibliotecas do python.
from time import sleep 
from random import randint
#Funções e procedimentos importados do arquivo que fornece suporte ao jogo com funções e procedimentos.
import Funções_ProcedimentosDoQuiz
print(Funções_ProcedimentosDoQuiz.mascote())#Printa o mascote Leo.
sleep(7)#Conta 7 segundos para o novo print.
print(Funções_ProcedimentosDoQuiz.menu())#Printa o Menu.
op=str(input("Qual opção você deseja (1,2,3 ou 4)? ")).strip()
#O while, é usado para avaliar caso o usuário responda errado ou algo inexistente nesse sistema de loop.
while op!='1' and op!='2' and op!='3' and op!='4':
  print("CÓDIGO INVÁLIDO!")
  op=str(input("Qual opção você deseja (1,2,3 ou 4)? ")).strip()
print("Pressione ENTER para continuar!")
enter=input("")
#Esse while (estrutura de repetição)é para certificar que é um ENTER.
while enter!= "":
  print("CÓDIGO INVÁLIDO. Pressione ENTER para continuar!")
  enter=input("")
Funções_ProcedimentosDoQuiz.limpa_tela()#Importa a função do arquivo Funções_ProcedimentosDoQuiz que limpa a tela.
#Existem 4 opções, enquanto a opção (variável->op), for diferente de 4, ou seja, for 3, 2 ou 1, entrará nesse sistema de loop, onde realmente funciona o jogo. Quando op for igual à 4, siginifica que o usuário deseja sair do jogo e, é assim, que aparece os créditos em tela.
while op!="4":
  #A opção 1 é para quando o usuário deseja ver como funciona o jogo. Essa parte é necessária em quase todos os sistemas de games, pois equivale a explicação do jogo, portanto, do tema do quiz.
  if op=="1":
    print("""
    ---------------------------------------------------------------------
                            INSTRUÇÕES DO JOGO
    ---------------------------------------------------------------------
    Prazer, meu nome é Leo! Sou esse robôzinho charmoso que você
    conheceu no início. Você fez bem, antes de querer jogar algo
    é necessário conhecer como ele funciona! Então vamos à um
    BATE-PAPO comigo, onde vou lhe explicar tim-tim por tim-tim.
            
    --> O QUE É O JOGO?
    
    * O QUIZ é um jogo de perguntas e respostas que estimula a
    habilidade lógica dos jogadores. Esse jogo tem como tema:
    A Turma do 1° Ano de Informática do ano 2018. Tendo os
    integrantes da turma como o público alvo, mas podendo ser
    jogado por qualquer um que conheça a turma ou que sinta-se
    desafiado.Esse Quiz pode ser jogado individualmente ou em
    uma competição.
       Existem 3 níveis: Fácil, Intermediário e Difícil. O jogo
    gera um arquivo.txt que registra as porcentagens de acertos
    de cada jogador, podendo ser adicionadas informações, como:
    nível, data, hora em que foi realizada a partida.
    
    --> QUAIS SÃO AS REGRAS?

    1) Toda opção pode ser selecionada através de números ou
    letras, só serão aceitas as opções descritas no jogo,
    caso contrário aparecerá na tela "CÓDIGO INVÁLIDO",
    até a opção digitada for existente no jogo .

    2) Em caso de competição (item 2 do Menu), será um duelo.
    
            2.1) Na segunda rodada, seja honesto com você
            mesmo e não olhe as respostas da jogada anterior.
            
            2.2) Na competição, seleciona o nível a ser jogado.
            A ordem dos jogadores é selecionado pelo próprio
            jogo (BOA SORTE!Isso decide quem acertou
            primeiro a pergunta. É um critério de desempate,
            meu jovem!). Cada jogador tem sua vez e 
            terminado o jogo, mostrará a classificação
            de quem mais conhece a turma.

            2.3)Em caso de empate, o 1° lugar vai para o
            primeiro que respondeu.

    3) O jogo individual do item 3 do Menu, o jogador
    responderá as perguntas e escolherá o nível
    a ser jogado. Ao final, exibirá a porcentagem de quanto
    ele conhece a turma.
    
    4) Quando quiser sair do jogo, é só responder a pergunta
    "Qual opção você deseja?", digitando "4".
    ----------------------------------------------------------------------
    É isso meus caros, desejo a todos um BOM JOGO, e que a força esteja
    sempre com você. Que comecem os joogos!
    ----------------------------------------------------------------------""")
  #A opção 2, é usada em caso de competição.
  if op=="2":
    print("""
    ______________________________________________________________________

                       COMPETIÇÃO DE DOIS JOGADORES 
    ______________________________________________________________________""")
    nomes=[]#Lista com os nomes dos jogadores na ordem do usuário.
    players=[]#Lista com os nomes dos jogadores, na ordem do sorteio (futuro critério de desempate).
    porcentagens_players=[]#Lista com a porcentagem de acerto de cada jogador.
    #As duas estruturas de for a seguir:1) Determina a leitura de nomes, a partir da quantidade de jogadores; 2) Sorteia a ordem dos jogadores na competição através da quantidade de jogadores, caso o jogo empate, o ranking dará a posição de vitória ao que tiver respondido primeiro, por isso a ordem dos jogadores é primordial.
    for jogadores in range (2):
      print("--------------------------------------------------------------")
      nome=str(input("Informe o nome do {}° jogador: ".format(jogadores+1))).strip()
      nomes.append(nome)
      print("--------------------------------------------------------------")
    jásorteados=[]#Lista para englobar as posições dos nomes já sorteados.
    for sorteio_jogadores in range(2):
      s=randint(0,len(nomes)-1)
      while True:
        #Caso o sorteio (0 ou 1) que está na variável "s", já estiver na lista "jásorteados", então será necessário sortear novamente até ser diferente.
        if s in jásorteados:
          s=randint(0,len(nomes)-1)
        else:
          break;
      jásorteados.append(s)
      #players recebe o nome que está na posição s, definida pelo sorteio.
      players.append(nomes[s])
    #Printa com a diferença de 1 segundo cada palavra.
    print('......SOR ')
    sleep(1)
    print('.................TE')
    sleep(1)
    print('............................AN')
    sleep(1)
    print('.....................................DO')
  
    print('''
    --------------------------------------------------------------------------
                              ORDEM DOS JOGADORES
    --------------------------------------------------------------------------''')
    #Essa 3° estrutura de for,repete-se a partir da quantidade de jogadores, pois cada jogador responde 10 perguntas na sua vez. Terminado, virá o ranking. Nesse caso, foi usada outra forma de saber a quantidade de jogadores; a partir do tamanho da lista "players".
    for a in range(len(players)):
      print("O {}° Jogador é {}!".format(a+1,players[a]))
    print(" ")
    #Só aparece a opção de escolha de nível, nas opções 2 e 3 do menu, respectivamente Competição e Jogo Individual.
    print(Funções_ProcedimentosDoQuiz.niveis())#Printa os níveis (função do arquivo de apoio)
    print(" ")
    nivel=str(input("Qual nível você quer jogar? ")).strip()
    #O sistema de avaliador de níveis é o mesmo do menu.
    while True:
      if nivel!="1" and nivel!="2" and nivel!="3":
        print("CÓDIGO INVÁLIDO!")
        nivel=str(input("Qual Nível você quer jogar? ")).strip()
      else:
        break;
    #Esse loop repetirá de acordo com a quantidade de jogadores que está na lista "players", no caso 2.
    for partida in range(len(players)):
      print('''
      -------------------------------------------------------------------------
                                   {}° Jogador ({})
      -------------------------------------------------------------------------
      '''.format(partida+1,players[partida]))
      #A partir da escolha de nível, vem as perguntas. As perguntas são sorteadas e seguem a mesma lógica para o sorteio dos jogadores, onde há uma lista (nesse caso, "sorteados"), onde terá as perguntas que já foram sorteadas. Essas perguntas são identificadas através de números. Caso a pergunta já esteja na lista dos sorteados, o sistema de loop irá sortear (através do randint) novamente. Isso se repete 10 vezes (quantidade de perguntas por nível) com o nível selecionado (Um dos 3).
      if nivel=="1":
        cont=0
        sorteados=[]
        for perguntas in range (10):
          print(" ")
          print("{}° QUESTÃO".format(perguntas+1))
          sorteio=randint(1,13)
          while True:
            if sorteio in sorteados:
              sorteio=randint(1,13)#Cada sorteio avalia 13 perguntas, entretanto pela estrutura de for que repete-se 10 vezes, vão ser selecionadas apenas 10 perguntas.
            else:
              break;
          if sorteio==1:
            p='   Qual pessoa da sala tem o apelido do personagem de tv?      '
            a1='a) Danielly'
            a2='b) Jônatas ' #certo
            a3='c) Luis C. '
            a4='d) Gleysse '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)#Chamada do procediemento responsável por deixar as perguntas em quadrados e retângulos.
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')#Função que retorna o feedback da questão.
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==2:       
            p='   Dentre as alternativas, quem não usa óculos?                '
            a1='a) Patrick ' #certo
            a2='b) Yuri    '
            a3='c) Clézia  ' 
            a4='d) Kennedy '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==3:
            p='   Quem é a mais baixa da sala?                                '
            a1='a) Adriely '
            a2='b) Clézia  '
            a3='c) Isadora '
            a4='d) Alicia  ' #certo
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==4:
            p='   Quem é o(a) mais sorridente?                                '
            a1='a)Carlos M.'
            a2='b) Catarina' #certo
            a3='c) Clézia  ' 
            a4='d) Alisson '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==5:  
            p='   Quem é considerado o "figurante" da sala?                   '
            a1='a) Aniel   '
            a2='b) Luiz F. '
            a3='c) Celson  ' #certo
            a4='d) Arthur  '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==6:
            p='   Quem é conhecido por o nome de um animal de desenho?        '
            a1='a) Luiz C. ' #certo
            a2='b) Geovanny'
            a3='c) Renato  '
            a4='d)Darlisson'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==7: 
            p='   Quem é o "Rei" das piadas?                                  '
            a1='a) Lucas   '
            a2='b) Mateus  '
            a3='c) Alisson ' #certo
            a4='d) Emannuel'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==8:
            p='   Quem desapareceu e por isso ficou conhecido como "Lost boy?"'
            a1='a) Yuri    '
            a2='b) Pedro K.'
            a3='c) Kennedy '
            a4='d) Aniel   ' #certo
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==9:
            p='   Quem ama água?                                              '
            a1='a)M.Letícia' #certo
            a2='b) Mahatma '
            a3='c) Luana   '
            a4='d)Letícia R'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==10:
            p='    Quem é muito sortudo?                                      '
            a1='a) Rubens  '
            a2='b) Aniel   '
            a3='c) Yuri    ' #certo
            a4='d) Kennedy '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==11:
            p='    Onde foi a primeira aula de Redes?                         '
            a1='a)Sala 01  '
            a2='b)Lab.Redes'
            a3='c)Sala 16  ' #certo
            a4='d)L. Info 4'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==12:
            p='    Qual a primeira aula da segunda?                           '
            a1='a) Port    '
            a2='b) Mat     '
            a3='c) Vaga    ' #certo
            a4='d) Geo     '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==13:
            p='    Qual professor(a) apresentou o curso?                      '
            a1='a) Elaine  '#certo
            a2='b) Gurjão  '
            a3='c) Romeryto' 
            a4='d) Glayds  '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          sorteados.append(sorteio)
        print("""Você conhece {}% da turma do 1° Ano de Informática do
nível fácil, pois acertou {} perguntas de 10!""".format(Funções_ProcedimentosDoQuiz.porcentagem(cont),cont))
      elif nivel=="2":
        cont=0
        sorteados=[]
        for perguntas in range (10):
          print(" ")
          print("{}° QUESTÃO".format(perguntas+1))
          sorteio=randint(1,13)
          while True:
            if sorteio in sorteados:
              sorteio=randint(1,13)
            else:
              break;
          if sorteio==1:
            p='   Quem é conhecido(a) pelo nome da cidade?                    '
            a1='a) Gabi.   '
            a2='b) Alicia  '
            a3='c)Leticia A' #certo
            a4='d) Adrielly'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==2:       
            p='  Quem ganhou o primeiro campeonato de vídeo game da sala?     '
            a1='a) Celson  ' #certo
            a2='b) Edvá    '
            a3='c) Rubens  '
            a4='d) Alisson '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==3:
            p='   Quem se mostrou uma/um ótima atriz/ator na prova de Artes?  '
            a1='a) Emmanuel'
            a2='b) Aniel   '
            a3='c) Brenda  ' #certo
            a4='d) Kennedy '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==4:
            p='   Quem é o(a) poeta?                                          '
            a1='a) Brenda  '
            a2='b) Emmanuel'#certo
            a3='c) Isadora ' 
            a4='d) Pedro F.'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==5:  
            p='   Quem come a coxinha por baixo?                              '
            a1='a) Rubens  '
            a2='b) Mahatma '
            a3='c) Yuri    ' 
            a4='d) Clézia  ' #certo
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==6:
            p='   Quem está na lista de chamada, mas nunca apareceu?          '
            a1='a) Ícaro   '
            a2='b) Juliana '
            a3='c) Ismael  ' #certo
            a4='d) Júlia   ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)    
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==7: 
            p='   Quem destas pessoas já teve o cabelo roxo?                  '
            a1='a) Luana   ' #certo 
            a2='b)LeticiaA.'
            a3='c) Isadora ' 
            a4='d) Alicia  '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==8:
            p='  Quais são as iniciais das pessoas que tem nomes de políticos?'
            a1='a) L e P   ' 
            a2='b) L e K   ' #certo ((L)úcia Mahatma->Mahatma Gandhy (Líder político)e (K)ennedy->presidente dos EUA)
            a3='c) I e G   ' 
            a4='d) K e P   '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==9:
            p='  Quanto(as) pessoa(s) da sala tem os olhos azuis?             '
            a1='a) 3       ' 
            a2='b) 2       '
            a3='c) 1       ' #certo
            a4='d) 0       ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==10:
            p='10)Quantas meninas tem o cabelo cacheado?                      '
            a1='a) 9       '
            a2='b) 10      ' #certo
            a3='c) 12      ' 
            a4='d) 5       ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==11:
            p='   Quantas pessoas moram em outras cidades?                    '
            a1='a)17       ' #certo
            a2='b)18       ' 
            a3='c)16       ' 
            a4='d)24       ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==12:
            p='   Quantas pessoas pessoas tem a bolsa bege no Grupo A?        '
            a1='a)2        ' 
            a2='b)4        '#certo 
            a3='c)5        ' 
            a4='d)3        ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==13:
            p='   Quantas pessoas fazem condicionamento físico?               '
            a1='a)15       ' 
            a2='b)14       '#certo 
            a3='c)16       ' 
            a4='d)18       ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          sorteados.append(sorteio)
        print("""Você conhece {}% da turma do 1° Ano de Informática do nível
Intermediário, pois acertou {} perguntas de 10!""".format(Funções_ProcedimentosDoQuiz.porcentagem(cont),cont))
      else:
        sorteados=[]
        cont=0
        for perguntas in range (10):
          print(" ")
          print("{}° QUESTÃO".format(perguntas+1))
          sorteio=randint(1,13)
          while True:
            if sorteio in sorteados:
              sorteio=randint(1,13)
            else:
              break;
          if sorteio==1:
            p='   De quem são as expressões "Dale boy" e "Tampa meu irmão"?   '
            a1='a) E & H   '
            a2='b) G & g   '
            a3='c) H & E   ' #certo(Heleno e Emmanuel)
            a4='d) H & A   '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==2:       
            p='   Quem quebrou a carteirinha do ônibus no início do ano?      '
            a1='a) Geovana '
            a2='b) Alisson '
            a3='c) Isadora ' #certo
            a4='d) Celson  '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==3:
            p='   Quais inciais de quem foi até a semifinal da ONHB?          '
            a1='a)J,I,M,T,C'#Certo(Jônatas, Isadora, Mika, Thaynara e Catarina)
            a2='b)J,M.L,L,Y'
            a3='c)Y,J,C,T,M' 
            a4='d)K,I,G,C,L'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==4:
            p='   Quem teve o nome em duas chamadas?                          '
            a1='a)Vinícius '
            a2='b) Gabriela'
            a3='c) Jônatas ' #certo
            a4='d) Ismael  ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==5:  
            p='   Geralmente, quantas pessoas usam o casaco da GAP?           '
            a1='a) 1       '
            a2='b) 2       ' #certo
            a3='c) 3       ' 
            a4='d) 0       ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4) 
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==6:
            p='  Quem tem uma cicatriz no pé, devido um acidente de bike?     '
            a1='a) Mika    '
            a2='b) Geovana ' #certo
            a3='c) Gleysse ' 
            a4='d)MªLetícia' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)   
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==7: 
            p='Qual das pessoas tem o sobrenome "Rêgo"?                       '
            a1='a) Kennedy ' #certo 
            a2='b) Geovany '
            a3='c) Luis C. ' 
            a4='d) Adrielly' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==8:
            p='  Quantas pessoas tem o sobrenome "Santos"?                    '
            a1='a) 4       '
            a2='b) 5       '
            a3='c) 8       ' 
            a4='d) 12      ' #certo
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==9:
            p='   Quem das pessoas tem a matrícula terminada em "77"?         '
            a1='a) Heleno  '
            a2='b) Patrick '
            a3='c) Gleysse ' #certo
            a4='d) Luana   ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==10:
            p='   Quem teve  óculos "cirurgiado"?                             '
            a1='a)Yuri     '
            a2='b)L. Felipe' #certo
            a3='c)Kennedy  ' 
            a4='d)Mateus   ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==11:
            p='   Quem fazia parte do semáforo no começo do ano?              '
            a1='a)J,Y e L  ' #certo (Jônatas, Yuri, Lucas)
            a2='b)P,R e E  ' 
            a3='c)W,L e D  ' 
            a4='d)G,L e C  ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==12:
            p=' Qual matéria a turma tem a maior média?                       '
            a1='a)Física   ' 
            a2='b)Artes    ' 
            a3='c)Português' 
            a4='d)Química  '#certo 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==13:
            p=' Quem da sala faz/fez curso de Inglês?                         '
            a1='a)J,Y e L  ' 
            a2='b)C,R e E  ' 
            a3='c)W,L e D  ' 
            a4='d)A,L e C  ' #certo
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          sorteados.append(sorteio)
        print(" ")
        print("""Você conhece {}% da turma do 1° Ano de Informática do nível
difícil, pois acertou {} perguntas de 10!""".format(Funções_ProcedimentosDoQuiz.porcentagem(cont),cont))
        print(" ")
      print("Pressione ENTER para continuar!")
      enter=input("")
      while enter!= "":
        print("CÓDIGO INVÁLIDO. Pressione ENTER para continuar!")
        enter=input("")
      Funções_ProcedimentosDoQuiz.limpa_tela()#Função de limpa tela importada do arquivo de suporte do jogo.
      pct=Funções_ProcedimentosDoQuiz.porcentagem(cont)#Função de calculo de porcentagem importada do arquivo de suporte do jogo.
      porcentagens_players.append(pct)#A lista de porcentagens dos jogadores adiciona a porcentagem do jogador da partida em questão.
    #Chamada do procediemento que traz o ranking.
    Funções_ProcedimentosDoQuiz.calcula_ranking(players,porcentagens_players)
    #Chamada do procedimento que cria o arquivo.txt.
    Funções_ProcedimentosDoQuiz.arquivos(players,porcentagens_players)
    print("--------------------------------------------------------------")
    print("""Arquivo.txt gerado com sucesso!Confira os resultados
em texto, na pasta em que se encontra esse jogo!""")
    print("--------------------------------------------------------------")
  #Se a opção 3 for escolhida, a lógica de sorteio de perguntas, porcentagens e  escolha de níveis é a mesma do da Competição. Contudo, ao invés de repetir em um sistema de for determinado pela quantidade de jogadores, se repete apenas 1 vez, afinal é apenas 1 jogador.
  if op=="3":
    #O .strip() é utilizado para cortar espaços, caso o usuário dê espaços antes e depois da digitação de seu nome.
    print("--------------------------------------------------------------")
    nome=str(input(" Informe seu nome: ")).strip()
    print("--------------------------------------------------------------")
    cont=0
    usuario="S"
    while usuario=="S":
      cont=0
      print(Funções_ProcedimentosDoQuiz.niveis())#Chamada da função que retorna os níveis do arquivo de suporte.
      print(" ")
      nivel=str(input("Qual Nível você quer jogar? ")).strip()
      #Estrutura de repetição que avalia se a opção digitada é válida.
      while True:
        if nivel!="1" and nivel!="2" and nivel!="3":
          print("CÓDIGO INVÁLIDO!")
          nivel=str(input("Qual Nível você quer jogar? ")).strip()
        else:
            break;
      if nivel=="1":
        sorteados=[]
        for perguntas in range (10):
          print(" ")
          print("{}° QUESTÃO".format(perguntas+1))
          sorteio=randint(1,13)
          while True:
            if sorteio in sorteados:
              sorteio=randint(1,13)
            else:
              break;

          if sorteio==1:
            p='   Qual pessoa da sala tem o apelido do personagem de tv?      '
            a1='a) Danielly'
            a2='b) Jônatas ' #certo
            a3='c) Luis C. '
            a4='d) Gleysse '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==2:       
            p='   Dentre as alternativas, quem não usa óculos?                '
            a1='a) Patrick ' #certo
            a2='b) Yuri    '
            a3='c) Clézia  ' 
            a4='d) Kennedy '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==3:
            p='   Quem é a mais baixa da sala?                                '
            a1='a) Adriely '
            a2='b) Clézia  '
            a3='c) Isadora '
            a4='d) Alicia  ' #certo
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==4:
            p='   Quem é o(a) mais sorridente?                                '
            a1='a)Carlos M.'
            a2='b) Catarina' #certo
            a3='c) Clézia  ' 
            a4='d) Alisson '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==5:  
            p='   Quem é considerado o "figurante" da sala?                   '
            a1='a) Aniel   '
            a2='b) Luiz F. '
            a3='c) Celson  ' #certo
            a4='d) Arthur  '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==6:
            p='   Quem é conhecido por o nome de um animal de desenho?        '
            a1='a) Luiz C. ' #certo
            a2='b) Geovanny'
            a3='c) Renato  '
            a4='d)Darlisson'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==7: 
            p='   Quem é o "Rei" das piadas?                                  '
            a1='a) Lucas   '
            a2='b) Mateus  '
            a3='c) Alisson ' #certo
            a4='d) Emmanuel'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==8:
            p='   Quem desapareceu e por isso ficou conhecido como "Lost boy?"'
            a1='a) Yuri    '
            a2='b) Pedro K.'
            a3='c) Kennedy '
            a4='d) Aniel   ' #certo
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==9:
            p='   Quem ama água?                                              '
            a1='a)M.Letícia' #certo
            a2='b) Mahatma '
            a3='c) Luana   '
            a4='d)Letícia R'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==10:
            p='    Quem é muito sortudo?                                      '
            a1='a) Rubens  '
            a2='b) Aniel   '
            a3='c) Yuri    ' #certo
            a4='d) Kennedy '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==11:
            p='    Onde foi a primeira aula de Redes?                         '
            a1='a)Sala 01  '
            a2='b)Lab.Redes'
            a3='c)Sala 16  ' #certo
            a4='d)L. Info 4'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==12:
            p='    Qual a primeira aula da segunda?                           '
            a1='a) Port    '
            a2='b) Mat     '
            a3='c) Vaga    ' #certo
            a4='d) Geo     '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==13:
            p='    Qual professor(a) apresentou o curso?                      '
            a1='a) Elaine  '#certo
            a2='b) Gurjão  '
            a3='c) Romeryto' 
            a4='d) Glayds  '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          sorteados.append(sorteio)
        print("""Você conhece {}% da turma do 1° Ano de Informática do nível
fácil, pois acertou {} perguntas de 10!""".format(Funções_ProcedimentosDoQuiz.porcentagem(cont),cont))
      elif nivel=="2":
        sorteados=[]
        for perguntas in range (10):
          print(" ")
          print("{}° QUESTÃO".format(perguntas+1))
          sorteio=randint(1,13)
          while True:
            if sorteio in sorteados:
              sorteio=randint(1,13)
            else:
              break;
          if sorteio==1:
            p='   Quem é conhecido(a) pelo nome da cidade?                    '
            a1='a) Gabi.   '
            a2='b) Alicia  '
            a3='c)Leticia A' #certo
            a4='d) Adrielly'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==2:       
            p='  Quem ganhou o primeiro campeonato de vídeo game da sala?     '
            a1='a) Celson  ' #certo
            a2='b) Edvá    '
            a3='c) Rubens  '
            a4='d) Alisson '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==3:
            p='   Quem se mostrou uma/um ótima atriz/ator na prova de Artes?  '
            a1='a) Emmanuel'
            a2='b) Aniel   '
            a3='c) Brenda  ' #certo
            a4='d) Kennedy '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==4:
            p='   Quem é o(a) poeta?                                          '
            a1='a) Brenda  '
            a2='b) Emmanuel'#certo
            a3='c) Isadora ' 
            a4='d) Pedro F.'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==5:  
            p='   Quem come a coxinha por baixo?                              '
            a1='a) Rubens  '
            a2='b) Mahatma '
            a3='c) Yuri    ' 
            a4='d) Clézia  ' #certo
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==6:
            p='   Quem está na lista de chamada, mas nunca apareceu?          '
            a1='a) Ícaro   '
            a2='b) Juliana '
            a3='c) Ismael  ' #certo
            a4='d) Júlia   ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)    
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==7: 
            p='   Quem destas pessoas já teve o cabelo roxo?                  '
            a1='a) Luana   ' #certo 
            a2='b)LeticiaA.'
            a3='c) Isadora ' 
            a4='d) Alicia  '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==8:
            p='  Quais são as iniciais das pessoas que tem nomes de políticos?'
            a1='a) L e P   ' 
            a2='b) L e K   ' #certo(Lúcia->Mahatama Gandhy (Líder político), Kennedy-> Kenndy, presisdente dos EUA)
            a3='c) I e G   ' 
            a4='d) K e P   '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
               cont+=1
          if sorteio==9:
            p='  Quanto(as) pessoa(s) da sala tem os olhos azuis?             '
            a1='a) 3       ' 
            a2='b) 2       '
            a3='c) 1       ' #certo
            a4='d) 0       ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==10:
            p='10)Quantas meninas tem o cabelo cacheado?                      '
            a1='a) 9       '
            a2='b) 10      ' #certo
            a3='c) 12      ' 
            a4='d) 5       ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==11:
            p='   Quantas pessoas moram em outras cidades?                    '
            a1='a)17       ' #certo
            a2='b)18       ' 
            a3='c)16       ' 
            a4='d)24       ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==12:
            p='   Quantas pessoas tem a bolsa bege no Grupo A?                '
            a1='a)2        ' 
            a2='b)1        ' 
            a3='c)4        ' #certo
            a4='d)3        ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==13:
            p='   Quantas pessoas fazem condicionamento físico?               '
            a1='a)15       ' 
            a2='b)14       '#certo 
            a3='c)16       ' 
            a4='d)18       ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          sorteados.append(sorteio)
        print("""Você conhece {}% da turma do 1° Ano de Informática do nível
Intermediário, pois acertou {} perguntas de 10!""".format(Funções_ProcedimentosDoQuiz.porcentagem(cont),cont))
      else:
        sorteados=[]
        for perguntas in range (10):
          print(" ")
          print("{}° QUESTÃO".format(perguntas+1))
          sorteio=randint(1,13)
          while True:
            if sorteio in sorteados:
              sorteio=randint(1,13)
            else:
                break;
          if sorteio==1:
            p='   De quem são as expressões "Dale boy" e "Tampa meu irmão"?   '
            a1='a) E & H   '
            a2='b) G & g   '
            a3='c) H & E   ' #certo(Heleno e Emmanuel)
            a4='d) H & A   '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==2:       
            p='   Quem quebrou a carteirinha do ônibus no início do ano?      '
            a1='a) Geovana '
            a2='b) Alisson '
            a3='c) Isadora ' #certo
            a4='d) Celson  '
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==3:
            p='   Quais inciais de quem foi até a semifinal da ONHB?          '
            a1='a)J,I,M,T,C'#Certo (Jônatas, Isadora, Mika, Thaynara e Catarina)
            a2='b)J,M.L,L,Y'
            a3='c)Y,J,C,T,M' 
            a4='d)K,I,G,C,L'
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==4:
            p='   Quem teve o nome em duas chamadas?                          '
            a1='a)Vinícius '
            a2='b) Gabriela'
            a3='c) Jônatas ' #certo
            a4='d) Ismael  ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==5:  
            p='   Geralmente, quantas pessoas usam o casaco da GAP?           '
            a1='a) 1       '
            a2='b) 2       ' #certo
            a3='c) 3       ' 
            a4='d) 0       ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4) 
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==6:
            p='  Quem tem uma cicatriz no pé, devido um acidente de bike?     '
            a1='a) Gleysse '
            a2='b) Geovana ' #certo
            a3='c) Thaynara' 
            a4='d)MªLetícia' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)   
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==7: 
            p='Qual das pessoas tem o sobrenome "Rêgo"?                       '
            a1='a) Kennedy ' #certo 
            a2='b) Geovany '
            a3='c) Luis C. ' 
            a4='d) Adrielly' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==8:
            p='  Quantas pessoas tem o sobrenome "Santos"?                    '
            a1='a) 4       '
            a2='b) 5       '
            a3='c) 8       ' 
            a4='d) 12      ' #certo
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==9:
            p='   Quem das pessoas tem a matrícula terminada em "77"?         '
            a1='a) Heleno  '
            a2='b) Patrick '
            a3='c) Gleysse ' #certo
            a4='d) Luana   ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('c')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==10:
            p='   Quem teve  óculos "cirurgiado"?                             '
            a1='a)Yuri     '
            a2='b)L. Felipe' #certo
            a3='c)Kennedy  ' 
            a4='d)Mateus   ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('b')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==11:
            p='   Quem fazia parte do semáforo no começo do ano?              '
            a1='a)J,Y e L  ' #certo (Jônatas,Yuri e Lucas)
            a2='b)P,R e E  ' 
            a3='c)W,L e D  ' 
            a4='d)G,L e C  ' 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('a')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==12:
            p=' Qual matéria da turma tem a maior média?                      '
            a1='a)Física   ' 
            a2='b)Artes    ' 
            a3='c)Português' 
            a4='d)Química  '#certo 
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          if sorteio==13:
            p=' Quem da sala faz curso de Inglês?                             '
            a1='a)J,Y e L  ' 
            a2='b)C,R e E  ' 
            a3='c)W,L e D  ' 
            a4='d)A,L e C  ' #certo
            Funções_ProcedimentosDoQuiz.pergunta_alternativa(p, a1, a2, a3, a4)
            avaliação=Funções_ProcedimentosDoQuiz.avalia_respostas('d')
            print(avaliação)
            if avaliação=="Isso mesmo!Você acertou!":
              cont+=1
          sorteados.append(sorteio)
        print("""Você conhece {}% da turma do 1° Ano de Informática do nível
difícil, pois acertou {} perguntas de 10!""".format(Funções_ProcedimentosDoQuiz.porcentagem(cont),cont))#Chamada da função que retorna a porcentagem de quanto cada jogador conhece a turma.
      print(" ")
      porcentagem_player=Funções_ProcedimentosDoQuiz.porcentagem(cont)#Chamada da função do arquivo Funções_ProcedimentosDoQuiz que retorna a porcentagem.
      Funções_ProcedimentosDoQuiz.arquivos(nome,porcentagem_player)#Chamada da função que gera arquivos.
      print("--------------------------------------------------------------")
      print("""Arquivo.txt gerado com sucesso!Confira os resultados em texto,
na pasta em que se encontra esse jogo!""")#Mensagem que confirma a geração do arquivo.txt
      print("--------------------------------------------------------------")
      usuario=str(input("Deseja jogar outro nível (s/n)? ")).upper()#Terminada a partida, é perguntado ao usuário se ele deseja jogar outro nível. O sistema de avaliar se a resposta é válida é a mesma usada anteriormente (com sistema de loop, while).
      while True:
        if (usuario!="S") and (usuario!="N"):
          print('CÓDIGO INVÁLIDO!')
          usuario=str(input("Deseja jogar outro nível (s/n)? ")).upper()
        else:
            break;
      if usuario=="S":
        print("Pressione ENTER para continuar!")
        enter=input("")
        while enter!= "":
          print("CÓDIGO INVÁLIDO. Pressione ENTER para continuar!")
          enter=input("")
        Funções_ProcedimentosDoQuiz.limpa_tela()
  #Depois de escolhida opção do menu (1,2 ou 3) nesse sistema de while que aceita opções diferentes de 4 (opção de sair do jogo), retorna o procediemento do menu novamente, para que o usuário possa escolher outras opção. O sistema de avaliação se a resposta é válida segue e mesma lógica dos sistemas anteriores.
  print("Pressione ENTER para continuar!")
  enter=input("")
  while enter!= "":
    print("CÓDIGO INVÁLIDO. Pressione ENTER para continuar!")
    enter=input("")
  Funções_ProcedimentosDoQuiz.limpa_tela()
  print(Funções_ProcedimentosDoQuiz.menu())
  print(" ")
  op=str(input("Qual opção você deseja (1,2,3 ou 4)?")).strip()
  while (op!="1")and(op!="2")and (op!="3")and(op!="4"):
    print("CÓDIGO INVÁLIDO!")
    op=str(input("Qual opção você deseja (1,2,3 ou 4)?")).strip()
  print("Pressione ENTER para continuar!")
  enter=input("")
  while enter!= "":
    print("CÓDIGO INVÁLIDO. Pressione ENTER para continuar!")
    enter=input("")
  Funções_ProcedimentosDoQuiz.limpa_tela()
#Caso o usuário opte por sair do jogo (opção 4), aparece os créditos na tela.
if op=="4":
  print("""
         ____________________________________________________________________
                EU, Leo, agradeço sua participação nesse quiz!
         -------------------------------------------------------------------
                                  CRÉDITOS
         -------------------------------------------------------------------
           Instituto Federal de Educação, Ciência e Tecnologia da Paraíba
                             Campus Campina Grande
                        Curso Integrado em Informática

                                  Orientação:
                        Elaine Cristina Juvino de Araújo
                  Marcos Vinícius Cantidiano Marques de Andrade
                            
                Disciplina: Algoritmos e Lógica de Programação
                        Série: 1° Ano de Informática (único)

                        Equipe desenvolvedora do jogo:

                       -Catarina Ramalho dos Santos
                      -Clézia Mirielly Soares Ribeiro
                       -Geovana Stefani Lopes Bezerra

                         (Meninas Superpoderosas)
         --------------------------------------------------------------------
                                FIM DE JOGO
         ____________________________________________________________________""")
  d=input(" ")
