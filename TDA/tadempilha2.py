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
        Insire o item 'x' na pilha.
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
        Remove o item que estiver no topo da pilha.
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

    # def desempilhaMostra(self) -> Item:
    #     '''
    #     Desempilha o topo da pilha e retorna o item desempilhado.
    #     Exemplos:
    #     >>> p1 = Pilha(5)
    #     >>> p1.empilha(Item(2))
    #     >>> p1.empilha(Item(3))
    #     >>> p1.desempilhaMostra().valor
    #     3
    #     '''

    #     if self.vazia():
    #         raise ValueError('Pilha vazia')
    #     else:
    #         self.topo -= 1
    #         return deepcopy(self.elemento[self.topo])
        
    def consulta_topo(self) -> Item:
        '''
        Retorna (apenas mostra) qual o item que está no topo da pilha.
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
        
    # def imprime_ordem_empilhados(self):
    #     '''
    #     Imprime na ordem os items empilhados.
    #     Exemplos:
    #     >>> p1 = Pilha(5)
    #     >>> p1.empilha(Item(1))
    #     >>> p1.empilha(Item(2))
    #     >>> p1.empilha(Item(3))
    #     >>> p1.imprime_ordem_empilhados()
    #     '1 2 3 '
    #     '''
    #     aux_pilha = Pilha(self.tam_maximo)

    #     if self.vazia():
    #         raise ValueError('Pilha vazia')
    #     else:
    #         ordem = '' 
    #         while self.vazia() == False:
    #             aux_pilha.empilha(self.desempilhaMostra())

    #         while aux_pilha.vazia() == False:
    #             ordem += str(aux_pilha.desempilhaMostra().valor) + ' '

    #     return ordem

    def pilha(self, c: Item):
        '''
        Imprime a pilha sem o c.
        Exemplos:
        >>> p1 = Pilha(5)
        >>> p1.empilha(Item(1))
        >>> p1.empilha(Item(2))
        >>> p1.empilha(Item(3))
        >>> p1.pilha(Item(2))
        >>> p1.imprime_ordem_empilhados()
        '1 3 '
        
        '''
        aux_pilha = Pilha(self.tam_maximo)

        if self.vazia():
            raise ValueError('Pilha Vazia') 
        else:
            
            while self.consulta_topo() != c and self.vazia() == False:
                aux_pilha.empilha(self.desempilha())

            while aux_pilha.vazia == False:
                self.empilha(aux_pilha.desempilha())

            



            
