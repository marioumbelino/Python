from random import randint
print('-' * 20)
print('Vamos jogar PAR ou ÍMPAR??')
print('-' *20)
win = 0
while True:
    num = int(input('Digite um número: '))
    pc = randint(0, 10)
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Escolha entre PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    print(f'Eu escolhi {pc}! O resultado é igual a {pc + num}!')
    if ((num + pc) % 2) == 0:
        if pi in 'P':
            print('Você \033[32mvenceu\033[m!! Parabéns! Vamos novamente!')
        elif pi in 'I':
            print('Que pena, você \033[31mperdeu\033[m!!')
            break
    else:
        if pi in 'P':
            print('Que pena, você \033[31mperdeu\033[m!!')
            break
        elif pi in 'I':
            print('Você \033[32mvenceu\033[m!! Parabéns! Vamos novamente!')
    win += 1
print('=' * 20)
print('\033[31mGAMER OVER\033[m')
print('=' * 20)
if win > 0:
    print(f'Você conseguiu \033[32m{win}\033[m vitórias consecutivas.')
    print('Parabéns!!')
elif win == 0:
    print('Você não conseguiu nenhuma vitória...')
    print('Mas não desanime, tente novamente!')
