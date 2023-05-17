from random import choice
from time import sleep
jokenpô = ['pedra', 'papel', 'tesoura']
print('-=-' * 2)
print('\033[1;35mJokenpô\033[m')
print('-=-' * 2)
jogador = str(input('Vamos jogar Jokenpô?? \nDigite papel, pedra ou tesoura: '))
pc = choice(jokenpô)
if pc == 'pedra' and 'pedra' in jogador or pc == 'papel' and 'papel' in jogador or pc == 'tesoura' and 'tesoura' in jogador:
    print('Suspense...')
    sleep(3)
    print('\033[34mEmpate\033[m!! Vamos novamente!')
elif pc == 'pedra' and 'papel' in jogador or pc == 'papel' and 'tesoura' in jogador or pc == 'tesoura' and 'pedra' in jogador:
    print('Suspense...')
    sleep(3)
    print('\033[32mParabéns, você venceu\033[m! Se quiser ir novamente, basta apertar play!')
    print('Eu escolhi {}.'.format(pc))
elif pc == 'papel' and 'pedra' in jogador or pc == 'tesoura' and 'papel' in jogador or pc == 'pedra' and 'tesoura' in jogador:
    print('Suspense...')
    sleep(3)
    print('\033[31mQue pena, você perdeu\033[m! Mas não desanime, vamos novamente!')
    print('Eu escolhi {}.'.format(pc))
else:
    print('\033[1;31mERRO: opção não reconhecida.\033[m \nPor favor, tente novamente e lembre-se de digitar "pedra", "papel" ou "tesoura" corretamente!')
