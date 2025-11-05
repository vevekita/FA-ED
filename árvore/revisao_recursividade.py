from __future__ import annotations
from dataclasses import dataclass

@dataclass
class item:
    valor: int

class no:
    def __init__(self, x: item):
        self.dado: item = x
        self.prox: no | None = None

class lista:
    def __init__ (self):
        self.primeiro: no | None = None
        self.ultimo: no | None = None

    def vazia(self):
        return self.primeiro == None
    
    def busca(self, chave: int) -> no:
        ptr = self.primeiro
        while (ptr != None) and (ptr.dado.valor != chave):
            ptr = ptr.prox
        return ptr
    
    def insere_fim(self, x: item) -> bool:
        if self.busca(x.valor) == None:
            novo = no(x)
            if self.vazia():
                self.primeiro = novo
            else:
                self.ultimo.prox = novo
            self.ultimo = novo
            return True
        else:
            return False
        
    def soma_elementos(self, ptr: no) -> int:
        '''
        Soma todos os elementos da lista.
        Exemplos:
        >>> l = lista()
        >>> l.insere_fim(item(1))
        True
        >>> l.insere_fim(item(2))
        True
        >>> l.insere_fim(item(3))
        True
        >>> l.insere_fim(item(4))
        True
        >>> l.soma_elementos(l.primeiro)
        10
        '''
        if ptr == None:
            return 0
        else:
            return ptr.dado.valor + self.soma_elementos(ptr.prox)