def positivos(lst: list[int]) -> list[int]:
    '''Recebe uma lista de números inteiros positivos e retorna uma lista com os números negativos da lista antes dos positivos.
    Exemplos:
    >>> positivos([1, 2, 3, 4])
    [-1, -2, -3, -4, 1, 2, 3, 4]
    >>> positivos([5, 6, 7])
    [-5, -6, -7, 5, 6, 7]
    '''
    negativos: list[int] = [] 
    for i in lst:
        nNegativo = i * -1
        negativos.append(nNegativo)
    for i in lst:
        negativos.append(i)
    return negativos