from time import sleep
print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)
r1 = float(input('Informe o comprimento de uma das retas: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
print('Analisando, aguarde...')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas retas CONSEGUEM formar um triângulo!')
else:
    print('Essas retas NÃO conseguem formar um triângulo!')
