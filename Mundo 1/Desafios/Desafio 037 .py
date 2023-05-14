num = int(input('Digite um número inteiro que queira converter: '))
conv = str(input('Qual será a base de conversão? \n1- Binário \n2- Octal \n3- Hexadecimal \n')).upper()
if '1' in conv or 'BINÁRIO' in conv or 'BINARIO' in conv:
    bi = bin(num)
    print('O número {} em binários equivale a {}'.format(num, bi[2:]))
elif '2' in conv or 'Octal' in conv:
    oc = oct(num)
    print('O número {} em octal equivale a {}'. format(num, oc[2:]))
elif '3' in conv or 'HEXADECIMAL' in conv:
    he = hex(num)
    print('O número {} representado em Hexadecimal equivale a {}'.format(num, he[2:]))

