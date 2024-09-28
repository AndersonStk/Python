velocidade = float(input('Digite sua velocidade: '))
if velocidade <= 80:
    print('\033[1;32mTenha um bom dia e dirija com segurança!\033[m')
else:
    limite = 7 * (velocidade - 80)
    print(f'\033[1;31mVocê atingiu o limite de velocidade que é de 80Km/h '
          f'e sofreu uma multa no valor de R$ {limite:.2f}\033[m')

