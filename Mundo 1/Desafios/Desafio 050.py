s = 0
for c in range(1, 7):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        s += num
print('A soma de todos os números pares digitados é igual a {}!'.format(s))
