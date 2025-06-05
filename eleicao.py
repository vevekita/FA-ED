from enum import Enum, auto

class Resultado(Enum):
    CANDIDATO1 = auto()
    CANDIDATO2 = auto()
    BRANCO = auto()
    
def eleicao(votos: list[Resultado], voto: int) -> Resultado:
    '''Uma eleição possui apenas dois candidatos e o eleitor pode votar em apenas 
    um deles ou em branco. Se os votos em branco forem mais do que 50%, uma nova 
    eleição é realizada.
    A função recebe uma lista de votos e retorna o resultado da eleição.
    Se o primeiro candidato tiver a maior quantidade de votos, então retorna que ele venceu.
    Se o segundo candidato tiver a maior quantidade de votos, então retorna que ele venceu.
    Se os votos em branco forem mais do que 50%, então retorna que haverá uma outra eleição.
    Exemplos:
    >>> eleicao([Resultado.CANDIDATO1, Resultado.CANDIDATO2], Resultado.CANDIDATO1], 1).name
    'CANDIDATO1'
    >>> eleicao([1, 2, 2, 2, 1, 1, 2, 2, 2, 0], 2).name
    'CANDIDATO2'
    >>> eleicao([0, 0, 0, 1, 0 , 1, 2, 0, 0], 3).name
    'BRANCO'
    '''
    totalCandidato1 = 0
    totalCandidato2 = 0
    totalBranco = 0

    for i in votos:
        if i == 1:
            totalCandidato1 += 1
        elif i == 2:
            totalCandidato2 += 1
        elif i == 3:
            totalBranco += 1

    
    if totalCandidato1 > totalCandidato2:
        vencedor: Resultado = Resultado.CANDIDATO1
    elif totalCandidato2 > totalCandidato1:
        vencedor = Resultado.CANDIDATO2
    elif totalBranco > totalCandidato1 + totalCandidato2:
        vencedor = Resultado.BRANCO
    return vencedor