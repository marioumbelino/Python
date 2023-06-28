jogador = {}
gols = []
tot = 0
jogador['Nome'] = str(input('Digite o nome do jogador: '))
part = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range (0, part):
    gols.append(int(input(f'Quantos gols {jogador["Nome"]} marcou no {c + 1}º jogo? ')))
jogador['Qtde. Gols'] = gols[:]
jogador['Total de Gols'] = sum(gols)
jogador['Aproveitamento'] = jogador['Total de Gols'] / part
print('-' * 30)
print(f'{jogador["Nome"]} jogou {len(jogador["Qtde. Gols"])} partidas:')
for c in range(0, part):
    print(f'Na {c + 1}º partida, {jogador["Nome"]} marcou {gols[c]} gols.')
print(f'Tendo um total de {jogador["Total de Gols"]} gols.')
print(f'E um aproveitamento de {jogador["Aproveitamento"]} gols por jogo.')
print('-' * 30)
