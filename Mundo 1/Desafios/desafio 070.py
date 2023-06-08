cheaper = ''
total = caro = count = preco = 0
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    price = float(input('Digite o valor do produto: R$'))
    keep = str(input('Deseja acrescentar mais produtos [S/N]? ')).strip().lower()[0]
    while keep != 's' and keep != 'n':
        keep = str(input('Deseja acrescentar maIS produtos [S/N]? ')).strip().lower()[0]
    total += price
    if price > 1000:
        caro += 1
    if count == 1 or price < preco:
        cheaper = nome
        preco = price   
    count += 1
    if keep in 'n':
        break
print(f'O valor total gasto foi de R${total:.2f}!')
print(f'Dos produtos cadastrados, {caro} produtos custam mais do que R$1000.')
print(f'O produto mais barato é o {cheaper}, que custa R${preco:.2f}.')