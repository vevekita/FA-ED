def aparece_mais(lista: list[int], elemento: int) -> int:
    '''
    Retorna quantas vezes um elemento aparece na lista.
    Exemplos:
    >>> aparece_mais([1, 5, 1, 7], 1)
    2
    >>> aparece_mais([5, 7, 6, 6, 5, 5, 4, 5], 5)
    4
    '''
    quantidade: int = 0
    if len(lista) == 0:
         return 0
    else:
        quantidade = 0
        if lista[0] == elemento:
            quantidade += 1
        else:
            quantidade = 0
    return quantidade + aparece_mais(lista[1:], elemento)
        