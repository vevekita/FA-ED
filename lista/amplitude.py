# Projete uma função que calcule a amplitude dos valores de uma lista não vazia de números, isto é, a diferença entre o maior e o menor valor da lista.

def amplitude(numeros: list[int]) -> int:
    '''Calcula a diferença entre o menor e o maior valor de uma lista.
    Exemplos:
    >>> amplitude([6, 2, 7, 10, 3])
    8
    >>> amplitude([50, 48, 12, 63, 14, 57, 80])
    68
    '''
    menor: int = numeros[0]
    maior: int = numeros[0]

    for n in numeros:
        if n <= menor:
            menor = n
        if n >= maior:
            maior = n
    return maior - menor

