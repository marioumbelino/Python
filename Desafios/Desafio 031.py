dis = float(input('Me informe a distância de sua viagem em KM: '))
if dis <= 200:
    print('O valor total da sua passagem é igual a R${:.2f}!'.format(dis * 0.50))
else:
    print('O valor total da sua passagem é igual a R${:.2f}!'.format(dis * 0.45))