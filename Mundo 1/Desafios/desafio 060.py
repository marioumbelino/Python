# COM FOR
'''fat = 1
num = int(input('Digite um número inteiro que queira saber o fatorial: '))
for c in range (1, num + 1):
    fat *= c
print('O fatorial de {} é igual a {}'.format(num, fat))'''

# COM WHILE
num = int(input('Digite um número inteiro que queira saber o fatorial: '))
fat = 1
n = num
while n > 1:
    fat *= n
    n -= 1
print('O fatorial do número {} é igual a {}'.format(num, fat))

# COM BIBLIOTECAS
'''from math import factorial
num = int(input('Digite um número inteiro que queira saber o fatorial: '))
print('{}! é igual a {}'.format(num, factorial(num)))'''