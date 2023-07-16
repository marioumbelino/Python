import moedas

din = float(input('Informe o valor do produto: '))
print(f'O dobro de {moedas.moeda(din)} é {moedas.moeda(moedas.dobro(din))}')
print(f'A metade de {moedas.moeda(din)} é {moedas.moeda(moedas.metade(din))}')
print(f'Aumentando 10% de {moedas.moeda(din)} é {moedas.moeda(moedas.aumentar(din, 10))}')
print(f'Diminuíndo 13% de {moedas.moeda(din)} é igual a {moedas.moeda(moedas.diminuir(din, 13))}')