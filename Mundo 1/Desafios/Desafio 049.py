num = int(input('digite o número inteiro no qual queira saber sua tabuada: '))
print('A tabuada do número {} é:'.format(num))
for c in range (1, 11):
    tab = num * c
    print('{} x {} = {}'.format(num, c, tab))
    