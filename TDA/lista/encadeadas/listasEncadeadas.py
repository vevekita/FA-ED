from dataclasses import dataclass
from copy import deepcopy
from __future__ import __annotations__

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
    
    def busca_item(self, chave: int) -> item | None:
        ptr = self.busca(chave)
        if ptr != None:
            return deepcopy(ptr.dado)
        else:
            return None
        
    def insere_inicio(self, x: item) -> bool:
        if self.busca(x.valor) == None:
            novo = no(x)
            if self.vazia():
                self.ultimo = novo
            novo.prox = self.primeiro
            self.primeiro = novo
            return True
        else:
            return False
        
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
        
    def remove_chave(self, chave: int) -> bool:
        ptr = self.primeiro
        if not self.vazia():
            if ptr.dado.valor == chave:
                return self.remove_inicio()
            while ptr.prox != None and ptr.prox.dado.valor != chave:
                ptr = ptr.prox
            if ptr.prox != None:
                rem = ptr.prox
                ptr.prox = rem.prox
                if ptr.prox == None:
                    self.ultimo = ptr
                rem.prox = None
                return True
        return False
    
    def remove_inicio(self) -> bool:
        if not self.vazia():
            rem = self.primeiro
            self.primeiro = rem.prox
            if self.vazia():
                self.ultimo = None
            rem.prox = None
            return True
        return False
    # 1) ponteiro no ínicio (ptr = self.primeiro); 
    # 2) deslocar ponteiro primeiro (self.primeiro = ptr.prox); 
    # 3) desconectar o elem. da lista (ptr.prox = None);

    
        