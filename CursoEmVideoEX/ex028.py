from random import randint
from time import sleep
print('Vamos jogar um jogo de advinhação!')
print('Voce tera que escolher um numero entre 0 & 5.')
print('\033[32m-=-\033[m'*20)

while True:
    computador = randint(0, 5)
    jogador = int(input('Qual o numero que estou pensando?\n'))

    if jogador == computador:
     print('\033[1;32mPARABÉNS, VOCÊ GANHOU!\033[m')
    else:
      print('\033[1;31mQUE PENA, VOCÊ PERDEU!\033[m')
      print(f'O numero escolhido foi {computador}')
      sleep(2)

    resposta = input('Deseja continuar? (s/n)')
    if resposta == 'n':
          print('Foi otimo jogar com voce ate aqui! Espero que possamos jogar de novo outro dia.')
          break
    else:
          print('Oba vamos continuar com o nosso joguinho de advinhação!')
          sleep(1.5)


