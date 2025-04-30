def tipos_triangulos(x: float, y: float, z: float) -> str:
    '''Determinar se é possível formar um triângulo com as medidas recebidas,
    levando em consideração que para ser um triângulo é necessário que o comprimento
    de um dos lados seja menor do que a soma dos outros dois lados.
    Se essa condição for atendida, deve dizer se o triângulo é isósceles (com dois 
    lados iguais), equilátero (todos os lados iguais) ou escaleno (todos os lados diferentes)
    Exemplos:
    >>> tipos_triangulos(3, 4, 4)
    'Triângulo Isósceles'
    >>> tipos_triangulos(2, 2, 2)
    'Triângulo Equilátero'
    >>> tipos_triangulos(5, 6, 7)
    'Triângulo Escaleno'
    >>> tipos_triangulos(0.5, 1, 0.3)
    'Não é triângulo'
    '''
    if(x + y > z and x + z > y and z + y > x):
        if(x == y and z == x):
            return("Triângulo Equilátero")
        elif((x == y) or (x == z) or (y == z)):
            return("Triângulo Isósceles")
        else:
            return("Triângulo Escaleno")
    else:
        return("Não é triângulo")