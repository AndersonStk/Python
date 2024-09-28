produto = float(input('Qual o valor do produto: R$'))
desconto = produto - (produto * 5 / 100)
print(f'O valor do prduto é R$ \033[32m{produto:.2f}\033[m, com \033[31m5%\033[m de desconto fica por R$ \033[32m{desconto:.2f}\033[m.')