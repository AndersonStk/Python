import math
cateto = float(input('Qual o valor do cateto: '))
adjacente = float(input('Qual o valor da adjacence: '))
print(f'A hipotenusa vai medir {(cateto ** 2 + adjacente ** 2) ** (1/2):.2f}')