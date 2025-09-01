from TADempilhaDesempilha import *

def sequencia():
    '''
    Temos os números 1, 2, 3, 4, 5 e 6. 
    Precisamos obter as sequencias 325641 e 154623.
    O processo para a primeira sequencia será:
    1) inserir o 1;
    2) inserir o 2;
    3) inserir o 3;
    4) retirar o 3;
    5) retirar o 2;
    6) inserir o 4;
    7) inserir o 5;
    8) remover o 5;
    9) inserir o 6;
    10) remover o 6;
    11) remover o 4;
    12) remover o 1. 
    '''

    saida = []
    p1 = Pilha(6)
    n1 = 1
    n2 = 2
    n3 = 3
    n4 = 4
    n5 = 5
    n6 = 6
    
    #acho que tem que adiconar os consulta_topo aqui
    p1.empilha(Item(n1))
    p1.empilha(Item(n2))
    p1.empilha(Item(n3))
    saida.append(p1.desempilha())
    saida.append(p1.desempilha())
    p1.empilha(Item(n4))
    p1.empilha(Item(n5))
    saida.append(p1.desempilha())
    p1.empilha(Item(n6))
    saida.append(p1.desempilha())
    saida.append(p1.desempilha())
    saida.append(p1.desempilha())

    print(saida)

sequencia()