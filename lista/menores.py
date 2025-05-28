# Projete uma função que verifique quantos elementos de uma lista de inteiros são menores que 10.

def menores(inteiros: list) -> int:
    '''Verifica quantos números de uma lista são menores que 10 e retorna
    Exemplos:
    >>> menores([1, 5, 11, 9, 23])
    2
    >>> menores([54, 25, 14, 18, 6])
    4
    '''
    total: int = 0
    for elementos in inteiros:
        if elementos > 10:
            total = total + 1
    return total