# Projete uma função que verifique se todos os elementos de uma lista de booleanos são falsos.

def verificar_bool(lista: list) -> str:
    '''Verifica se todos os elementos de uma lista de booleanos são falsos.
    Se forem, retorna que todos são falsos, caso contrário, retorna que nem todos são falsos.
    Exemplos:
    >>> verificar_bool([False, False, False, False])
    'Todos os elementos são falsos.'
    >>> verificar_bool([False, True, True, False, True])
    'Nem todos os elementos são falsos.'
    '''
    for elemento in lista:
        if elemento == True:
            return 'Nem todos os elementos são falsos.'
    return 'Todos os elementos são falsos.'