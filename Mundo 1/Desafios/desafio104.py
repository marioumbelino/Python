def leiaInt(msg):
    """Lê um número inteiro

    Args:
        msg (str): mensagem que será mostrada para o usuário

    Returns:
        int: retorna um número inteiro
    """
    while True:
        lei = input(msg)
        try:
            lei = int(lei)
            break
        except ValueError:
            print('\033[31mErro!! Digite um número inteiro\033[m')
    return lei

help(leiaInt)
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')
