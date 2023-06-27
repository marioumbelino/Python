from time import sleep
temp = []
alunos = []
while True:
    nome = str(input('Digite o nome: '))
    no1 = float(input('Digite a 1ª nota: '))
    no2 = float(input('Digite a 2ª nota: '))
    media = (no1 + no2) / 2
    temp.append(nome)
    temp.append(no1)
    temp.append(no2)
    temp.append(media)
    alunos.append(temp[:])
    temp.clear()
    res = ' '
    while True:
        res = str(input('Deseja acrescentar mais algum aluno? [S/N] ')).strip().upper()[0]
        if res not in 'SN':
            print('Ocorreu um erro, tente novamente!')
        else:
            break
    if res in 'N':
        break
print('-' * 23)
print('{:<3}{:<10}{:>10}'.format('Nº', 'Nome', 'Média'))
print('-' * 23)
for n, m in enumerate(alunos):
    print('{:<3}{:<10}{:>10}'.format(n, alunos[n][0], alunos[n][3]))
média = 0
while média != 999:
    média = int(input('Deseja visualizar as notas de qual aluno? [Digite 999 para parar] '))
    if média != 999:
        print(f'As notas do aluno {alunos[média][0]} foram {alunos[média][1:3]}')
    else:
        print('Finalizando...')
        sleep(1.5)
        print('Volte sempre!!')
    