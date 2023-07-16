def aumentar(num=0, pcem=0, form=False):
    aum = num + (num * (pcem / 100))
    return aum if form == False else moeda(aum)

def diminuir(num=0, pcem=0, form=False):
    dim = num - (num * (pcem / 100))
    return dim if form == False else moeda(dim)

def metade(num=0, form=False):
    met = num / 2
    return met if form == False else moeda(met)

def dobro(num=0, form=False):
    dob = num * 2
    return dob if form == False else moeda(dob)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
    
def resumo(p=0, acres=10, desc=5):
    print('-' * 35)
    print(f'{"Resumo do Valor":^35}')
    print('-' * 35)
    print(f'Valor analizado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, form=True)}')
    print(f'Metade do preço: \t{metade(p, form=True)}')
    print(f'{acres}% de acrescimo: \t{aumentar(p, acres, form=True)}')
    print(f'{desc}% de desconto: \t{diminuir(p, 30, form=True)}')
    print('-' * 35)