from datetime import date
con = 0
for c in range (1, 8):
    nasc = int(input('Qual é o ano do seu nascimento?? '))
    nasc = date.today().year - nasc
    if nasc >= 21:
        con = con + 1
print('{} pessoas são maiores de idade, e'.format(con))
print('{} pessoas são menores de idade.'.format(7 - con))
