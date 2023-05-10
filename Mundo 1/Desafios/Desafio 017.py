import math
c1 = float(input('Informe o valor de um dos catetos: '))
c2 = float(input('Informe o valor do outro cateto: '))
hi = math.hypot(c1, c2)
print('Um triângulo, cujo catetos medem \033[4;35m{}\033[m e \033[4;35m{}\033[m, possui hipotenusa igual a \033[4;33m{:.2f}\033[m!'.format(c1, c2, hi))
