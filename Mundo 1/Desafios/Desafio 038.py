from time import sleep
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
print('Analisando os dois números, aguarde...')
sleep(3)
if n1 > n2:
    print('O número {} é maior do que o {}!'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior do que o {}!'.format(n2, n1))
else:
    print('Não há número maior do que o outro, ambos são iguais.')