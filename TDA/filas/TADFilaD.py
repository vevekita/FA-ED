from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor: int 

class no:
    def __init__(self, x: item):
        self.dado: item = x
        self.prox: no | None = None

class fila:
    def __init__(self):
        self.inicio: no | None = None
        self.fim: no | None = None
  
    def vazia(self):
        '''
        Verifica se a fila está vazia e retorna True ou False.
        Exemplo:
        >>> f1 = fila()
        >>> f1.vazia()
        True
        >>> f1.enfileira(item(2))
        >>> f1.vazia()
        False
        '''
        return self.inicio == None

    def enfileira(self, x:item):
        '''
        Insere item x na fila.
        Exemplo:
        >>> f1 = fila()
        >>> f1.enfileira(item(2))
        >>> x: int = f1.obtem_primeiro()
        >>> x
        2
        '''
        novo = no(x)
        if self.fim != None:
            self.fim.prox = novo
        else:
            self.inicio = novo   
        self.fim = novo
        
        
    def desenfileira(self):
        '''
        Remove um item que estiver no começo da fila.
        Exemplo:
        >>> f1 = fila()
        >>> f1.enfileira(item(2))
        >>> f1.enfileira(item(3))
        >>> f1.desenfileira()
        2
        >>> x: int = f1.obtem_primeiro()
        >>> x
        3
        '''
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            rem = self.inicio
            self.inicio = rem.prox
            if self.vazia():
                self.fim = self.inicio
            rem.prox = None

            return deepcopy(rem.dado.valor)

    def obtem_primeiro(self) -> int:
        '''
        Mostra o elemento que estiver no começo da fila.
        Exemplo:
        >>> f1 = fila()
        >>> f1.enfileira(item(2))
        >>> f1.enfileira(item(3))
        >>> f1.enfileira(item(4))
        >>> x: int = f1.obtem_primeiro()
        >>> x
        2
        '''

        if self.vazia() == True:
            raise ValueError('Fila vazia')
        else:
            return deepcopy(self.inicio.dado.valor)
        
    def soma(self) -> int:
        fila2 = fila()
        soma = 0
        while self.vazia != True:
            numero = self.desenfileira()
            fila2.enfileira(item(numero))
            soma += numero
        while fila2.vazia() != True:
             self.enfileira(item(fila2.desenfileira()))
        return soma



