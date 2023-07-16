def aumentar(num=0, pcem=0):
    aum = num + (num * (pcem / 100))
    return aum

def diminuir(num=0, pcem=0):
    dim = num - (num * (pcem / 100))
    return dim
def metade(num=0):
    met = num / 2
    return met

def dobro(num=0):
    dob = num * 2
    return dob

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
    
    