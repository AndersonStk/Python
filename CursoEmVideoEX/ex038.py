numero = int(input('Primeiro numero: '))
numero1 = int(input('Segundo numero: '))
if numero > numero1:
    print(f'O numero {numero} é o maior.')
elif numero1 > numero:
    print(f'O numero {numero1} é o maior.')
elif numero == numero1:
    print('Os dois numeros são iguais.')