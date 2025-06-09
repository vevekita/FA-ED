# Considere uma função que recebe como parâmetro um nome e converta no formato sobrenome, nome. Ex: nome = 'José da Silva' --> 'Silva, José da'
def nome_completo(nomeCompleto: str) -> str:
    '''Recebe um nome completo e depois retorna o sobrenome seguido do restante do nome separado por uma vírgula
    Exemplos:
    >>> nome_completo('Verônica Manami Kitamura')
    'Kitamura, Verônica Manami'
    >>> nome_completo('Victor Komadaki Lorenzzi da Silva)
    'Silva, Victor Komadaki Lorenzzi da'
    '''
    for i in range(len(nomeCompleto)):
        if nomeCompleto[i] == ' ':
            nome = nomeCompleto[-i]
    return nome 
            
