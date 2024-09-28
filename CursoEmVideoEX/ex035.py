print('ANALISSADOR DE TRIÂNGULOS...')
print('\033[36m-=-\033[m' * 20)
seg = float(input('Primeiro seguimento: '))
seg1 = float(input('Seguendo seguimento: '))
seg2 = float(input('Terceiro seguimento: '))

if seg < seg1 + seg2 and seg1 < seg + seg2 and seg2 < seg + seg1:
    print('\033[32mÉ UM TRIÂNGULO\033[m')
else:
    print('\033[31mNÃO É UM TRIÂNGULO\033[m')