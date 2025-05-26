def maior_num(numeros: list) -> int:
    '''Compara os números de uma lista e retorna o maior deles.
    Exemplos:
    >>> maior_num([5,6,1])
    6'''
    maior: int = 0
    for n in numeros:
        if n > maior:
            maior = n
    return maior
