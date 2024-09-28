dias = int(input('Por quantos dias sara alugado o veiculo? '))
km = float(input('Quantos Km/h foram rodados? '))
dia = dias * 60
km1 = km * 0.15
valor = dia + km1
print(f'O valor total do pagamento é de R${valor:.2f}')