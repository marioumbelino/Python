ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('\033[31mOcorreu um erro, tente novamente.\033[m')
    print(ext[num].capitalize())
    res = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if 'N' in res:
        break
print('Fim do programa...')