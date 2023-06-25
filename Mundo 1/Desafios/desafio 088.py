from random import randint
from time import sleep
print('-' * 40)
print(f'{"Mega Sena":^40}')
print('-' * 40)
jog = int(input('Quantos jogos quer que eu gere? '))
jogos = []
temp = []
for lis in range(jog):
    for num in range(0, 6):
        pc = randint(1, 60)
        if pc not in temp:
            temp.append(pc)
    temp.sort()
    jogos.append(temp[:])
    temp.clear()
print('-' * 40)
for sena in range(jog):
    print(f'O {sena + 1}º jogo é: {jogos[sena]}')
    sleep(0.5)
print('\033[32mBoa sorte!\033[m')
print('-' * 40)
