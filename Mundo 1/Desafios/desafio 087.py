matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
som3 = pares = mai = 0
for l in range (0, 3):
    for c in range (0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l}; {c}]: '))
print('-' * 25)
print('A matriz digitada é: ')
for l in range (0, 3):
    for c in range (0, 3):
        print(f'[{matriz[l][c]:^5}]', end= ' ')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            som3 += matriz[l][c]
        if l == 1:
            if c == 0:
                mai = matriz[l][c]
            elif mai < matriz[l][c]:
                mai = matriz[l][c]
    print()
print('-' * 25)
print(f'A soma de todos os valores pares da matriz é igual a {pares}.')
print(f'A soma dos valores da 3º coluna é igual a {som3}!')
print(f'O maior valor da segunda linha é: {mai}')
print('-' * 25)