# Projete uma função que encontre as posições de todas as ocorrências de um nome em uma lista de nomes.

def posicao_nome(nomes: list[str], n: str) -> list[int]:
    '''Encontra as posições em que um determinado nome aparece.
    Exemplos:
    >>> posicao_nome(['Sakai', 'Komadaki', 'Emilyn', 'Komadaki'], 'Komadaki')
    [1, 3]
    >>> posicao_nome(['Yuuki', 'Sakai', 'Emilyn', 'Kojiio', 'Emilyn', 'Emilyn'], 'Emilyn')
    [2, 4, 5]
    '''

    posicao = []
    i: int = 0
    for elemento in nomes:
        if elemento == n:
            posicao.append(i)
        i += 1 #com o range não precisa dessa parte
    return posicao
        