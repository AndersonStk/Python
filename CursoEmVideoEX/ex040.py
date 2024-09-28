nota = float(input('Primeira nota: '))
nota1 = float(input('Segunda nota: '))
media = (nota + nota1) / 2
if media <= 5.0:
    print(f'A soma entre as notas {nota} & {nota1} é de {media:.1f}.\n'
          f'\033[1;31mVOCÊ ESTÁ REPROVADO! ESTUDE MAIS.\033[m')
elif media >= 5.0 and  media <= 6.9:
    print(f'A soma entre as notas {nota} & {nota1} é de {media:.1f}.\n'
          f'\033[1;34mVOCÊ ESTÁ DE RECUPERAÇÃO! SE ESFORCE MAIS.\033[m')
elif media >= 7.0:
    print(f'A soma entre as notas {nota} & {nota1} é de {media:.1f}.\n'
          f'\033[1;32mPARABÉNS, VOCÊ ESTA APROVADO!!! CONTINUE SEMPRE ASSIM.\033[m')