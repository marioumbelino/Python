maior = boy = girl = 0
ordem = 1
while True:
    idade = int(input(f'Quantos anos a {ordem}° pessoa tem? '))
    sexo = str(input(f'Qual é o sexo da {ordem}° pessoa [M/F]? ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input(f'Qual é o sexo da {ordem}° pessoa [M/F]? ')).strip().upper()[0]
    keep = str(input('Deseja acrescentar mais pessoas [S/N]? ')).strip().upper()[0]
    while keep != 'S' and keep != 'N':
        keep = str(input('Deseja acrescentar mais pessoas [S/N]? ')).strip().upper()[0]
    ordem += 1
    if idade > 18:
        maior += 1
    if sexo in 'M':
        boy += 1
    if sexo in 'F' and idade < 20:
        girl += 1
    if keep in 'N':
        break
print(f'Com as informações fornecidads, conclui-se que há {maior} pessoas com mais de 18 anos, \nForam cadastrados {boy} homens. \nE foram cadastradas {girl} mulheres com menos de 20 anos.')