# Projete uma função que conte quantas vezes o valor mínimo de uma lista de inteiros não vazia aparece na lista.

def valor_minimo(valor: list) -> int:
    '''Verifica quantas vezes o valor mínimo de uma lista de inteiros não vazia aparece.
    Exemplos:
    >>> valor_minimo([1, 5, 9, 1, 23])
    2
    >>> valor_minimo([12, 5, 5, 14, 5, 16, 5])
    4'''
    minimo = valor[0]
    total: int = 0
    for elemento in valor:
        if elemento <= minimo:
            minimo = elemento
    for i in valor:
        if i == minimo:
            total = total + 1
    return total 
