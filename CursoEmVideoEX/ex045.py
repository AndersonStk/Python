from random import randint
from time import sleep
# OPÇÕES DE ESCOLHA
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua escolha: ')) # JOGADOR ESCOLHE
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
# JOGADA DE CADA UM
print('-=' * 15)
print(f'O compuador jogou: {itens[computador]}')
print(f'O jogador jogou: {itens[jogador]}')
print('-=' * 15)
if computador == 0: # COMPUTADOR JOGA PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!!!')
elif computador == 1: # COMPUTADOR JOGA PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!!!')
elif computador == 2: # COMPUTADOR JOGA TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!!!')
