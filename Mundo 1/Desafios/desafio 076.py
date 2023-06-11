prod = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Trasnferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print('{:^40}'.format('LOJA SKYLLOR'))
print('-' * 40)
for pos in range (0, len(prod)):
    if pos % 2 == 0:
        print(f'{prod[pos]:.<30}', end='')
    else:
        print(f'R${prod[pos]:>7.2f}')
print('-' * 40)
    