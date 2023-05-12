nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
média = (nota1 + nota2) / 2
if média >= 7:
    print('Parabéns, com suas notas \033[1;32mvocê foi aprovado\033[m!! Sua média: {}!'.format(média))
elif média < 7 and média >=5:
    print('Que pena! Suas notas não foram suficiente para você ser aprovado, \nmas não se desanime, ainda \033[1;36mpoderá realizar a prova de recuperação\033[m!! \nSua média: {}!'.format(média))
elif média < 5:
    print('Que pena! Suas notas \033[1;31mnão foram suficientes para você ser aprovado nem ficar de recuperação\033[m. \nMas não se abale, com foco, disposição e estudo, você conseguirá sua aprovação!. \nSua média: {}'.format(média))