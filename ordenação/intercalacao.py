def ordena_intercalado(lista1: list[int], lista2: list[int]) -> list[int]:
    '''
    Recebe duas listas numéricas ordenadas e retorna um arranjo ordenado que seja
    o resultado da intercalação desses dois arranjos.
    Exemplos.
    >>> lista1 = [1, 3, 5, 7, 9]
    >>> lista2 = [2, 4, 6, 8]
    >>> ordena_intercalado(lista1, lista2)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''
    indiceLista1 = 0
    indiceLista2 = 0
    lista_intercalada = []

    while indiceLista1 < len(lista1) and indiceLista2 < len(lista2):
        if lista1[indiceLista1] < lista2[indiceLista2]:
            lista_intercalada.append(lista1[indiceLista1])
            indiceLista1 += 1
        else:
            lista_intercalada.append(lista2[indiceLista2])
            indiceLista2 += 1

    while indiceLista1 < len(lista1):
        lista_intercalada.append(lista1[indiceLista1])
        indiceLista1 += 1

    while indiceLista2 < len(lista2):
        lista_intercalada.append(lista2[indiceLista2])
        indiceLista2 += 1
        
    return lista_intercalada
        

