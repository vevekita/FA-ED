def soma_elementos(lista1: list[int]) -> int:
    '''
    Retorna a soma de todos os elementos da lista1.
    Exemplos:
    >>> soma_elementos([3, 5, 2, 4])
    14
    >>> soma_elementos([1, 6])
    7
    '''

    if len(lista1) == 0:
        return 0
    else:
        return soma_elementos(lista1[1:]) + lista1[0]