from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Item:
    valor: int | None

class Pilha:
    def __init__(self, tam_maximo: int):
        self.elemento: list[Item] = [Item(None)]*tam_maximo
        self.tam_maximo = tam_maximo
        self.topo = 0

    def vazia(self) -> bool:
        '''
        Verifica se uma pilha está vazia e retorna True se sim.
        Exemplos:
        >>> p1 = Pilha(5)
        >>> p1.vazia()
        True
        >>> p1.empilha(Item(2))
        >>> p1.vazia()
        False
        '''

        return self.topo == 0
    
    def cheia(self) -> bool:
        '''
        Verifica se uma pilha está cheia, ou seja, se atingiu o tam_maximo definido.
        Retorna True ou False.
        Exemplos:
        >>> p1 = Pilha(2)
        >>> p1.cheia()
        False
        >>> p1.empilha(Item(3))
        >>> p1.empilha(Item(1))
        >>> p1.cheia()
        True
        '''

        return self.topo == self.tam_maximo
    
    def empilha(self, x: Item):
        '''
        Insire o Item 'x' na pilha.
        Exemplos:
        >>> p1 = Pilha(5)
        >>> p1.empilha(Item(4))
        >>> x: int = p1.consulta_topo().valor
        >>> x
        4
        '''

        if self.cheia():
            raise ValueError('Pilha cheia')
        else:
            self.elemento[self.topo] = deepcopy(x)
            self.topo += 1

    def desempilha(self):
        '''
        Remove o Item que estiver no topo da pilha.
        Exemplos:
        >>> p1 = Pilha(5)
        >>> p1.empilha(Item(2))
        >>> p1.empilha(Item(7))
        >>> p1.desempilha()
        >>> x: int = p1.consulta_topo().valor
        >>> x
        2
        '''

        if self.vazia():
            raise ValueError('Pilha vazia')
        else:
            self.topo -= 1

    def consulta_topo(self) -> Item:
        '''
        Retorna (apenas mostra) qual o Item que está no topo da pilha.
        >>> p1 = Pilha(5)
        >>> p1.empilha(Item(2))
        >>> p1.empilha(Item(7))
        >>> n: int = p1.consulta_topo().valor
        >>> n 
        7
        '''

        if self.vazia():
            raise ValueError('Pilha vazia')
        else:
            return deepcopy(self.elemento[self.topo-1])