si = 0
nm = ''
im = 0
m20 = 0
for c in range (1, 5):
    print('-=-' * 5)
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o seu sexo (M/F): ')).lower().strip()
    si += idade
    if c == 1 and 'm' in sexo:
        im = idade
        nm = nome
    if 'm' in sexo and idade > im:
        im = idade
        nm = nome
    if 'f' in sexo and idade < 20:
        m20 += 1
print('\033[36mA média de idade é igual a {}'.format(si / 4))
print('O homem mais velho tem {} e se chama {}'.format(im, nm.capitalize()))
print('Há {} mulheres com menos de 20 anos\033[m'.format(m20))