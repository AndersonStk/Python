from datetime import date
ano = int(input('Em que ano você nasceu?: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print(f'Classificação: MIRIM')
elif idade >= 10 and idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print(f'Classificação: INFANTIL')
elif idade >= 15 and idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print(f'Classificação: JUNIOR')
elif idade >= 20 and idade <= 25:
    print(f'O atleta tem {idade} anos.')
    print(f'Classificação: SÊNIOR')
elif idade > 25:
    print(f'O atleta tem {idade} anos.')
    print(f'Classificação: MASTER')