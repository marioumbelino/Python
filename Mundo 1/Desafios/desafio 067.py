while True:
    num = int(input('Digite o número do qual queira saber a tabuada. Digite um número negativo para interromper o programa: '))
    if num < 0:
        break
    print('-' * 15)
    for c in range (1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 15)
    