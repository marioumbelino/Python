from random import randint
def sorteio(lista):
    print('Sorteando 5 valores: ', end='')
    for i in range(0, 5):
        num = randint(0, 10)
        lista.append(num)
        print(num, end=' ')
    print()
def somaPar(lista):
    s = 0
    for i in lista:
        if i % 2 == 0:
            s += i
    print(f'Somandos os valores pares contidos em {lista}, temos o resultado: {s}')
números = []
sorteio(números)
somaPar(números)
