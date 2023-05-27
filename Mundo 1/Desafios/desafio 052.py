num = int(input('Digite um número: '))
primo = 0
for c in range (1, num+1):
    if num % c == 0:
        print('\033[36m', end='')
        primo = primo + 1
    else:
        print('\033[m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divido {} vezes'.format(num, primo))
if primo == 2:
    print('Logo, é um número primo.')
else:
    print('Logo, não é um número primo.')