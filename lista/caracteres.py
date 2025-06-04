# Faça uma função que receba como entrada uma lista de caracteres e mais dois 
# caracteres, c1 e c2. Crie uma nova lista trocando todas as ocorrências de c1 por c2.

def troca(caracteres: list[str], c1: str, c2: str) -> list[str]:
    '''Recebe uma lista de caracteres e mais dois outros caracteres, c1 e c2. Depois retorna uma lista trocando todas as ocorrências de c1 por c2
    Exemplos:
    >>> troca(['a', 'b', 'c', 'a', 'd', 'e', 'a'], 'a', 'v')
    ['v', 'b', 'c', 'v', 'd', 'e', 'v']
    >>> troca(['w', 'z', 'z', 'z', 'w'], 'z', 'o')
    ['w', 'o', 'o', 'o', 'w']
    '''
    lista2: list[str] = []
    for i in range(len(caracteres)):
        if caracteres[i] == c1:
            lista2.append(c2)
        else:
            lista2.append(caracteres[i])
    return lista2

    #lista2: list[str] = []
    #for letra in caracteres:
    #    if letra == c1:
    #        lista2.append(c2)
    #    else:
    #        lista2.append(letra)
    #return lista2
    