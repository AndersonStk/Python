numero = int(input('Escolha um numero: '))
print(f'A tabuada do numero {numero} é:')
print('-='*6)
for n in range(11):
    print(f'{numero} x {n} = {numero * n}')
print('-='*6)
print('Obrigado pela participação!!')