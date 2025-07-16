def maior_elemento(lista: list[int]) -> int:
    '''
    Retorna o maior elemento da lista.
    Exemplos:
    >>> maior_elemento([8, 3, 4, 2])
    8
    >>> maior_elemento([7, 5, 9])
    9
    '''

    if len(lista) == 1:
        return lista[0]
    else:
        maior: int = maior_elemento(lista[1:])
        if lista[0] > maior:
            return lista[0]
        else:
            return maior