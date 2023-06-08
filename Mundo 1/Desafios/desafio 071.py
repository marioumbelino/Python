from time import sleep
print('=' * 30)
print('\033[36m{:^30}\033[m'.format('BANCO UMBELINO'))
print('=' * 30)
fifty = twenty = ten = one = 0
saque = int(input('Digite o valor que deseja sacar: R$'))
while saque // 50:
    fifty += 1
    saque -= 50
while saque // 20:
    twenty += 1
    saque -= 20
while saque // 10:
    ten += 1
    saque -= 10
while saque // 1:
    one += 1
    saque -= 1
print('Processando...')
sleep(2)
print('Foram sacadas:')
if fifty > 0:
    print(f'{fifty} notas de 50 reais.')
if twenty > 0:
    print(f'{twenty} notas de 20 reais.')
if ten > 0:
    print(f'{ten} notas de 10 reais.')
if one > 0:
    print(f'{one} moeadas de 1 real.')