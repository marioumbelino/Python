frase = str((input('Digite uma frase: '))).strip()
frase = frase.lower()
print('Na sua frase há {} letra(s) "a(s)"'.format(frase.count('a') + frase.count('á')))
print('O primeiro "a" se encontra na posição {}'.format(frase.find('a') + 1))
print('A última letra "a" se econtra na posição {}'.format(frase.rfind('a') + 1))