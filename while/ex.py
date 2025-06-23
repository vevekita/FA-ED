# Usando while, faça uma função que retorne se um elemento está em uma lista.

def numero_lista(numeros: list[int], num: int) -> bool:
    '''
    Recebe uma lista de números e compara se um número existe nessa lista.
    Se existir, retorna True.
    Se não existir, retorna False.
    Exemplos.
    >>> numero_lista([1, 5, 4, 9, 3, 6], 9)
    True
    >>> numero_lista([12, 45, 36, 0, 4, 87], 45)
    True
    >>> numero_lista([56, 44, 31, 75, 96, 1], 6)
    False
    '''
    resposta: bool = False
    i = 0
    while i < len(numeros):
        if numeros[i] == num:
            resposta = True
        i += 1
    return resposta