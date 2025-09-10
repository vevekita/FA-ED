from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Item:
    valor: int | None

class Fila:
    def __init__(self, tam_maximo: int):
        self.elementos: list[Item] = [Item(None) for i in range(tam_maximo)]
        self.tamanho = tam_maximo
        self.inicio = 0
        self.fim = 0

    def vazia(self) -> bool:
        return self.inicio == self.fim

    def cheia(self) -> bool:
        return self.proximo_indice(self.fim) == self.inicio
    
    def proximo_indice(self, i: int) -> int:
        return (i + 1) % self.tamanho
    
    def enfileira(self, x: Item):
        if self.cheia():
            raise ValueError('Fila cheia') 
        else:
            self.elementos[self.fim] = deepcopy(x)
            self.fim = self.proximo_indice(self.fim)

    def desenfileira(self) -> Item:
        '''
        Desenfileira o primeiro elemento da fila e retorna
        Exemplo:
        >>> f1 = Fila(5)
        >>> f1.enfileira(Item(1))
        >>> f1.enfileira(Item(2))
        >>> f1.enfileira(Item(3))
        >>> f1.desenfileira().valor
        1
        '''
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            desenfileirado = self.obtem_primeiro()
            self.inicio = self.proximo_indice(self.inicio)
        return desenfileirado

    def obtem_primeiro(self) -> Item:
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            return deepcopy(self.elementos[self.inicio])
        
    def pares(self):
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            elementosPares = ''
            for i in range(self.fim):
                if self.obtem_primeiro().valor % 2 == 0:
                    elementosPares += str(self.obtem_primeiro().valor) + ' '
                self.desenfileira()
        print(elementosPares)





