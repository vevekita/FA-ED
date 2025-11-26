from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class item:
    chave: int
    valor: float

class no:
    def __init__(self, dado: item):
        self.esq: no | None = None
        self.dir: no | None = None
        self.altura: int = 1
        self.dado: item = dado

class arvore_avl:
    def __init__(self):
        self.raiz: no | None = None

    def vazia(self):
        '''
        Se a árvore estiver vazia, ou seja, for igual a None, retorna True.
        Caso contrário retorna False.
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

    def busca_no(self, n: no, chave:int) -> no | None:
        if n == None:
            return None
        elif chave > n.dado.chave:
            return self.busca_no(n.dir, chave)
        elif chave < n.dado.chave:
            return self.busca_no(n.esq, chave)
        else:
            return n
        
    def insere_no(self, n: no , x: item) -> no | None:
        if n == None:
            n = no(deepcopy(x))
        elif x.chave > n.dado.chave:
            n.dir = self.insere_no(n.dir,x)
        elif x.chave < n.dado.chave:
            n.esq = self.insere_no(n.esq,x)
        return self.balanceia(n)

    def maior(self, n: no) -> no:
        if n.dir == None:
            return n
        else:
            return self.maior(n.dir)
    
    def remove_no(self, n: no, chave: int) -> no | None:
        if n != None:
            if n.dado.chave < chave:
                n.dir = self.remove_no(n.dir, chave)
            elif n.dado.chave > chave:
                n.esq = self.remove_no(n.esq, chave)
            else:
                if n.esq != None and n.dir != None:
                    antecessor = self.maior(n.esq)
                    n.dado = antecessor.dado
                    n.esq = self.remove_no(n.esq, antecessor.dado.chave)
                elif n.esq == None:
                    n = n.dir
                else:
                    n = n.esq 
        return self.balanceia(n)
    
    def altura_no(self, n:no) -> int:
        altura_sad = 0
        altura_sae = 0
        altura_no = 0
        if n != None:
            if n.dir != None:
                altura_sad = n.dir.altura
            if n.esq != None:
                altura_sae = n.esq.altura
            altura_no = max(altura_sae,altura_sad) + 1
        return altura_no
    
    def rotacao_esq(self, p: no) -> no:
        q = p.dir
        p.dir = q.esq
        q.esq = p
        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        return q
    
    def rotacao_dupla_esq(self, p: no) -> no:
        q = p.dir
        w = q.esq
        q.esq = w.dir
        p.dir = w.esq
        w.dir = q
        w.esq = p

        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        w.altura = self.altura_no(w)
        return w
    
    #criar as funções de rotação simples e dupla pra direita!!!
    def rotacao_dir(self, p: no) -> no:
        q = p.esq
        p.esq = q.dir
        q.esq = p
        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        return q
    
    def rotacao_dupla_dir(self, p: no) -> no:
        q = p.esq
        w = q.dir
        q.dir = w.esq
        p.esq = w.dir
        w.esq = q
        w.dir = p

        p.altura = self.altura_no(p)
        q.altura = self.altura_no(q)
        w.altura = self.altura_no(w)
        return q
    
    def balanceia(self, n: no) -> no:
        if n!= None:
            asd = self.altura_no(n.dir)
            ase = self.altura_no(n.esq)
            if asd > ase + 1 :
                if self.altura_no(n.dir.esq) > self.altura_no(n.dir.dir):
                    return self.rotacao_dupla_esq(n)
                else:
                    return self.rotacao_esq(n)
            elif ase > asd + 1:
                if self.altura_no(n.esq.dir) > self.altura_no(n.esq.esq):
                    return self.rotacao_dupla_dir(n)
                else:
                    return self.rotacao_dir(n)
            n.altura = self.altura_no(n)
        return n