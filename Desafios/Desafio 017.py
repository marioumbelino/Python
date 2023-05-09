import math
c1 = float(input('Informe o valor de um dos catetos: '))
c2 = float(input('Informe o valor do outro cateto: '))
hi = math.hypot(c1, c2)
print('Um triângulo, cujo catetos medem {} e {}, possui hipotenusa igual a {:.2f}!'.format(c1, c2, hi))
