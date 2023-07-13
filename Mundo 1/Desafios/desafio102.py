def fatorial(num, show=False):
    """Calcula o fatorial de um número

    Args:
        num (int): Número a ser calculado
        show (bool, optional): Mostra ou não o cálculo. Defaults to False.

    Returns:
        int: Retorna o resultado do fatorial
    """
    fac = 1
    for c in range(num, 0, -1):
        fac *= c
        if show is True:
            if c != 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
                return fac
    return fac

print(fatorial(5))
