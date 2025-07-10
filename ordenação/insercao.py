def ordenacao_insercao(arranjo: list):
    '''
    Recebe uma lista desordenada e retorna ela ordenada usando o método de inserção.
    Exemplos:
    >>> lista = [3, 4, 9, 2, 10, 5, 8, 1, 7, 6]
    >>> ordenacao_insercao(lista)
    >>> lista
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    '''
    for i in range(1, len(arranjo)):
        pivo = arranjo[i]
        j = i - 1
        while j >=0 and pivo < arranjo[j]:
            arranjo[j + 1] = arranjo[j]
            j = j -1
        arranjo[j + 1] = pivo