n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua outra nota: '))
n3 = float(input('Digite sua terceira nota: '))
media = (n1 + n2 + n3) / 3
print('Sua média foi: {:.1f}'.format(media))
if media >= 7:
    print('Parabéns, você passou!')
else:
    print('Que pena, você não foi aprovado. Mas não desanime, continue estudando que você conseguirá!')