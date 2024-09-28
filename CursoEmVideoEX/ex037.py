numero = int(input('Digite um numero: '))
print('-=-'*15)
print('[ 1 ] converter para BINARIO')
print('[ 2 ] convertar para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
print('-=-'*15)
escolha = int(input('Escolha um para converter. '))
if escolha == 1:
    print(f'O numero {numero} convertido em numero binario é {bin(numero)[2:]}')
elif escolha == 2:
    print(f' O numero {numero} convertido em numero octal é {oct(numero)[2:]}]')
elif escolha == 3:
    print(f' O numero {numero} convertido em numero hexadecimal é {hex(numero)[2:]} ')
else:
    print('Opção invalida!')
