prin = [[], []]
for c in range (1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        prin[0].append(num)
    else:
        prin[1].append(num)
prin[1].sort()
prin[0].sort()
print(f'Os números pares cadastrados foi: {prin[0]}')
print(f'Os números ímpares cadastrados foi: {prin[1]}')
    