from random import randint
números = []
def sorteio():
    print('Sorteando 5 valores: ', end='')
    for i in range(0, 5):
        num = randint(0, 10)
        números.append(num)
        print(num, end=' ')
    print()
def somaPar():
    s = 0
    for i in números:
        if i % 2 == 0:
            s += i
    print(f'Somandos os valores pares contidos em {números}, temos o resultado: {s}')

sorteio()
somaPar()
