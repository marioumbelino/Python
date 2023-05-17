print('-=-' * 6)
print('\033[1;35mCalculadora IMC\033[m')
print('-=-' * 6)
al = float(input('Me informe a sua altura em metros: '))
peso = float(input('Me informe o seu peso em KG: '))
imc = peso / al ** 2
if imc < 18.5:
    print('Seu IMC é igual a {:.2f}. \nVocê está abaixo do peso!!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é igual a {:.2f}. \nVocê está no peso ideal!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é igual a {:.2f}. \nVocê está sobrepeso!'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é igual a {:.2f}. \nSua condição física é OBESIDADE!!'.format(imc))
else:
    print('Seu IMC é igual a {:.2f}. \nVocê está com OBESIDADE MÓRBIDA!!'.format(imc))
