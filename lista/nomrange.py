def posicao_nome(nomes: list[str], n: str) -> list[int]:
    '''Encontra as posições em que um determinado nome aparece.
    Exemplos:
    >>> posicao_nome(['Sakai', 'Komadaki', 'Emilyn', 'Komadaki'], 'Komadaki')
    [1, 3]
    >>> posicao_nome(['Yuuki', 'Sakai', 'Emilyn', 'Kojiio', 'Emilyn', 'Emilyn'], 'Emilyn')
    [2, 4, 5]
    '''

    posicao = []
    for i in range(len(nomes)):
        if nomes[i] == n:
            posicao.append(i)
    return posicao