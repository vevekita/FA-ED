from tadponto import *
# from tadpontosemself import *

def entrada():
    x = 2
    y = 3
    a = 4
    b = 5
    p1 = Ponto.cria_ponto(x, y)
    p2 = Ponto.cria_ponto(a, b)
    print('A distância entre os pontos p1 e p2 é', p1.distancia(p2))

    p1.imprime()

entrada()