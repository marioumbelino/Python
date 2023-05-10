n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite o terceiro número: '))
# Qual é o maior
if n1 > n2 and n1 > n3:
    print('O número {} é o maior!'.format(n1))
if n2 > n1 and n2 > n3:
    print('O número {} é o maior!'.format(n2))
if n3 > n1 and n3 > n2:
    print('O número {} é o maior!'.format(n3))
# Qual é o menor
if n1 < n2 and n1 < n3:
    print('O número {} é o menor!'.format(n1))
if n2 < n1 and n2 < n3:
    print('O número {} é o menor!'.format(n2))
if n3 < n1 and n3 < n2:
    print('O número {} é o menor!'.format(n3))