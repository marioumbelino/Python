import random
from time import sleep
print('-'*90)
print('Vou pensar em um número de 0 a 5, tente adivinhar qual número eu estou pensando')
print('-'*90)
pc = random.randint(0, 5)
print('Processando...')
sleep(2)
num = int(input('Em qual número eu pensei? '))
if num == pc:
    print('Parabéns, você acertou!! Eu estava pensando no número {}'.format(num))
else:
    print('Infelizmente você não acertou... \nEu pensei em {} e não no {}. \nTente novamente!'. format(pc, num))
