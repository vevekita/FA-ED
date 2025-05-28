def confirmar_senha(senha: str) -> bool:
    '''Verificar se a senha inserida é a senha correta.
    Se ela estiver correta mostrar que está correta e 
    que o acesso está autorizado.
    Se estiver incorreta mostrar que está incorreta e
    que o acesso não foi autorizado.
    Exemplo:
    >>> confirmar_senha("senha")
    True
    >>> confirmar_senha("batata")
    False
    '''

    if(senha == "senha"):
        return True
    else:
        return False
