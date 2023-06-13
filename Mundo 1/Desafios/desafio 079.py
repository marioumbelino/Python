lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adiciionado com sucesso.')
    else:
        print('Valor já adicionado.')
    res = ' '
    while True:
        res = str(input('Deseja acrescentar mais algum número? [S/N] ')).strip()[0]
        if res not in 'SsNn':
            print('\033[31mOcorreu um erro, tente novamente!\033[m')
        else:
            break
    if res in 'Nn':
        break
lista.sort()
print(f'Os números digitados foram: {lista}')