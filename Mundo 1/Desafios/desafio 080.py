num = list()
for c in range(1, 6):
    valor = int(input(f'Digite o {c}º: '))
    if c == 1 or valor > max(num):
        num.append(valor)
        print('Valor adicionado ao final da lista.')
    elif valor < min(num):
        num.insert(0, valor)
        print('Valor adicionado ao início da lista.')
    else:
        for i, v in enumerate(num):
            if valor < num[i]:
                num.insert(i, valor)
                print(f'Valor adicionado a posição {num.index(valor)} da lista.')
                break
print(f'Os valores digitados em ordem crescente foram: {num}.')
