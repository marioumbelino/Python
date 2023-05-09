n = input('Digite um numero de 4 digitos: ')
s = '000' + n
uni = s[-1]
dez = s[-2]
cen = s[-3]
mil = s[-4]

print(f'Unidade:{uni}\nDezena:{dez}\nCentena:{cen}\nMilhar:{mil}')
