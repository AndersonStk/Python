nome = str(input('Qual o seu nome completo: ')).strip().upper()
sobrenome = 'SILVA' in nome
print(f'Seu nome tem \033[1;31mSilva\033[m? {sobrenome}')