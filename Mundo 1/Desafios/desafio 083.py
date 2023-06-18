exp = str(input('Digite uma expressão matemática: ')).strip()
lista = []
count = count2 = 0
for p in exp:
    if '(' in p:
        lista.append('(')
    elif ')' in p:
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('Sua expressão está certa!')
else:
    print('Sua expressão está incorreta!')