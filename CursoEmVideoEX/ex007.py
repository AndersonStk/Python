nota = float(input('Digite a primeira nota: '))
nota1 = float(input('Digitea a segunda nota: '))
media = (nota + nota1) / 2
if media == 6:
    print(f'Parabens voce passou!! Com a media de \033[1;32m{media}\033[m.')
else:
    print(f'Que pena voce reprovou! Voce ficou com a media de \033[1;31m{media}\033[m.')