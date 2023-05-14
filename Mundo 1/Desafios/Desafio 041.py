from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
ida = date.today().year - ano
cor = '\033[1;35m'
ori = '\033[m'
if ida <= 9:
    print('Sua categoria de natação é {}MIRIM!{}'.format(cor, ori))
elif ida > 9 and ida <= 14:
    print('Sua categoria de natação é {}INFANTIL{}'.format(cor, ori))
elif ida > 14 and ida <= 19:
    print('Sua categoria de natação é {}JÚNIOR{}'.format(cor, ori))
elif ida == 20:
    print('Sua categoria de natação é {}SÊNIOR{}'.format(cor, ori))
else:
    print('Sua categoria de natação é {}MASTER{}'.format(cor, ori))
