from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class item:
    valor: float

class no:
    def __init__(self, dado: item):
        self.esq: no | None = None
        self.dir: no | None = None
        self.dado: item = dado

class arvore:
    def __init__(self):
        self.raiz: no | None = None

    def vazia(self):
        '''
        Verifica se a árvore está vazia.
        Exemplos:
        >>> a = arvore()
        >>> a.vazia()
        True
        >>> a.insere(item(3))
        >>> a.vazia()
        False
        '''
        return self.raiz == None
    
    def insere(self, x:item):
        '''
        Insere o x na árvore.
        Exemplos:
        >>> a = arvore()
        >>> a.insere(item(3))
        >>> a.insere(item(1))
        >>> a.insere(item(5))
        >>> a.PreOrdem()
        item(valor=3)
        item(valor=1)
        item(valor=5)
        '''
        self.raiz = self.insere_no(self.raiz, x)
    
    def busca(self, ch:int) -> item | None:
        '''
        Procura na árvore se a chave "ch" existe, se existir, retorna ela.
        Caso contrário, retorna None.
        Exemplos:
        >>> a = arvore()
        >>> a.insere(item(5))
        >>> a.insere(item(4))
        >>> a.insere(item(2))
        >>> a.busca(2)
        item(valor=2)
        >>> a.busca(6)
        '''
        no = self.busca_no(self.raiz, ch)
        if no != None:
            return no.dado
        else:
            return None
    
    def remove(self, chave: int):
        '''
        Remove o número "chave" da árvore.
        Exemplos:
        >>> a = arvore()
        >>> a.insere(item(4))
        >>> a.insere(item(1))
        >>> a.insere(item(5))
        >>> a.remove(1)
        >>> a.PreOrdem()
        item(valor=4)
        item(valor=5)
        '''
        self.raiz = self.remove_no(self.raiz, chave)

    def busca_no(self, n: no, num:int) -> no | None:
        if n == None:
            return None
        elif num > n.dado.valor:
            return self.busca_no(n.dir, num)
        elif num < n.dado.valor:
            return self.busca_no(n.esq, num)
        else:
            return n
        
    def insere_no(self, n: no , x: item) -> no | None:
        if n == None:
            n = no(deepcopy(x))
        elif x.valor > n.dado.valor:
            n.dir = self.insere_no(n.dir,x)
        elif x.valor < n.dado.valor:
            n.esq = self.insere_no(n.esq,x)
        return n

    def maior(self, n: no) -> no:
        if n.dir == None:
            return n
        else:
            return self.maior(n.dir)
    
    def remove_no(self, n: no, chave: int) -> no | None:
        if n != None:
            if n.dado.valor < chave:
                n.dir = self.remove_no(n.dir, chave)
            elif n.dado.valor > chave:
                n.esq = self.remove_no(n.esq, chave)
            else:
                if n.esq != None and n.dir != None:
                    antecessor = self.maior(n.esq)
                    n.dado = antecessor.dado
                    self.remove_no(n.esq, antecessor.dado.valor)
                elif n.esq == None:
                    n = n.dir
                else:
                    n = n.esq
        return n
    
    def PreOrdem(self, no):
        '''
        Mostra a árvore em ordem RED (Raiz, Esquerda, Direita).
        Portanto, mostra a raiz, depois percorre toda a subárvore esquerda e mostra.
        Depois faz a mesma coisa com a subárvore direita.
        Exemplos:
        >>> a = arvore()
        >>> a.insere(item(4))
        >>> a.insere(item(2))
        >>> a.insere(item(6))
        >>> a.PreOrdem()
        item(valor=4)
        item(valor=2)
        item(valor=6)
        '''
        if no != None:
            print(no.dado)
            self.PreOrdem(no.esq)
            self.PreOrdem(no.dir)

    def InOrdem(self, no):
        '''
        Mostra a árvore em ordem ERD(Esquerda, Raiz e Direita).
        Portanto, percorre a subárvore esquerda e vai mostrando, depois mostra a raiz e percorre e mostra
        a subárvore direita. Inclusive, mostra todos os elementos em ordem crescente.
        Exemplos:
        >>> a = arvore()
        >>> a.insere(item(4))
        >>> a.insere(item(2))
        >>> a.insere(item(6))
        >>> a.InOrdem()
        item(valor=2)
        item(valor=4)
        item(valor=6)
        '''
        if no != None:
            self.InOrdem(no.esq)
            print(no.dado)
            self.InOrdem(no.dir)            

    def PosOrdem(self, no):
        '''
        Mostra a árvore em ordem EDR(Esquerda, Direita e Raiz)
        Portanto, mostra todos os elementos da subárvore esquerda, depois a direita e finalmente mostra a raiz.
        Exemplos:
        >>> a = arvore()
        >>> a.insere(item(4))
        >>> a.insere(item(2))
        >>> a.insere(item(6))
        >>> a.PosOrdem()
        item(valor=2)
        item(valor=6)
        item(valor=4)
        '''
        if no != None:
            self.PosOrdem(no.esq)
            self.PosOrdem(no.dir)      
            print(no.dado)         

    def folhas(self, no):
        '''
        Mostra apenas as folhas da árvore.
        Exemplos:
        >>> a = arvore()
        >>> a.insere(item(4))
        >>> a.insere(item(2))
        >>> a.insere(item(6))
        >>> a.folhas()
        item(valor=2)
        item(valor=6)
        '''
        if no != None:
            self.folhas(no.esq)
            if no.esq == None and no.dir == None:
                print("Folha: ", no.dado)
            self.folhas(no.dir)

    def conta_nos(self, no):
        '''
        Mostra a quantidade de nós que tem na árvore.
        Exemplos:
        >>> a = arvore()
        >>> a.insere(item(4))
        >>> a.insere(item(2))
        >>> a.insere(item(6))
        >>> a.conta_nos()
        3
        '''
        if no != None:
            return 1 + self.conta_nos(no.esq) + self.conta_nos(no.dir)
        else:
            return 0                    