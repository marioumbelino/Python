def notas(*n, sit=False):
    """Mostra o total de notas, a maior e a menor nota, e a média das notas. Ademais, pode mostrar, ainda, a situação (opcional)

    Args:
        sit (bool, optional): Mostrar ou não a situação. Defaults to False.

    Returns:
        dict: retorna um dicionários contendo as informações. 
    """
    média = sum(n) / len(n)
    grades = {}
    grades['Total'] = len(n)
    grades['Maior Nota'] = max(n)
    grades['Menor Nota'] = min(n)
    grades['Média'] = média
    if sit is True:
        if média < 5:
            grades['Situação'] = 'Ruim'
        elif 5 <= média < 7:
            grades['Situação'] = 'Razoável'
        elif 7 <= média  < 9:
            grades['Situação'] = 'Boa'
        else:
            grades['Situação'] = 'Ótima!'
    return grades
print(notas(9, 10, 8.5, 9.5, 9))
