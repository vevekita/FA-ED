def alfabeto(lista: list[str]):
    '''
    Recebe uma lista com letras desordenadas e retorna as letras em ordem alfabética 
    utilizando do método de inserção.
    Exemplos.
    >>> alfa = ['a', 'z', 'c', 'r']
    >>> alfabeto(alfa)
    >>> alfa
    ['a', 'c', 'r', 'z']
    '''
    for i in range(1, len(lista)):
        pivo = lista[i]
        j = i - 1
        while j >= 0 and pivo < lista[j]:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = pivo


