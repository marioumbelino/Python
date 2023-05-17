from time import sleep
print('-=-' * 10)
print('\033[1;36mAnalisador de Triangulos\033[m')
print('-=-' * 10)
n1 = float(input('Informe o comprimento de uma das retas: '))
n2 = float(input('informe o comprimento da segunda reta: '))
n3 = float(input('Informe o comprimento da terceira reta: '))
print('Analisando as 3 retas, por favor aguarde...')
sleep(3)
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 != n2 and n2 != n3 and n1 != n3:
        print('Essas retas \033[32mconseguem\033[m formar um \033[36mtriângulo escaleno\033[m, pois não possuem retas (lados) iguais')
    elif n1 != n2 and n1 == n3 or n1 != n3 and n2 == n3 or n2 != n3 and n1 == n2:
        print('Essas retas \033[32mconseguem\033[m formar um \033[36mtriângulo isósceles\033[m, pois possuem 2 retas (lados) iguais.')
    else:
        print('Essas retas \033[32mconseguem\033[m formar um \033[36mtriângulo equilátero\033[m, pois possui todos as retas (lados) iguais.')
else:
    print('Essas retas não conseguem formar um triângulo!!')
