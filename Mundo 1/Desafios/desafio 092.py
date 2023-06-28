import datetime
pessoas = []
pessoas['Nome'] = str(input('Digite o nome: '))
nasc = int(input('Digite o ano de nascimento: '))
ctps = str(input('Você tem carteira de trabalho? [S/N] ')).strip()[0]
Pessoas['Idade'] = datetime.date.today().year - nasc
if ctps in 'Ss':
    numctps = int(input('Digite o número da sua carteira de trabalho: '))
    contract = int(input('Digite o ano de contratação: '))
    sal = float(input('Qual é o seu salário? R$'))
    pessoa['Ano de Contratação'] = contract
    pessoa['Salário'] = sal
    apos = contract - nasc + 35
print('-' * 20, 'Resultado', '-' * 20)
print(f'O nome cadastrado é {pessoas["Nome"]}.')
print(f'Sua idade é {pessoas['Idade]} anos.')
if ctps in 'Ss':
    print(f'O número da sua carteira de trabalho é: {numctps}')
    print(f'Foi contratado no ano de {contract} e possui um salário de R${sal:.2f}.')
    print(f'Com isso, poderá se aposentar com {apos} anos.')
else:
    print('A pessoa cadastrada não possui carteira de trabalho.')


