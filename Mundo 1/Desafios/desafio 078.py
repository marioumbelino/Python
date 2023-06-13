valores = []
for r in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)}, na(s) posição(ões)', end=' ')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'{p + 1}...', end=' ')
print(f'\nO menor valor digitado foi {min(valores)}, na(s) posição(ões):', end=' ')
for p, v in enumerate(valores):
    if v == min(valores):
        print(f'{p + 1}...', end=' ')
