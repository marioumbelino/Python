num = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão da PA: '))
count = 0
x = 1
print('Uma PA com o primeiro termo {} e razão {}, resulta nos seguintes termos:'.format(num, raz))
while count < 10:
    pa = num + (x - 1) * raz
    print(pa)
    count += 1
    x += 1
