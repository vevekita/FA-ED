# Projete uma função que receba como entrada um arranjo de números, uma posição i e um número n e devolve 
# um novo arranjo com n adicionado na posição i do arranjo de entrada.

def posicao(arranjo: list[int], pos: int, num: int) -> list[int]:
    '''Recebe um arranjo de números, uma posição i e um número n. Devolve um arranjo com n adicionado na posição i
    Exemplos:
    >>> posicao([1, 45, 63, 3, 5], 3, 6)
    [1, 45, 63, 6, 3, 5]
    >>> posicao([2, 3, 5, 7], 2, 4)
    [2, 3, 4, 5, 7]
    >>> posicao([0, 1, 2, 3, 4, 5, 6], 1, 1)
    [0, 1, 1, 2, 3, 4, 5, 6]
    '''
    #elemento = arranjo[i]
    #for num in range(len(arranjo)):
    #    if arranjo[num] == elemento:
    #        arranjo.insert(i, n)
    #    elemento = arranjo[i + 1] 
    #return arranjo
    
    aux: list[int] = []
    for i in range(len(arranjo)):
        if i == pos:
            aux.append(num)
        aux.append(arranjo[i])
    return aux

print(posicao([1, 45, 63, 3, 5], 3, 6))