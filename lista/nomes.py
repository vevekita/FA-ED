# Projete uma função que encontre as posições de todas as ocorrências de um nome em uma lista de nomes.

def posicao_nome(nomes: list[str]) -> list[int]:
    '''Encontra as posições em que um determinado nome aparece.
    Exemplos:
    >>> posicao_nome([Sakai, Komadaki, Emilyn, Komadaki])
    [1, 3]
    >>> posicao_nome([Yuuki, Sakai, Emilyn, Kojiio, Emilyn, Emilyn])
    [2, 4, 5]
    '''

    posicao = []
    nome: str = nomes[0]
    for n in nomes:
        if n == nome:
            
        