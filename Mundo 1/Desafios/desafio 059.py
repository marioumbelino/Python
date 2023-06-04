menu = 0
n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
while menu != 5:
    print('---- MENU ----')
    print('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA')
    menu = int(input('Qual ação deseja realizar? '))
    if menu == 1:
        res = n1 + n2
        print('O resultado é igual a: {}'.format(res))
    elif menu == 2:
        res = n1 * n2
        print('O resultado é igual a: {}'.format(res))
    elif menu == 3:
        if n1 < n2:
            print('{} é o maior.'.format(n2))
        else:
            print('{} é o maior.'.format(n1))
    elif menu == 4:
        print('Digite novos números')
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))
    elif menu == 5:
        print('Que pena que queira sair do meu programa, volte sempre!!')  
    else:
        print('Resposta inválida, tente novamente!')
print('Fim!')