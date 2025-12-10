from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor: int

class no:
    def __init__(self, dado: item):
        self.esq: no | None = None
        self.dir: no | None = None
        self.dado: item = dado

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
        self.raiz: no | None = None

    def adiciona(self, n1: int) -> None:
        '''
        Adiciona o *n1* ao conjunto.
        Exemplos:
        >>> c = Conjunto()
        >>> c.adiciona(3)
        >>> c.adiciona(1)
        >>> c.adiciona(5)
        >>> c.mostra()
        '{1,3,5}'
        '''
        self.raiz = self.insere_no(self.raiz, n1)

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
        resultado = self.InOrdem(self.raiz)
        if len(resultado) >= 2:
            resultado = resultado[:-1]
        return '{' + resultado + '}'

    def union(self, c2: Conjunto) -> Conjunto:
        '''
        Realiza a união entre dois conjuntos
        '''
        conjunto_unido = Conjunto()
        conjunto_unido.adiciona(self.raiz.esq.valor)
        conjunto_unido.adiciona(self.no.dir.valor)
        conjunto_unido.adiciona(c2.no.esq.valor)
        conjunto_unido.adiciona(c2.no.dir.valor)
        return conjunto_unido

    def insere_no(self, n: no , x: int) -> no | None:
            if n == None:
                n = no(item(valor=deepcopy(x)))
            elif x > n.dado.valor:
                n.dir = self.insere_no(n.dir, x)
            elif x < n.dado.valor:
                n.esq = self.insere_no(n.esq, x)
            return n
    
    def InOrdem(self, no) -> str:
        '''
        Mostra o conjunto em ordem ERD (Esquerda, Raiz e Direita).
        Portanto, percorre o lado esquerdo do conjunto e vai mostrando, depois mostra a raiz e percorre e mostra
        o lado direito do conjunto. Inclusive, mostra todos os elementos em ordem crescente.
        Exemplos:
        >>> c = Conjunto()
        >>> c.adiciona(4)
        >>> c.adiciona(2)
        >>> c.adiciona(6)
        >>> c.InOrdem(c.raiz)
        '2,4,6,'
        '''
        resultado = ''
        if no != None:
            resultado += self.InOrdem(no.esq)
            resultado += str(no.dado.valor) + ','
            resultado += self.InOrdem(no.dir)
        return resultado