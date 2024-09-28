numero = int(input('Digite o primeiro valor: '))
numero1 = int(input('Digite o segundo valor: '))
numero2 = int(input('Digite o ultimo valor: '))
if numero < numero1 and numero < numero2:
    print(f'O numero menor foi {numero}')
if numero1 < numero and numero1 < numero2:
    print(f'O numero menor foi {numero1}')
if numero2 < numero and numero2 < numero1:
    print(f'O numero menor foi {numero2}')
if numero > numero1 and numero > numero2:
    print(f'O numero maior foi {numero}')
if numero1 > numero and numero1 > numero2:
    print(f'O numero maior foi {numero1}')
if numero2 > numero and numero2 > numero1:
    print(f'O numero maior foi {numero2}')