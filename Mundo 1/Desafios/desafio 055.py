mep = 0
map = 0
for c in range (1, 6):
    peso = float(input('Digite o peso {}: '.format(c)))
    if c == 1:
        mep = peso
        map = peso
    else:
        if peso > map:
            map = peso
        if peso < mep:
            mep = peso
print('O maior peso foi {:.0f}kg.'.format(map))
print('O menor peso foi {:.0f}kg.'.format(mep))