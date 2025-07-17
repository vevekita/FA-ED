def crescente(lista: list[int]) -> bool:
    '''
    Recebe uma lista de inteiros.
    Verifica se todos os elementos estão em ordem crescente.
    Ou seja, o próximo elemento tem que ser maior ou igual ao anterior.
    Se todos fore, retorna True.
    Senão, retorna False.
    Exemplos:
    >>> crescente([1, 2, 3, 4])
    True
    >>> crescente([1, 2, 2, 3, 5, 5, 7])
    True
    >>> crescente([5, 4, 3, 2, 1])
    False
    '''
    if len(lista) <= 1:
       return True  
    else:
        if lista[0] <= lista[1]:
            resultado = True
        else:
            resultado = False

    return resultado and crescente(lista[1:])