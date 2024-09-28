altura = float(input('Qual a altura da parede: '))
largura = float(input('Qual a largura da parede: '))
area = altura * largura
tinta = area / 2
print(f'A dimençao da parede é de {altura}x{largura}, assim tendo uma area de {area}m²')
print(f'Será nescessario {tinta}L de tinta para pintar a parede.')