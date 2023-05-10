import math
n = float(input('Digite um número real: '))
it = math.trunc(n)
print('A parte inteira do número \033[1;31m{}\033[m é igual a \033[1;32m{}\033[m'.format(n, it))