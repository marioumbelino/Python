nuns = 0
soma = 0
count = 0
while nuns != 999:
    nuns = int(input('Digite um número inteiro [Utilize "999" para parar].: '))
    if nuns != 999:
        soma += nuns
        count += 1
print('Foram digitados {} números e a soma destes resulta em {}'.format(count, soma))