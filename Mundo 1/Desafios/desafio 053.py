frase = str(input('Digite uma frase: ')).split()
frase = ''.join(frase)
inv = frase[::-1]
if inv == frase:
    print('Que interessante, sua frase é um políndromo!!')
else:
    print('Infelizmente essa frase não é um políndromo...')