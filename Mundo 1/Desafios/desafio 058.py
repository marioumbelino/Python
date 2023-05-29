import random
from time import sleep
num = 11
count = 1
print('-'*90)
print('Vou pensar em um número de 0 a 10, tente adivinhar qual número eu estou pensando')
print('-'*90)
pc = random.randint(0, 10)
print('Processando...')
sleep(2)
while num != pc:
    num = int(input('Em qual número eu pensei? '))
    if num != pc:
        print('Infelizmente você não acertou... \nTente novamente!'. format(pc, num))
        count += 1
print('Parabéns, você acertou!! Eu estava pensando no número {}. \nForam necessárias {} chances até acertar!!'.format(num, count))
