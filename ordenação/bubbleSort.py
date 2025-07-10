def bubbleSort(arranjo: list):
    '''
    Recebe uma lista desordenada e retorna ela ordenada usando o método do bubble sort.
    Exemplos.
    >>> lista = [10, 1, 5, 9, 4, 3, 0, 7, 2, 6, 8]
    >>> bubbleSort(lista)
    >>> lista
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
    n = len(arranjo)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arranjo[j] > arranjo[j + 1]:
                aux: int = arranjo[j]
                arranjo[j] = arranjo[j + 1]
                arranjo[j + 1] = aux