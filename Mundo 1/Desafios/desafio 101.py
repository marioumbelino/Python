from datetime import date
def voto(idade):
    """Função que calcula a idade e retorna, com base no ano de nascimento, 
    a situação do voto no Brasil para a idade.

    Args:
        idade (ano de nascimento): lê o ANO de nascimento de alguém

    Returns:
        NEGADO: Se a idade for menor de 16 anos;
        OPCIONAL: Se a idade estiver entre 16 e 17 anos ou acima de 65 anos;
        OBRIGATÓRIO: Se a idade estiver entre 18 e 64 anos
    """
    ida = date.today().year - idade
    if ida < 16:
        return 'seu voto foi \033[31mNEGADO\033[m.'
    elif 16 <= ida < 18 or ida >= 65:
        return 'seu voto é \033[33mOPCIONAL\033[m.'
    else:
        return 'seu voto é \033[32mOBRIGATÓRIO\033[m.'

nasc = int(input('Digite o ano do seu nascimento: '))
print(f'Com {date.today().year - nasc} anos, {voto(nasc)}')
