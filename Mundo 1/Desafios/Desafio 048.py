sc = 0
for c in range (1, 501):
    if c % 2 != 0 and c % 3 == 0:
        sc += c
print('A soma entre os números multiplos de 3 contidos entre 1 a 500 é igual {}'.format(sc))