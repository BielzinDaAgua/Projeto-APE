from deftest import *

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


