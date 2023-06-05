res = 's'
num = 0
soma = 0
count = 0
maior = 0
menor = 0
while res in 'Ss':
    num = int(input('Digite um número inteiro: '))
    res = str(input('Você deseja continuar [S/N]? ')).strip().upper()[0]
    soma += num
    count += 1
    if count == 1:
        maior = num
        menor = num
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num
media = soma / count
print('A soma dos números digitados resulta em {} e possui uma média de {}.'.format(soma, media))
print('O maior número digitado foi {}, enquanto que o menor foi {}.'.format(maior, menor))