nome = str(input('Digite seu nome completo: ')).strip()
nome1 = nome.split()
print(f'Primeiro nome é \033[1:31m{nome1[0]}\033[m')
print(f'Ultimo nome é \033[1:31m{nome1[-1]}\033[m')