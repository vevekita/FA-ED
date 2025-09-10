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
            
    def desenfileira(self):
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            self.inicio = self.proximo_indice(self.inicio)

    def obtem_primeiro(self) -> Item:
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            return deepcopy(self.elementos[self.inicio])
