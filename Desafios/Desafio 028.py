import random
pc = random.randint(0, 5)
num = int(input('Tente advinhar qual número inteiro de 0 a 5 o computador está pensando? '))
if num == pc:
    print('Parabéns, você acertou!!')
else:
    print('Infelizmente você não acertou, tente novamente!')
print('O número que o computador estava pensando era {}'.format(pc))
