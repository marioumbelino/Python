vel = int(input('Quantos Km/h você está? '))
if vel <= 80:
    print('Parabéns, você está dentro do limite de velocidade, continue assim!')
else:
    print('Que decepção, você está a {}, acima da velocidade permitida.'.format(vel))
    multa = (vel - 80) * 7
    print('Como consequência, você levará uma multa de R${:.2f}'.format(multa))