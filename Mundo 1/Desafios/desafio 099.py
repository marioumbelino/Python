from time import sleep
def maior(*num):
    if len(num) > 0 and num[0] > 0:
        print('-' * 40)
        print('Analisando os valores fornecidos...')
        for i in num:
            sleep(0.5)
            print(i, end=' ')
        print()
        print(f'Foram informados {len(num)} números.')
        print(f'O maior número fornecido foi o {max(num)}')
        print('-' * 40)
    else:
        print('-' * 40)
        print('Analisando os valores fornecidos...')
        print('Não foi informado nenhum número, além do 0.')
        print(f'Portanto, maior número fornecido foi o {max(num)}')
        print('-' * 40)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
