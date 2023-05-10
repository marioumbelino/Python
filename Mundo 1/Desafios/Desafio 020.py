import random
n1 = input('Digite o nome de um dos alunos: ')
n2 = input('Digite o nome de outro aluno: ')
n3 = input('Digite o nome de outro aluno: ')
n4 = input('Digite o nome de outro aluno: ')
nomes = [n1, n2, n3, n4]
ordem = random.sample(nomes, 4)
print('A ordem dos alunos será: ')
print(ordem)