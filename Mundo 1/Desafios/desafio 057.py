sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Resposta incorreta. Por favor, tente novamente.')
if sexo == 'F':
    print('Seu sexo é feminino')
else:
    print('Seu sexo é masculino')
print('Fim!')