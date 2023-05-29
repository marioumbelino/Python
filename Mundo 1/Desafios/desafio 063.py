qtde = int(input('Digite a quantidade de termos da sequência de Fibonacci que deseja saber: '))
count = 0
x = 0
x1 = 1
x2 = 0
print(x, end= ' ')
print(x1, end= ' ')
while count < (qtde - 2):
    count += 1
    x2 = x + x1
    print(x1, end=' ')
    x = x1
    x1 = x2
    