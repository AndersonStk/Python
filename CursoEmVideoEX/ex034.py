salario = float(input('Digite o seu salario: '))
if salario <= 1250:
    print(f'O seu salario era de \033[32mR${salario:.2f}\033[m e teve um aumento de \033[32m15%\033[m. '
          f'Assim ficando agora em \033[32mR${(salario * 0.15) + salario:.2f}\033[m')
else:
    print(f'O Seu salario era de \033[32mR${salario:.2f}\033[m e teve um aumento de \033[32m10%\033[m. '
          f'Assim ficando agora em \033[32mR${(salario * 0.10) + salario:.2f}\033[m')