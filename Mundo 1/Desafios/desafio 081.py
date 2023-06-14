lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    res = ' '
    while True:
        res = str(input('Deseja acrescentar mais algum número: [S/N] ')).strip().upper()[0]
        if res not in 'SN':
            print('\033[31mOcorreu um erro, tente novamente!\033[m')
        else:
            break
    if res in 'N':
        break
print('-' * 30)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não foi digitado, por isso, não está na lista.')
print('-' * 30)
print()