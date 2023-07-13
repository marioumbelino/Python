def ficha(nome, gols):
    """Função armazena o nome e os gols de um jogador

    Args:
        nome (str): O nome do jogador
        gols (int): Quantidade de gols feito pelo jogador

    Returns:
        str: Retorna qual é o nome jogador e quantos gols ele marcou
    """
    if gols == '':
        gols = 0
    if nome == '':
        nome = '<desconhecido>'
    return f'O jogador {nome} fez {gols} gols no campeonato.'

print(ficha(input('Digite o nome do jogador: '), input('Quantos gols ele marcou?? ')))
