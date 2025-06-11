# Considere uma função que recebe como parâmetro um nome e converta no formato sobrenome, nome. Ex: nome = 'José da Silva' --> 'Silva, José da'
def nome_completo(nomeCompleto: str) -> str:
    '''
    Recebe um nome completo e depois retorna o sobrenome seguido do restante do nome separado por uma vírgula
    Exemplos:
    >>> nome_completo('Verônica Manami Kitamura')
    'Kitamura, Verônica Manami'
    >>> nome_completo('Victor Komadaki Lorenzzi da Silva')
    'Silva, Victor Komadaki Lorenzzi da'
    '''
    posicao_ultimo_espaco = 0
    for i in range(len(nomeCompleto)):
        if nomeCompleto[i] == ' ':
            posicao_ultimo_espaco = i

    ultimo_nome = nomeCompleto[posicao_ultimo_espaco +1:]
    resto_nome = nomeCompleto[:posicao_ultimo_espaco]
    
    nome_resultado = ultimo_nome + ', ' + resto_nome        
    return nome_resultado 
          
