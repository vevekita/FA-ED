from TADmostraDesenfileirado import *
from TADpilha import *

def pilhaFila(x: Item, pilha: Pilha, fila: Fila):
    if x.valor > 0:
        pilha.empilha(x)
    else:
        fila.enfileira(x)
    
def entrada():
    f1 = Fila(8)
    f2 = Pilha(5)
    f3 = Fila(5)
    n1 = 1
    n2 = -2
    n3 = 3
    n4 = 4
    n5 = 5
    n6 = 6
    n7 = 7
    n8 = 8

    f1.enfileira(Item(n1))
    f1.enfileira(Item(n2))
    f1.enfileira(Item(n3))
    f1.enfileira(Item(n4))
    f1.enfileira(Item(n5))
    # f1.enfileira(Item(n6))
    # f1.enfileira(Item(n7))
    # f1.enfileira(Item(n8))
    pilhaFila(Item(n1), f2, f3)
    pilhaFila(Item(n2), f2, f3)
    print(f2.consulta_topo())
    print(f3.obtem_primeiro())
    f1.pares()


entrada()