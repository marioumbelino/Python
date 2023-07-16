def aumentar(num=0, pcem=0, form=True):
    aum = num + (num * (pcem / 100))
    return aum if form == False else moeda(aum)

def diminuir(num=0, pcem=0, form=True):
    dim = num - (num * (pcem / 100))
    return dim if form == False else moeda(dim)

def metade(num=0, form=True):
    met = num / 2
    return met if form == False else moeda(met)

def dobro(num=0, form=True):
    dob = num * 2
    return dob if form == False else moeda(dob)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
    
    