def comparar(gabarito: list[list[str]], prova: list[list[str]]) -> int:
    '''
    Recebe duas matrizes com 5 linhas e 4 colunas, uma representando o gabarito de uma prova
    e a outra a prova do candidato.
    Na matriz temos o 'x' representando a resposta correta e o 'o' a resposta incorreta.
    Retorna a quantidade de acertos desse candidato.
    Exemplos:
    >>> gabarito1 = [['o', 'o', 'o', 'x'], ['o', 'x', 'o', 'o'], ['x', 'o', 'o', 'o'], ['o', 'o', 'x', 'o'], ['x', 'o', 'o', 'o']]
    >>> prova1 = [['o', 'o', 'o', 'x'], ['x', 'o', 'o', 'o'], ['o', 'x', 'o', 'o'], ['o', 'o', 'x', 'o'], ['o', 'x', 'o', 'o']]
    >>> comparar(gabarito1, prova1)
    2
    '''

    acertos: int = 0
    linhas = 5
    colunas = 4
    listasErradas: int = 0
    for i in range(linhas):
        for j in range(colunas):
            if prova[i][j] != gabarito[i][j]:
                acertos += 1
        
    return acertos

    
    # Quando uso o range(len()) pra ler uma lista de lista, ele considera cada lista dentro da lista um índice 
    # ou os elementos dentro da lista dentro da lista como o índice?