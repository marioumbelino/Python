def leiaDinheiro(msg):
    while True:
        dado = input(msg).strip().replace(',', '.')
        try:
            dado = float(dado)
            break
        except ValueError:
            print(f'\033[31mErro!! "{dado}" não é um preço válido!\033[m')
    
    return dado