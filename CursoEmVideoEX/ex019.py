import random
aluno = str(input('Digite o nome do primeiro aluno: '))
aluno1 = str(input('Digite o nome do segundo aluno: '))
aluno2 = str(input('Digite o nome do terceiro aluno: '))
aluno3 = str(input('Digite o nome do quarto aluno: '))

lista = [aluno, aluno3, aluno2, aluno1]
lista_alunos = random.choice(lista)
print(f'O aluno sorteado foi: {lista_alunos}')