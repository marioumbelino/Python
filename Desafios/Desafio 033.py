n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 > n2:
    if n1 > n3:
        print('O número {} é maior do que {} e {}'.format(n1, n2, n3))
    else:
        print('O número {} é maior do que {} e {}'.format(n3, n1, n2))
else:
    if n2 > n3:
        print('O número {} é maior do que {} e {}'.format(n2, n1, n3))
    else:
        print('O número {} é maior do que {} e {}'.format(n3, n1, n2))