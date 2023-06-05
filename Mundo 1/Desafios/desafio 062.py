num = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão desta PA: '))
count = 0
x = 1
count2 = 2
while count < 10:
    pa = num + (x - 1) * raz
    print(pa)
    count += 1
    count2 += 1
    x += 1
cont = str(input('Quer mostrar mais alguns termos [S/N]?? '))
while cont in 'Ss':
    qtde = int(input('Mais quantos termos quer mostrar?? '))
    print('Certo, a seguir, temos mais {} termo(s) da PA: '.format(qtde))
    count = 0
    while count < qtde:
        pa = num + (x - 1) * raz
        print(pa)
        count += 1
        count2 += 1
        x += 1
    cont = str(input('Quer mostrar mais alguns termos [S/N]?? '))
if cont in 'Nn':
    print('Tudo bem, foram mostrados {} termos. \nQuando quiser saber os termos de alguma PA, basta executar o programa novamente. \nTenha um ótimo dia!'.format(count2 - 2))
else:
    print('\033[31mErro\033[m! Tente novamente!')