def ordenacao_selecao(arranjo: list):
    '''
    Recebe uma lista desordenada e retorna ela ordenada usando o método de seleção.
    Exemplos.
    >>> lista = [3, 4, 9, 2, 10, 5, 8, 1, 7, 6]
    >>> ordenacao_selecao(lista)
    >>> lista
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
    n = len(arranjo)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if arranjo[minimo] > arranjo[j]:
                minimo = j
        aux = arranjo[i]
        arranjo[i] = arranjo[minimo]
        arranjo[minimo] = aux