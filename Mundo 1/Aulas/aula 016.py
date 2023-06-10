print('--' * 15)
lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim')
for l in lanche:
    print(l)
print('--' * 15)
for p, l in enumerate(lanche):
    print(f'Eu quero {l}, que está na posição {p + 1}')
    
del(lanche)
print('--' * 15)
print('Fim...')