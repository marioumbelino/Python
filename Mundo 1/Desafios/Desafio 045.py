from random import choice
from time import sleep
jokenpô = ['pedra', 'papel', 'tesoura']
print('-=-' * 10)
print('\033[1;35mJokenpô\033[m')
print('-=-' * 10)
jogador = str(input('Vamos jogar Jokenpô?? \nDigite papel, pedra ou tesoura: '))
print('Suspense...')
sleep(3)
pc = choice(jokenpô)
if pc == 'pedra' and 'pedra' in jogador or pc == 'papel' and 'papel' in jogador or pc == 'tesoura' and 'tesoura' in jogador:
    print('\033[34mEmpate\033[m!! Vamos novamente!')
elif pc == 'pedra' and 'papel' in jogador or pc == 'papel' and 'tesoura' in jogador or pc == 'tesoura' and 'pedra' in jogador:
    print('\033[32mParabéns, você venceu\033[m! Se quiser ir novamente, basta apertar play!')
else:
    print('\033[31mQue pena, você perdeu\033[m! Mas não desanime, vamos novamente!')
print('Eu escolhi {}.'.format(pc))
