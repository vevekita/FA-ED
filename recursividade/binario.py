def binario(lista: list[int]) -> bool:
    '''
    Recebe uma lista de números.
    Verifica se todos os elementos dessa lista são 0 ou 1.
    Se forem, retorna True.
    Se não forem, retorna False.
    Exemplos:
    >>> binario([1, 1, 0, 1, 2])
    False
    >>> binario([0, 0, 1, 0])
    True
    '''

    if len(lista) == 0:
        return True
    else:
        if lista[0] == 0 or lista[0] == 1:
            resultado = True
        else:
            resultado = False
    return resultado and binario(lista[1:])