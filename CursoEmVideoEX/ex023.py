numero = int(input('Digite um numero: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'Unidade: \033[32m{unidade}\033[m')
print(f'Dezena: \033[32m{dezena}\033[m')
print(f'Centena: \033[32m{centena}\033[m')
print(f'Milhar: \033[32m{milhar}\033[m')