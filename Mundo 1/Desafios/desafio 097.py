def escreva(txt):
    print('-' * (len(txt) + 4))
    print(f'  {txt}  ')
    print('-' * (len(txt) + 4))


msg = input('Digite uma mensagem: ')
escreva(msg)
