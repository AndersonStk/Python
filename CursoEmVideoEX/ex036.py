casa = float(input('Qual o valor da casa: '))
salario = float(input('Quanto voce ganha: '))
anos = int(input('Em quanto anos pretende pagar: '))
meses = anos * 12
prestaçao = casa / meses
if prestaçao <= (salario * 0.30) % salario:
    print(f'Parabéns seu emprestimo foi aprovado, o valor das parcelas ficaram de \033[32mR${prestaçao:.2f}\033[m')
else:
    print(f'Seu emprestimo foi recusado, o valor das parcelas ficaram de \033[31mR${prestaçao:.2f}\033[m')