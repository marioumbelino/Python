num = int(input('Digite o primeiro termo da PA: '))
raz = int(input('Digite a razão desta PA: '))
count = 0
x = 1
while count < 10:
    pa = num + (x - 1) * raz
    print(pa)
    count += 1
    x += 1
cont = str(input('Quer mostrar mais alguns termos [S/N]?? '))
if cont in 'Ss':
    qtde = int(input('Mais quantos termos quer mostrar?? '))
    print('Certo, a seguir, temos mais {} termos da PA: '.format(qtde))
    count = 0
    while count < qtde:
        pa = num + (x - 1) * raz
        print(pa)
        count += 1
        x += 1
elif cont in 'Nn':
    print('Tudo bem, quando quiser saber os termos de alguma PA, basta executar o programa novamente. Tenha um ótimo dia!')
else:
    print('\033[31mErro\033[m! Tente novamente!')