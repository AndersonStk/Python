salario = float(input('Qual o salario do funcionario? R$'))
aumento1 = salario + (salario * 0.15)
print(f'O novo salario é de \033[32mR${aumento1:.2f}\033[m, com um aumento de \033[32m15%\033[m.')
