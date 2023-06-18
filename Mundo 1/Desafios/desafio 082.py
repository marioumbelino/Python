lista = []
listap = []
listai = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    res = ' '
    while True:
        res = str(input('Deseja acrescentar mais algum número? [S/N] ')).strip()[0]
        if res not in 'SsNn':
            print('\033[31mOcorreu um erro, tente novamente!\033[m')
        else:
            break
    if res in 'Nn':
        break
for c, v in enumerate(lista):
    if v % 2 == 0:
        listap.append(v)
    else:
        listai.append(v)
print(f'A lista completa: {lista}')
print(f'A lista que contém apenas os números pares: {listap}')
print(f'Os números que contém apenas os números ímpares: {listai}')