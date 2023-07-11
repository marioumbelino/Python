from time import sleep
def contador(a, b, c):
    lin()
    c = abs(c)
    if c == 0:
        c += 1
    print(f'Contagem de {a} a {b} de {abs(c)} em {abs(c)}:')
    if b < a:
        c = -c
        b -= 2
    for num in range(a, b + 1, c):
        print(num, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
    lin()
def lin():
    print('-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez!!')
contador(int(input('Início: ')), int(input('Final: ')), int(input('Passo: ')))
