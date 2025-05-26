def soma_num(numeros: list) -> int:
    '''Recebe uma lista de números e retorna a soma deles.
    Exemplo:
    >>> soma_num([1,2,3])
    6
    '''
    soma: int = 0
    for n in numeros:
        soma = soma + n
    return soma