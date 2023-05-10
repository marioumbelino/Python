import random
n1 = input('Digite o nome de um dos alunos: ')
n2 = input('Digite o nome de outro aluno: ')
n3 = input('Digite o nome de outro aluno: ')
n4 = input('Digite o nome de outro aluno: ')
ale = [n1, n2, n3, n4]
print('O(a) aluno(a) sorteado foi: {}!'.format(random.choice(ale)))
