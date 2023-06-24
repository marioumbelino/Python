pessoastemp = []
pessoas = []
maior = menor = 0
while True:
    pessoastemp.append(str(input('Digite o nome: ')))
    pessoastemp.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoastemp[1]
    else:
        if pessoastemp[1] < menor:
            menor = pessoastemp[1]
        elif pessoastemp[1] > maior:
            maior = pessoastemp[1]
    pessoas.append(pessoastemp[:])
    pessoastemp.clear()
    res = ' '
    while True:
        res = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if res not in 'SN':
            print('Ocorreu um erro, tente novamente!')
        else:
            break
    if res == 'N':
        break
print('-' * 30)
print(f'{len(pessoas)} foram cadastradas.')
print(f'O maior peso cadastrado foi {maior}Kg. Peso de:')
for p in pessoas:
    if p[1] == maior:
        print(p[0])
print(f'O menor peso cadastrado foi {menor}Kg. Peso de:')
for p in pessoas:
    if p[1] == menor:
        print(p[0])
print('-' * 30)
