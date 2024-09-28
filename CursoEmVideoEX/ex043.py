altura = float(input('Qual sua altura: '))
peso = float(input('Qual seu peso: '))
imc = peso / (altura * altura)
if imc <= 18.5:
    print(f'O IMC dessa pessoa é {imc:.1f}')
    print('Abaixo do peso.')
elif imc <= 25:
    print(f'O IMC dessa pessoa é {imc:.1f}')
    print('Peso ideal')
elif imc <= 30:
    print(f'O IMC dessa pessoa é {imc:.1f}')
    print('Sobrepeso')
elif imc <= 40:
    print(f'O IMC dessa pessoa é {imc:.1f}')
    print('Obesidade')
else:
    print(f'O IMC dessa pessoa é {imc:.1f}')
    print('Obesidade Mórbida')