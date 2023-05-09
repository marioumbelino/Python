sal = float(input('Digite o seu salário: R$'))
if sal <= 1250.00:
    salf = sal + (sal * 15 / 100)
    print('Para o seu salário no valor de R${:.2f}, o aumento será de 15%, \nobtendo um salário final de R${:.2f}!'.format(sal, salf))
else:
    sal10 = sal + (sal * 10 / 100)
    print('Para o seu salario no valor de R${:.2f}, o aumento será de 10%, \nobtendo um salário final de R${:.2f}!'.format(sal, sal10))
