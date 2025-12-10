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

class lista:
    def __init__(self):
        self.primeiro: no = no(item(0))
        self.ultimo: no = self.primeiro

class Conjunto:
    '''
    Implementa operações sobre um conjunto de dados.
    Exemplos:
    >>> c1 = Conjunto()
    >>> c2 = Conjunto()
    >>> c1.adiciona(2)
    >>> c1.adiciona(3)
    >>> c1.adiciona(4)
    >>> c1.mostra()
    '{2,3,4}'
    >>> c2.adiciona(1)
    >>> c2.adiciona(2)
    >>> c2.adiciona(4)
    >>> c2.mostra()
    '{1,2,4}'
    >>> c3 = Conjunto()
    >>> c3 = c1.union(c2)
    >>> c3.mostra()
    '{1,2,3,4}'
    '''
    def __init__(self):
        '''Cria um novo conjunto vazio.'''
        self.lista = [lista() for i in range (10)]

    def adiciona(self, n1: int):
        '''Adiciona o *n1* ao conjunto.
        Exemplos:
        >>> c = Conjunto()
        >>> c.adiciona(3)
        >>> c.adiciona(1)
        >>> c.adiciona(5)
        >>> c.mostra()
        '{1,3,5}'
        '''
        indice: int = n1 % 10
        ptr = self.lista[indice].primeiro.prox
        while ptr != None:
            if ptr.dado.valor == n1:
                return None
            ptr = ptr.prox
        self.lista[indice].ultimo.prox = no(item(n1))
        self.lista[indice].ultimo = self.lista[indice].ultimo.prox

    def mostra(self) -> str:
        '''
        Cria uma string com os elementos entre chaves e separados por vírgula.
        Exemplos:
        >>> c = Conjunto()
        >>> c.adiciona(4)
        >>> c.adiciona(2)
        >>> c.adiciona(6)
        >>> c.mostra()
        '{2,4,6}'
        '''
        resultado: str = ''
        for n in range(7):
            ptr = self.lista[n].primeiro.prox
            while ptr != None:
                resultado += str(ptr.dado.valor) + ','
                ptr = ptr.prox
        if len(resultado) >= 2:
            resultado = resultado[:-1]
        return '{' + resultado + '}'
    
    def union(self, c2: Conjunto) -> Conjunto:
        '''
        Retorna um novo conjunto que é a união do conjunto atual com o *c2*.
        Exemplos:
        >>> c1 = Conjunto()
        >>> c1.adiciona(2)
        >>> c1.adiciona(3)
        >>> c1.adiciona(4)
        >>> c2 = Conjunto()
        >>> c2.adiciona(1)
        >>> c2.adiciona(2)
        >>> c2.adiciona(4)
        >>> c3 = Conjunto()
        >>> c3 = c1.union(c2)
        >>> c3.mostra()
        '{1,2,3,4}'
        '''
        c3 = deepcopy(self)
        for n in range(7):
            ptr = c2.lista[n].primeiro.prox
            while ptr != None:
                c3.adiciona(ptr.dado.valor)
                ptr = ptr.prox
        return c3
    