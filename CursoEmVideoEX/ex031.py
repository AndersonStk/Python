viagem = float(input('Qual a distancia que você pretende percorrer: '))
valor = viagem * 0.50
valor1 = viagem * 0.45
if viagem <= 200:
    print(f'O valor da sua viagem é de: \033[32mR$ {valor:.2f}\033[m.')
else:
    print(f'O valor da sua viagem acima de 200 Km/h é de: \033[32mR$ {valor1:.2f}\033[m')