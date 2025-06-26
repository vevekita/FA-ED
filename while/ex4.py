# Um número inteiro é triangular se ele é produto de três inteiros consecutivos.
# Por exemplo, 120 é triangular pois 120 = 4x5x6. Escreva um programa que lê um
# inteiro n e imprime se ele é triangular ou não.

def triangular(numero: int) -> bool:
    '''
    Recebe um número inteiro n e retorna se ele é triangular ou não.
    Para um número ser triangular, ele precisa ser um produto de três números consecutivos.
    Exemplos.
    >>> triangular(120)
    True
    >>> triangular(6)
    True
    >>> triangular(27)
    False
    '''

    i = 0 
    seraTriangular: bool = False
    while seraTriangular == False and numero > i:
        if i*(i + 1)*(i + 2) == numero:
            seraTriangular = True
        i += 1
    return seraTriangular

# Funciona assim: o i inicia em 0. Enquanto o número inserido for maior do que o i, o código funciona.
# O if pega o valor de i e faz as multiplicações ali.
# A primeiro momento vemos que fica 0*1*2 = 0, esse valor não é igual ao valor inserido, então soma 1 ao i.
# Só vai parar quando o seraTriangular for True ou quando o valor de i for maior que o valor do número. (Isso vai acontecer em algum momento
# porque você vai estar sempre adicionando 1 enquanto a condição do if não for estabelecida).