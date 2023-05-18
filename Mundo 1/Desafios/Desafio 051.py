num = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
for c in range (1, 11):
    pa = num + (c - 1) * raz
    print(pa)
