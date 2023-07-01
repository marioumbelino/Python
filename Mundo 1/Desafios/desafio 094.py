from math import trunc
pessoas = []
girls = []
dados = {}
count = 1
soma = 0
acima = []
while True:
    dados['Nome'] = str(input(f'Qual é o nome da {count}ª pessoa? '))
    while True:
        dados['Sexo'] = str(input('Qual é o sexo desta pessoa? [M/F] ')).strip().upper()[0]
        if dados['Sexo'] in 'MF':
            break
        else:
            print('\033[31mERRO!\033[m Por favor, tente novamente!')
    dados['Idade'] = int(input('Digite a idade desta pessoa: '))
    if 'F' in dados['Sexo']:
        girls.append(dados.copy())
    pessoas.append(dados.copy())
    soma += dados['Idade']
    count += 1
    res = ' '
    while True:
        res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        else:
            print('\033[31mERRO!!\033[m Tente novamente!')
    if res in 'N':
        break
if len(pessoas) > 1:
    for c in pessoas:
        if c['Idade'] > (soma / len(pessoas)):
            acima.append(c)
print('-' * 40)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade das pessoas cadastradas é de {trunc(soma / len(pessoas))}')
if len(girls) > 0:
    print('As mulheres adicionadas foram:')
    for p in girls:
        print(f'{p["Nome"]}')
else:
    print('Não foram adicionadas mulheres.')
if len(pessoas) == 1:
    print('Como foi adicionado apenas uma pessoa, não há ninguém acima da média de idade.')
elif len(acima) > 0:
    print('As pessoas que estão com a idade acima da média são: ')
    for p in acima:
        print(f'{p["Nome"]} com {p["Idade"]} anos.')
else:
    print('Todas as pessoas adicionadas possuem a mesma idade.')
print('-' * 40) 
    