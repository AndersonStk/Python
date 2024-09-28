from time import sleep
numero = int(input('Digite um numero: '))
resultado = numero + 1
resultado1 = numero - 1
print(f'Analisando o numero {numero} ... ')
sleep(1.5)
print(f'O numero {numero}, tem como antecessor o numero {resultado1} e como sucessor o numero {resultado}.')