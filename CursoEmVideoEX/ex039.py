from datetime import date
from time import sleep
ano = int(input('Digite o  ano que você nasceu: '))
sexo = str(input('Digite seu sexo: ')).upper()
idade = date.today().year - ano
if sexo == 'FEMININO':
    print('Você está dispensada, pois o alistamento feminino não é obrigatorio.')
    exit()
elif sexo == 'MASCULINO':
    print('Vamos da continuidade no seu alistamento!')
else:
    print('ERRO 444')
    print('TENTE NOVAMENTE...')
    exit()
if idade == 18:
    print(f'Você tem {idade} anos, já está na hora de fazer o alistamento militar.')

elif idade < 18:
    print(f'Você tem {idade} anos, ainda faltam {18 - idade} anos para você fazer seu alistamento militar.')
    print(f'Você terá que se alistar apenas em {ano + 18}')

elif idade > 18:
    print(f'Você tem {idade} anos, já passou do prazo para alistamento ou já concluiu.')
    print(f'''O ano para você se alistar era {ano + 18}. 
Procure o mais rapido possivel um posto de alistamento, caso não tenha se alistado.''')