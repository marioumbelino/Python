def area(l, c):
    are = l * c
    print(f'A área de um terreno {l}x{c} é de {are}m²')
    

print('-' * 30)
print(f'{"Controle de Terreno":^30}')
print('-' * 30)

lar = float(input('Largura (m): '))
com = float(input('Comprimento (m): '))

area(lar, com)