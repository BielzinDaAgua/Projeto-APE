import random

#função para criar matriz que terá as respostas, inicialmente a preenche com '-', em seguida sorteia a localização dos navios e os posiciona na matriz.

#Grupo: Amanda Cruz, Allison, Gabriel e Amanda Maria.

def criar_matriz_respostas(nlin,ncol,n):
  matriz = [[' - ']*ncol for i in range(nlin)]      
                                                                 
  for i in range(n):

    #Sortear navios e posicioná-los apenas se respeitarem os critérios

    l = int(random.randint(0,9))                    
    c = int(random.randint(0,9))

    while(matriz[l][c]=='N' or navios_ao_redor(matriz,l,c)):
      l = int(random.randint(0,9))                    
      c = int(random.randint(0,9))
    matriz[l][c] = 'N'

  return matriz


#função para verificar presença de navios ao redor da posição selecionada. Retorna True se tiver navio ao redor.

def navios_ao_redor(matriz,l,c):

    #verificando se tem navios ao redor das 'bordas' da matriz   
  if((l==0 and c>0 and c<9)):
    if(matriz[l+1][c+1] == 'N' or matriz[l][c+1] == 'N' or matriz[l+1][c] == 'N' or matriz[l+1][c-1] == 'N' or matriz[l][c-1] == 'N'):
      return True

  elif((l==9 and c>0 and c<9)):
    if(matriz[l-1][c-1] == 'N' or matriz[l-1][c+1] == 'N' or matriz[l][c+1] == 'N' or matriz[l][c-1] == 'N' or matriz[l-1][c] == 'N'):
      return True

  elif((l>0 and l<9 and c==0)):      
    if(matriz[l+1][c+1] == 'N' or matriz[l-1][c+1] == 'N' or matriz[l][c+1] == 'N' or matriz[l+1][c] == 'N' or matriz[l-1][c] == 'N'):
      return True

  elif((l>0 and l<9 and c==9)):
    if(matriz[l-1][c-1] == 'N' or matriz[l+1][c-1] == 'N' or matriz[l][c-1] == 'N' or matriz[l+1][c] == 'N' or matriz[l-1][c] == 'N'):
      return True
  
  #verificando se tem navios ao redor das 'quinas'

  elif(l==0 and c==0):
    if(matriz[l+1][c+1] == 'N' or matriz[l][c+1] == 'N' or matriz[l+1][c] == 'N'):
      return True

  elif(l==0 and c==9):
    if(matriz[l+1][c-1] == 'N' or matriz[l][c-1] == 'N' or matriz[l+1][c] == 'N'):
      return True

  elif(l==9 and c==0):
    if(matriz[l-1][c+1] == 'N' or matriz[l][c+1] == 'N' or matriz[l-1][c] == 'N'):
      return True
  
  elif(l==9 and c==9):
    if(matriz[l-1][c-1] == 'N' or matriz[l][c-1] == 'N' or matriz[l-1][c] == 'N'):
      return True

  #verificando se tem navios ao redor de casas do 'meio'

  else:
    if(matriz[l+1][c+1] == 'N' or matriz[l-1][c-1] == 'N' or matriz[l+1][c-1] == 'N' or matriz[l-1][c+1] == 'N' or matriz[l][c+1] == 'N' or matriz[l][c-1] == 'N' or matriz[l+1][c] == 'N' or matriz[l-1][c] == 'N'):
      return True      
  
  return False


#função para criar matriz que será exibição (sem os mostrar as posições dos navios - N)

def criar_matriz_exibir(nlin,ncol):

  matriz_exibir = [[' - ']*ncol for i in range(nlin)]
       
  return matriz_exibir


#função para exibir matriz sem respostas (não mostra os N)

def exibir_matriz_para_jogador(jogador,matriz_exibir):
  print(f'Tabuleiro do jogador {jogador}:')
  nlin = len(matriz_exibir)
  ncol = len(matriz_exibir[0])
  

  for i in range(ncol):
    print(f'{i+1:2}', end=' ')
  print()

  vetor = ['A','B','C','D','E','F','G','H','I','J']

  for i in range(nlin):
    print(vetor[i], end='')
    for j in range(ncol):
        print(f'{matriz_exibir[i][j]:3}', end='')
    print()


#função para exibir matriz com respostas(mostrando os N)

def exiba_matriz_respostas(jogador,matriz):
  print(f'Tabuleiro Resposta do jogador {jogador}:')
  nlin = len(matriz)
  ncol = len(matriz[0])

  for i in range(ncol):
    print(f'{i+1:2}', end=' ')
  print()

  vetor = ['A','B','C','D','E','F','G','H','I','J']

  for i in range(nlin):
    print(vetor[i], end='')
    for j in range(ncol):
      print(f'{matriz[i][j]:3}', end='')
    print()
  return matriz


#verificando o numero de navios afundados, para saber se algum jogador ganhou


def ganhou(matriz_exibir,jogador,n):
  nlin = len(matriz_exibir)                    
  ncol = len(matriz_exibir[0])                 

  cont=0
  for i in range(nlin):                
    for j in range(ncol):             
      if(matriz_exibir[i][j] == 'F'):
        cont+=1
  if(n==cont):                                         
    return True
  else:
    return False


#função para verificar o tiro

def tiro(matriz_resposta,matriz_exibir,jogador,n):
  
  print(f'\nJogador {jogador}, informe as coordenadas do tiro: ')
  print()
  
  exibir_matriz_para_jogador(jogador,matriz_exibir)

  coluna = int(input('Coluna(1 a 10): '))-1
  linha = input('Linha(A a J): ').upper()

  if(linha =='A'):
    linha=0
  elif(linha=='B'):
    linha=1
  elif(linha=='C'):
    linha=2
  elif(linha=='D'):
    linha=3
  elif(linha=='E'):
    linha=4
  elif(linha=='F'):
    linha=5
  elif(linha=='G'):
    linha=6
  elif(linha=='H'):
    linha=7
  elif(linha=='I'):
    linha=8
  elif(linha=='J'):
    linha=9

  while(matriz_resposta[linha][coluna] == 'N'):                  
    print('FOGO!')                                                                            
    matriz_exibir[linha][coluna]='F'
    if(ganhou(matriz_exibir,jogador,n)== False):
      print('Jogue novamente')
      exibir_matriz_para_jogador(jogador,matriz_exibir)

      coluna = int(input('Coluna(1 a 10): '))-1
      linha = input('Linha(A a J): ').upper()

      if(linha =='A'):
        linha=0
      elif(linha=='B'):
        linha=1
      elif(linha=='C'):
        linha=2
      elif(linha=='D'):
        linha=3
      elif(linha=='E'):
        linha=4
      elif(linha=='F'):
        linha=5
      elif(linha=='G'):
        linha=6
      elif(linha=='H'):
        linha=7
      elif(linha=='I'):
        linha=8
      elif(linha=='J'):
        linha=9
 
    elif(ganhou(matriz_exibir,jogador,n)== True):
      print(f'Jogador {jogador} ganhou! Parabéns!')
      return

  if(matriz_resposta[linha][coluna] == ' - '):                  
    print('ÁGUA')
    matriz_exibir[linha][coluna] = 'A'



#PROGRAMA

print('Bem vindo ao jogo Batalha Naval! VAMOS LÁ!')

while True:
  n = int(input('Informe o número de navios(máx:10):'))
  if 10 >= n and 1 <= n:
    break
  print('O número de navios tem que ser entre 1 a 10!')

  
matriz_respostas_jog1 = criar_matriz_respostas(10,10,n)
matriz_exibir_jog1 = criar_matriz_exibir(10,10)

matriz_respostas_jog2 = criar_matriz_respostas(10,10,n)
matriz_exibir_jog2 = criar_matriz_exibir(10,10)

#Se quiser jogar de forma que uma matriz com as respostas seja exibida no início (para verificar o jogo), só remover os comentários a seguir!

#exiba_matriz_respostas(1,matriz_respostas_jog1)
#exibir_matriz_para_jogador(1,matriz_exibir_jog1)

#exiba_matriz_respostas(2,matriz_respostas_jog2)
#exibir_matriz_para_jogador(2,matriz_exibir_jog2)

while(ganhou(matriz_exibir_jog1,1,n)==False and ganhou(matriz_exibir_jog2,2,n)==False):
  #Jogador 1 será o primeiro a jogar:
  tiro(matriz_respostas_jog1,matriz_exibir_jog1,1,n)
  if(ganhou(matriz_exibir_jog1,1,n)==False):
    tiro(matriz_respostas_jog2,matriz_exibir_jog2,2,n)


