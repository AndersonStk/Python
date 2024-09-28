import math
angulo = float(input('Digite  angulo que voce deseja: '))
radiantes = math.radians(angulo)
print(f'O angulo de {angulo} tem o SENO de {math.sin(radiantes):.2f}')
print(f'O Angulo de {angulo} tem o COSSENO de {math.cos(radiantes):.2f}')
print(f'O angulo de {angulo} tem o TANGENTE de {math.tan(radiantes):.2f}')