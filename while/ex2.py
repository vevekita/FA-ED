# Projete uma função que verifique se a quantidade de elementos de uma lista de floats é menor que 4.

def quantidade_elementos(lista: list[float]) -> bool:
    '''
    Recebe uma lista de números do tipo float e verifica se a quantidade de elementos
    nessa lista é menor que 4.
    Se for menor, retorna True.
    Se não for, retorna False.
    Exemplos.
    >>> quantidade_elementos([2.20, 4.2, 5.8, 4.63, 5.56])
    False
    >>> quantidade_elementos([2.45, 6.1, 4.6])
    True
    >>> quantidade_elementos([56.7, 48.4, 75.1, 360.0, 41.3, 6.3])
    False
    '''

    resposta: bool = True
    i = 0
    while i < len(lista):
        if i >= 4:
            resposta = False
        i += 1
    return resposta