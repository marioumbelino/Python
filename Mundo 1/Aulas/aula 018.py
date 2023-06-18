grupo = []
pessoas = []
while True:
    pessoas.append(str(input('Digite o nome de uma pessoa: ')))
    pessoas.append(int(input('Digite a idade desta pessoa: ')))
    grupo.append(pessoas[:])
    res = ' '
    while res not in 'N':
        res = str(input('Deseja acrescentar mais alguém? [S/N]')).strip().upper()[0]
        if res not in 'SN':
            print('Houve um erro, digite novamente.')
        else:
            break
    pessoas.clear()
    if res in 'N':
        break
print(grupo)
