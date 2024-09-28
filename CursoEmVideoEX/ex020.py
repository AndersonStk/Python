from random import shuffle
aluno = input('Digite um nome de aluno: ')
aluno1 = input('Digite um nome de aluno: ')
aluno2 = input('Digite um nome de aluno: ')
aluno3 = input('Digite um nome de aluno: ')

lista = [aluno, aluno2, aluno1, aluno3]
shuffle(lista)
print('A ordem escolhida foi:')
print(lista)