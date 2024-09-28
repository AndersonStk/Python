print(f'\033[1;32m{' LOJAS VOLPPY ':=^40}\033[m')
dinheiro = float(input('Valor dos produtos: R$'))
print('\033[36m-=-\033[m' * 15)
print('''Escolha uma forma de pagamento
[ 1 ] A vista 10% desconto
[ 2 ] A vista cartão 5% desconto
[ 3 ] 2x no cartão sem desconto
[ 4 ] 3x ou mais no cartão 20% de juros''')
print('\033[36m-=-\033[m' * 15)

resposta = int(input('Escolha a forma de pagamento: '))

a_vista = dinheiro - (dinheiro * 10 / 100)
a_vista_cartao = dinheiro - (dinheiro * 5 / 100)
cartao = dinheiro / 2
cartao1 = (dinheiro * 20 / 100) + dinheiro
parcelas = int(input('Em quantas parcelas: '))
valor = cartao1 / parcelas
if resposta == 1:
    print(f'O valor que era R${dinheiro:.2f} agora é R${a_vista:.2f}, teve um desconto de 10% a vista.')
elif resposta == 2:
    print(f'O valor que era R${dinheiro:.2f} agora é R${a_vista_cartao:.2f}, teve um desconto de 5% a vista no cartão.')
elif resposta == 3:
    print(f'O valor que era R${dinheiro:.2f} agora é R${cartao:.2f}, dividido em 2x sem desconto.')
elif resposta >= 4:
    print(f'O valor que era R${dinheiro:.2f} agora é R${valor:.2f}, dividido acima de 3x  com o juros de 20%.')
else:
    print('ERRO 444! TENTE NOVAMENTO...')