from time import sleep
nome = str(input('Digite seu nome completo: '))
print('Analissando...')
sleep(2)
print('Seu nome completo em letras maiusculas fica:')
print(f'\033[1;32m{nome.upper()}\033[m')
sleep(0.5)
print('Seu nome completo em letras minusculas fica:')
print(f'\033[1;32m{nome.lower()}\033[m')
sleep(1)
print(f'Seu nome possui um total de \033[1;32m{len(nome) - nome.count(' ')}\033[m letras')
sleep(1.3)
print(f'Seu primeiro nome tem um total de \033[1;32m{len(nome.split()[0])}\033[m letras')