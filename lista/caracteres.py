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

    for i in range(len(caracteres)):
        if caracteres[i] == c1:
            caracteres.remove(c1)
            caracteres.insert(i, c2)
    return caracteres