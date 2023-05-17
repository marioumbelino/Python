from time import sleep
print('-=-' * 4)
print('Estouro de Fogos de Artifícios')
print('-=-' * 4)
i = str(input('Digite "começar" para iniciar a contagem regressiva \npara o estouro de fogos de artifícios!! ')).lower()
if 'começar' in i:
    for c in range(10, 0, -1):
        print(c)
        sleep(1)
    print('Fogos!!🎆💥')
else:
    print('Comando inválido, tente novamente!')