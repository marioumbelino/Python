from time import sleep

brasileirao = ('Botafogo', 'Palmeiras', 'Atlético Mineiro', 'Grêmio', 'Flamengo', 'Fluminense', 'Athletico PR', 'São Paulo', 'Cruzeiro', 'Internacional', 'Fortaleza', 'Bragantino', 'Santos', 'Cuiabá', 'Bahia', 'Corinthians', 'América Mineiro', 'Goiás', 'Vasco', 'Curitiba')

print('=' * 30)
print('{:^30}'.format('BRASILEIRÂO 2023'))
print('=' * 30)

sleep(0.5)

print('-' * 30)
print('Os primeiros 5 colocados são:')
print('-' * 30)

for five in range (0, 5):
    sleep(1)
    print(brasileirao[five])
    
sleep(0.5)

print('-' * 80)
print('Os últimos 4 colocados, que estão na zona de rebaixamento até o momento, são:')
print('-' * 80)

for b in range (16, 20):
    sleep(1)
    print(brasileirao[b])
    
sleep(0.5)

print('-' * 30)
print('A tabela em ordem alfabética:')
print('-' * 30)
print(sorted(brasileirao))

sleep(0.5)

print('-' * 100)
print('A Chapecoense não está mais na Série A, e ocupa, atualmente, a 17ª colocação na 2ª divisão do campeonato brasileiro.')
print('-' * 100)
