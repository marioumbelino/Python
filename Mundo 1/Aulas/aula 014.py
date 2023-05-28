n = 1
np = ni = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n % 2 == 0:
        np += 1
    else:
        ni += 1
print('Você digitou {} números pares e {} números ímpares.'.format(np, ni))
print('Fim!')