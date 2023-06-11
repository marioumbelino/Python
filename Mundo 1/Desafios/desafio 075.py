tup = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')), int(input('Digite o terceito número: ')), int(input('Digite o quarto número: ')))
print(f'O número 9 apareceu {tup.count(9)} vezes.')
par = ''
if 3 in tup:
    print(f'O número 3 foi digitado primeiro na {tup.index(3) + 1}ª posição.')
else:
    print('Não foi digitado nenhum número 3.')
print('Os números pares digitados foram :', end=' ')
for n in tup:
    if n % 2 == 0:
        print(n, end= ' ')
