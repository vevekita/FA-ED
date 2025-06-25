def numero_primo(num: int) -> bool: # Admito que não sei porquê deu certo.
    '''
    Recebe um número e verifica se ele é um número primo ou não.
    Se for, retorna True.
    Se não for, retorna False.
    >>> numero_primo(2)
    True
    >>> numero_primo(9)
    False
    '''
    i = 0
    resposta: bool = True
    primo = int(num/2 + 1)
    while num > i and resposta == True:
        if num % primo != 0:
            resposta = False
        i += 1
    return resposta

# Exemplo do professor
# def primo(n: int) -> bool:
#     '''
#     Verifica se 'n' é um número primo e retorna True ou False.
#     Exemplos.
#     >>> primo(8)
#     False
#     >>> primo(11)
#     True
#     '''
#     resp = True
#     for i in range(2, int(n/2 + 1)):
#         if n % i == 0:
#             resp = False
#     return resp