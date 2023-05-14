from datetime import date
from math import trunc
nasc = int(input('Me informe o ano do seu nascimento: '))
alis = date.today().year
pas = alis - nasc - 18
ant = (alis - nasc - 18) * -1
if alis - nasc == 18:
    print('Já está na hora de você se alistar no Exército Brasileiro. \nAcesse \033[1;31malistamento.eb.mil.br\033[m e aliste-se já.')
elif alis - nasc < 18:
    if ant == 1:
        print("Ainda não chegou sua hora de se alistar no Exército Brasileiro, falta apenas 1 ano. \nLembrando que o alistamento é obrigatório para jovens masculinos que possuem 18 anos ou mais.")
    else:
        print('Ainda não chegou sua hora de se alistar no Exército Brasileiro, faltam {} anos. \nLembrando que o alistamento é obrigatório para jovens masculinos com 18 anos ou mais.'.format(ant))
elif pas == 1:
    print('Já passou do momento de você se alistar!! Se passou 1 ano! \nAcesse o site \033[1;31m"alistamento.eb.mil.br\033[m e aliste-se às forças armadas!')
else:
    print('Já passou do momento de você se alistar!! Já se passaram {} anos! \nAcesse o site \033[1;31m"alistamento.gov.br"\033[m e aliste-se às forças armadas!'.format(trunc(pas)))
