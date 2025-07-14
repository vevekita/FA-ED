def soma_naturais(n: int) -> int:
    '''
    Recebe um número n natural e retorna a soma de todos os números 
    até esse n natural.
    Exemplos.
    >>> soma_naturais(5)
    15
    >>> soma_naturais(2)
    3
    '''
    if n == 0:
        return 0
    else:
        return n + soma_naturais(n - 1)

print(soma_naturais(5))

