from math import trunc
from time import sleep
print('-=-' * 10)
print ('\033[36mBanco Umbelino\033[m')
print('-=-' * 10)
print('Para financiar um casa, precisamos de algumas informações antes:.')
casa = float(input('Qual é o valor total da casa? '))
sal = float(input('Me informe seu salário mensal: '))
ano = int(input('Em quantos anos pretende pagar? '))
print('Processando informações, verificando sua situação...')
sleep(3)
pcl = casa / (ano * 12 )
if pcl <= (sal - (sal * 70 / 100)):
    print('Para financiar uma casa no valor de R$\033[1;33m{:.2f}\033[m em \033[1;37m{}\033[m anos, você terá parcelas mensais no valor de R${:.2f}. \nPortanto, seu emprestimo foi \033[1;32mACEITO\033[m!'.format(casa, trunc(ano), pcl))
else:
    print('Para financiar uma casa no valor de R${:.2f} em {} anos, seria necessário pagar uma prestação de R${:.2f}. \nSeu salário é insuficiente para financiar essa casa, portanto, seu emprestimo foi \033[1;31mNEGADO\033[m!'.format(casa, ano, pcl))
