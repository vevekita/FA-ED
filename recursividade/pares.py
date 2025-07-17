def pares(lista: list[int]) -> bool:
    '''
    Recebe uma lista de números inteiros e verifica se todos são pares.
    Se todos forem pares, retorna True.
    Se ne todos forem, retorna False.
    Exemplos:
    >>> pares([2, 4, 6, 8])
    True
    >>> pares([12, 22, 1])
    False
    '''

    if len(lista) == 0:
        return True
    else:
        if lista[0] % 2 == 0:
            resultado = True
        else:
            resultado = False
    return resultado and pares(lista[1:])