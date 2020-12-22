#Procedimento responsável por colocar as perguntas dentro dos quadradinhos. Tem como parâmetro: a pergunta e 4 alternativas.
def pergunta_alternativa (p, a1 ,a2 ,a3 ,a4 ):
  w='_'*63
  y='_'*13
  print(''' {}  
|                                                               |
|{}|
|{}|

 {}    {}    {}    {}
|             |  |             |  |             |  |             |
|{}  |  |{}  |  |{}  |  |{}  | 
|{}|  |{}|  |{}|  |{}|

'''.format(w, p, w, y, y, y, y, a1, a2, a3, a4, y, y, y, y))
#Procedimento que cria um arquivo.txt com os resultados. Tem como parâmetros: nome, que aparece o nome ou a lista de nomes; p que recebe porcentagem.
def arquivos(nome,p):
    arquiz = open('arquiz.txt', 'a')
    titulo="""
_______________________________________________________________________
-----------------------------------------------------------------------
                  RESULTADOS DO JOGO DE QUIZ
-----------------------------------------------------------------------
"""
    arquiz.write(titulo)
    if type(nome)==list:
      for i in range(len(nome)):
        texto = ("{} conhece {}% da turma do 1° Ano de Informática.\n".format(nome[i],p[i]))
        arquiz.write(texto)
    if type(nome)==str:
      texto=("{} conhece {}% da turma do 1° Ano de Informática.\n".format(nome,p))
      arquiz.write(texto)
    linhafim="""
________________________________________________________________________
"""
    printvazio=" \n"
    arquiz.write(linhafim)
    arquiz.write(printvazio)
    arquiz.close()
#Procedimento que traz o ranking caso esteja na opção de competição. Tem como parâmetro a lista com o nome dos jogadores e outra lista com a porcentagem de cada um. Os elementos de cada lista possuem os mesmos índices, visto que foram anexados no mesmo momento de loop.
def calcula_ranking(nomes,porcentagens):
    if porcentagens[0]==porcentagens[1]:
        print("""
_______________________________________________________________________

                        JOGO EMPATADO!
_______________________________________________________________________""")
        for g in range (len(porcentagens)):
            print("""O {}° lugar é de {}, pois foi sorteado/a {}°.
Sabe {}% da turma do 1° ano de Informática.!""".format((g+1), nomes[g], (g+1), porcentagens[g]))
    else:
        indice=[]
        ordem_nomes=[]
        ordem_porcentagem=porcentagens[:]
        ordem_porcentagem.sort()
        ordem_porcentagem.reverse()
        for i in range (len(ordem_porcentagem)):
          indice.append(porcentagens.index(ordem_porcentagem[i]))
        for c in range (len(ordem_porcentagem)):
          ordem_nomes.append(nomes[indice[c]])
        print("-"*30)
        print("-"*10,'RANKING',"-"*10)
        for d in range(len(ordem_nomes)):
           print("""O {}° lugar é de {}, pois sabe {}% do 1° Ano
de informática!""".format((d+1),ordem_nomes[d],ordem_porcentagem[d]))
        print("-"*30)
#Função sem parâmetro que retorna o mascote do jogo ( o robôzinho, Leo).
def mascote():
  return """
                       (>>)
                        ||
                    ____||____
                    |_>__>__>_|
          ::::::::::::::::::::::::::::::::
          ::::::::::::::::::::::::::::::::
          ::::     _____   _____      ::::
       [[[::::     |(O)|   |(O)|      ::::]]]
       [[[::::     ^^^^^   ^^^^^      ::::]]]
       [[[:::: ( )   |       |   ( )  ::::]]]
          ::::        \     /         ::::
          ::::         ¨¨¨¨¨          ::::
          ::::::::::::::::::::::::::::::::
          ::::::::::::::::::::::::::::::::
                      :::::::
          ()        :::::::::::        ()
           ()======:::::::::::::======()
          ()      :::::::::::::::      ()
                 :::::::::::::::::
                :::::::::::::::::::
           .._...../¨¨¨¨¨¨¨¨¨¨¨\....._..
           |::::::::|         |::::::::|
           |::::::::|         |::::::::|
           ===========        ==========                               
  ::::::::::::::::::::::::::::::::::::::::::::::::
  ::::::::::::::::::::::::::::::::::::::::::::::::
  ::::   __________________________________   ::::        
  ::::  |                                  |  ::::         
  ::::  |  010101    01   01  °°  01010101 |  ::::         
  ::::  | 01|   |01  01   01  01     /01/  |  ::::      
  ::::  | 01|   |01  01   01  01   /01/    |  ::::        
  ::::  |  0101\ \   0101001  01  1010101  |  ::::       
  ::::  |__________________________________|  ::::        
  ::::                                        ::::      
  ::::::::::::::::::::::::::::::::::::::::::::::::              
  ::::::::::::::::::::::::::::::::::::::::::::::::"""
#Função (sem parâmetro), que retorna o meu de opções.
def menu ():
  return """
     001      011  01001010  0101    11  10   11
     01 0    0 10  100       101 0   00  10   00
     101 1  0 110  00101001  101  0  10  01   10
     010  10  101  010       010   1 01  00   01
     0101    1010  10101010  001    010  1010000

          _________________________________
          |                               |
          |   (1) INSTRUÇÕES DO JOGO      |
          |_______________________________|
          |                               |
          |   (2) COMPETIÇÃO              |
          |_______________________________|
          |                               |
          |   (3) INICIAR JOGO INDIVIDUAL |
          |_______________________________|
          |                               |
          |   (4) SAIR DO JOGO            |
          |_______________________________|"""
#Função sem parâmetro para retornar o menu.
def niveis ():
  return """
     010    01   /01/  01      01   0101010 (01)  01010101     
     01 01  01         01      01   01           01
     01  01 01   01    01      01   0101010  01    010101
     01   0101   01     01    01    01       01          0
     01   0101   01        01       0101010  01  01010101 

                _________________________________  
                |                               |
                |       (1) FÁCIL               |
                |_______________________________|
                |                               |
                |       (2) INTERMEDIÁRIO       |
                |_______________________________|
                |                               |
                |       (3) DIFÍCIL             |
                |_______________________________|

                                                          """
#Função que avalia a resposta da questão, tem como parâmetro apenas a resposta certa de cada questão.
def avalia_respostas(rcerta):
  #O método .strip() é usado para retirar os espaços que às vezes o usuario coloca sem querer e, portanto, não interferir na hora da avaliação da resposta. Já o .lower() é para deixar minúscula a alternativa, caso o usuario tenha deixado em caixa alta e, assim, nao dá código inválido.
  resposta=str(input("Qual alternativa você escolhe? ")).strip().lower()
  while (resposta!="a")and(resposta!="b")and (resposta!="c")and(resposta!="d"):
    print("CÓDIGO INVÁLIDO!")
    resposta=str(input("Qual alternativa você escolhe? ")).strip().lower()
  if resposta==rcerta:
    return 'Isso mesmo!Você acertou!'
  else:
    return 'Que pena!Você errou...A alternativa certa é "{}"! '.format(rcerta)
#Função que calcula a porcentagem dos acertos e tem como parâmetro a quantidade de acertos, para o cálculo da porcentagem.
def porcentagem(quantidade):
  p=(quantidade*100)/10
  return p
#Função que limpa a tela que está sendo executado o programa, sem parâmetros.
def limpa_tela ():
  import platform #importa funções dessas bibliotecas
  import os
  sistema_operacional=platform.system()#avalia o tipo do sistema operacional através da função platform.system()
  if sistema_operacional=="Windows": 
    return os.system("cls")
  else:
    return os.system("clear")
