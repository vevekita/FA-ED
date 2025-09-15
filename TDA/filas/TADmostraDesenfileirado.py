# todos os exercícios de fila estão aqui e no arquivo mostraPares.py (tem junto com o TADpilhafila.py também)
from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy
from TDA.filas.TADpilhafila import *

@dataclass
class Item: # tá dando erro, mas ignora, ele funciona
    valor: int | None

class Fila: # com fila circular
    def __init__(self, tam_maximo: int):
        self.elementos: list[Item] = [Item(None) for i in range(tam_maximo + 1)]
        self.tamanho = tam_maximo + 1
        self.inicio = 0
        self.fim = 0

    def vazia(self) -> bool:
        return self.inicio == self.fim

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

    def inverte(self):
        '''
        Recebe uma fila e inverte os elementos.
        Usa uma pilha auxiliar.
        Exemplos:
        >>> f1 = Fila(3)
        >>> f1.enfileira(Item(1))
        >>> f1.enfileira(Item(2)) # se colocar mais um item aqui ele dá erro pq a fila tá cheia, mas funciona (agora não dá mais erro pq aumentei em 1 o tamanho da fila)
        >>> f1.inverte()
        2 1 
        '''
        pilha_aux = Pilha(self.tamanho)
        fila_invertida = Fila(self.tamanho)
        mostra_invertido = ''
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            while self.vazia() != True:
                pilha_aux.empilha(self.desenfileira())
            while pilha_aux.vazia() != True:
                fila_invertida.enfileira(pilha_aux.desempilha())
            while fila_invertida.vazia() != True:
                mostra_invertido += str(fila_invertida.desenfileira().valor) + ' ' 
        print(mostra_invertido)
            




