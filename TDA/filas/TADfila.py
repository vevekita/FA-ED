from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Item:
    valor: int | None

class Fila:
    def __init__(self, tam_maximo: int):
        self.elementos: list[Item] = [Item(None)] * tam_maximo
        self.tam_maximo = tam_maximo
        self.fim = 0

    def vazia(self) -> bool:
        '''
        Verifica se uma fila está vazia e retorna True se sim.
        Exemplos:
        >>> f1 = Fila(5)
        >>> f1.vazia()
        True
        >>> f1.enfileira(Item(2))
        >>> f1.vazia()
        False
        '''
        return self.fim == 0
    
    def cheia(self) -> bool:
        '''
        Verifica se uma fila está cheia, ou seja, se atingiu o tam_maximo definido.
        Retorna True ou False.
        Exemplos:
        >>> f1 = Fila(2)
        >>> f1.cheia()
        False
        >>> f1.enfileira(Item(2))
        >>> f1.enfileira(Item(3))
        >>> f1.cheia()
        True
        '''
        return self.fim == self.tam_maximo
    
    def enfileira(self, x: Item):
        ''' Insere o item x na fila.
        Exemplos:
        >>> f1 = Fila(5)
        >>> f1.enfileira(Item(2))
        >>> x: int = f1.obtem_primeiro().valor
        >>> x
        2
        '''
        if self.cheia():
            raise ValueError('Fila cheia')
        else:
            self.elementos[self.fim] = deepcopy(x)
            self.fim += 1

    def desenfileira(self):
        '''
        Retorna o primeiro elemento da fila.
        Exemplos:
        >>> f1 = Fila(5)
        >>> f1.enfileira(Item(2))
        >>> f1.enfileira(Item(3))
        >>> f1.enfileira(Item(4))
        >>> f1.desenfileira()
        >>> x: int = f1.obtem_primeiro().valor
        >>> x
        3
        '''
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            for i in range(1, self.fim):
                self.elementos[i - 1] = self.elementos[i]
            self.fim -= 1

    def obtem_primeiro(self) -> Item:
        '''
        Retorna qual o item que está na primeira posição da fila.
        >>> f1 = Fila(5)
        >>> f1.enfileira(Item(2))
        >>> f1.enfileira(Item(3))
        >>> n: int = f1.obtem_primeiro().valor
        >>> n
        2
        '''
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            return deepcopy(self.elementos[0])