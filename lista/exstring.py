# Projete uma função que recebe como parâmentro dois campos: o nome e o sobrenome de uma pessoa. E retorne sobrenome, nome.
def nome_completo(nome: str, sobrenome: str) -> str:
    '''Recebe um nome e um sobrenome e retorna o sobrenome primeiro e depois o nome separado por vírgula.
    Exemplos.
    >>> nome_completo('Verônica', 'Kitamura')
    'Kitamura, Verônica'
    >>> nome_completo('Emilyn', 'Nascimento')
    'Nascimento, Emilyn'
    '''
    return sobrenome + ', ' + nome    