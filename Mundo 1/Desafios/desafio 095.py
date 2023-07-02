from time import sleep
jogador = {}
jogadores = []
gols = []
tot = 0
while True:
    jogador.clear()
    gols.clear()
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    part = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range (0, part):
        gols.append(int(input(f'Quantos gols {jogador["Nome"]} marcou no {c + 1}º jogo? ')))
    jogador['Qtde. Gols'] = gols[:]
    jogador['Total de Gols'] = sum(gols)
    jogador['Aproveitamento'] = round(jogador['Total de Gols'] / part, 2)
    jogadores.append(jogador.copy())
    res = ' '
    while True:
        res = str(input('Deseja acrescentar mais algum jogador? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
        else:
            print('\033[31mErro!!\033[m Tente novamente!')
    if res in 'N':
        break
print('-' * 40)
print(f'{"Cod."} {"Jogador"} {"Tot. Gols":^25}')
for c, v in enumerate(jogadores):
    print(f'{c + 1:^5} {v["Nome"]:<9} {v["Total de Gols"]:>14}')
print('-' * 40)
while True:
    while True:
        more = str(input('Deseja ver os dados detalhados de algum jogador? [S/N] ')).strip().upper()[0]
        if more in 'SN':
            break
        else:
            print('\033[31mErro!!\033[m Tente novamente!')
    if more in 'S':
        while True:
            cod = int(input(('Digite o "Cod." do jogador que deseja visualizar: ')))
            if cod - 1 <= len(jogadores):
                break
            else:
                print('\033[31mErro!!\033[m Este jogador não existe. Por favor, tente novamente!')
        jog = jogadores[cod - 1]
        for p, g in enumerate(jog['Qtde. Gols']):
            print(f'Na partida {p + 1}ª, o {jog["Nome"]} marcou {g} gols')
        print(f'Tendo um aproveitamento de {jog["Aproveitamento"]} gols por jogo')
    else:
        print('Finalizando...')
        sleep(1)
        print('Tenha um bom dia!')
        break
