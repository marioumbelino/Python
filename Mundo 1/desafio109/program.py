import moedas

din = float(input('Informe o valor do produto: '))
print(f'O dobro de {moedas.moeda(din)} é {moedas.dobro(din)}')
print(f'A metade de {moedas.moeda(din)} é {moedas.metade(din)}')
print(f'Aumentando 10% de {moedas.moeda(din)} é {moedas.aumentar(din, 10)}')
print(f'Diminuíndo 13% de {moedas.moeda(din)} é igual a {moedas.diminuir(din, 13)}')