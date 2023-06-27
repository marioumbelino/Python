nome = str(input('Digite o nome do aluno: '))
média = float(input('Digite a média do aluno: '))
aluno = {'Nome': nome, 'Média': média}
if média >= 7:
    aluno['Situação'] = '\033[32mAprovado\033[m'
else:
    aluno['Situação'] = '\033[31mReprovado\033[m'
print(f'O nome do aluno é {nome}')
print(f'A sua média é {média}')
print(f'Ele(a) foi {aluno["Situação"]}')