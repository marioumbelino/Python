r1 = float(input('Informe o comprimento de uma das retas: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
if r1 < r2 + r3:
    if r2 < r1 + r3:
        if r3 < r1 + r2:
            print('Essas retas conseguem formar um triângulo!')
        else:
            print('Essas retas não conseguem formar um triângulo!')
    else:
        print('Essas retas não conseguem formar um triângulo!')
else:
    print('Essas retas não conseguem formar um triângulo!')
