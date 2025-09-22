from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class item:
    valor: int | None

class lista:
    def __init__(self, tamanho: int):
        self.fim: int = 0
        self.tam_max: int = tamanho
        self.elementos: list[item] = [item(None) for i in range(tamanho)]
    
    def vazia(self) -> bool:
        '''retorna True se a lista estiver vazia
        e False caso contrário
        Exemplos:
        >>> l = lista(5)
        >>> l.vazia()
        True
        >>> l.insere_fim(item(2))
        True
        >>> l.vazia()
        False'''

        return self.fim == 0
            
    def cheia(self) -> bool:
        '''retorna True se a lista estiver cheia
        e False caso contrário
        Exemplos:
        >>> l = lista(2)
        >>> l.cheia()
        False
        >>> l.insere_fim(item(2))
        True
        >>> l.cheia()
        False
        >>> l.insere_fim(item(1))
        True
        >>> l.cheia()
        True'''

        return self.fim == self.tam_max
  
    def busca(self, n1: int) -> int:
        '''Procura um item na lista pelo valor.
        Se ele estiver na lista retorna o seu índice,
        caso contrário retorna -1
        Exemplos:
        >>> l = lista(3)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.busca(5)
        1
        >>> l.busca(2)
        -1
        '''
        
        for i in range(self.fim):
            if self.elementos[i].valor == n1:
                return i
            
        return -1

    def busca_item(self, n1: int) -> item | None:
        '''Retorna um item a partir de uma chave de busca.
        Caso a chave não exista, retorna None
        Exemplo:
        >>> l = lista(3)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.busca_item(5)
        item(valor=5)
        >>> l.busca_item(2)
        '''

        saida = None
        for i in range(self.fim):
            if self.elementos[i].valor == n1:
                saida = self.elementos[i]

        return saida

    def insere_fim(self, x: item) -> bool:
        '''Insere um item no final da lista.
        Se a inserção ocorrer normalmente ela 
        retorna True. Se o item já existir na
        lista, ou a lista já estiver cheia, 
        retorna False
        Exemplo:
        >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.busca(5)
        1
        >>> l.busca(8)
        0
        >>> l.insere_fim(item(5))
        False
        >>> l.insere_fim(item(1))
        True
        >>> l.insere_fim(item(3))
        False
        '''
        if self.cheia() == True:
            return False # ele pede pra retornar true ou false, então acho que não é pra colocar o raise ValueError
        else:
            if self.busca(x.valor) != -1: # aqui dá erro, mas funciona por algum motivo
                return False
            else:
                self.elementos[self.fim] = deepcopy(x)
                self.fim += 1
                return True

    def insere_pos(self, x: item, pos: int) -> bool:
        '''Insere um item na lista na posição
         indicada por *pos*. Se a inserção ocorrer 
         normalmente ela retorna True. Se o item já 
         existir na lista, ou a lista já estiver cheia, 
         ou *pos* estiver fora dos limites da lista,
        retorna False
        Exemplo:
        >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_pos(item(5),0)
        True
        >>> l.insere_pos(item(7),1)
        True
        >>> l.busca(5)
        0
        >>> l.busca(8)
        2
        >>> l.insere_pos(item(5),1)
        False
        >>> l.insere_pos(item(1),1)
        True
        >>> l.insere_pos(item(3),2)
        False
        >>> l.busca(7)
        2
        '''
        if self.cheia() == True or pos < 0 or pos > self.fim:
            return False
        else:
            if self.busca(x.valor) != -1:
                return False
            else:
                for i in range(self.fim, pos, -1):
                    self.elementos[i] = deepcopy(self.elementos[i-1])
                self.elementos[pos] = deepcopy(x)
                self.fim += 1
                return True

    def desloca(self, pos: int):
        '''Função de apoio para remoção
        de itens no meio da lista. Essas
        remoções exigem que os elementos
        após o item removido sejam deslocados
        para a esquerda
        Exemplo:
        >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.desloca(0)
        >>> l.busca(8)
        -1
        >>> l.busca(7)
        1
        '''

        for i in range(pos, self.fim):
            self.elementos[i] = deepcopy(self.elementos[i+1]) # pega o elemento e desloca todos a frente dele
        self.fim -= 1
        
        
    def remove_fim(self) -> bool:
        '''Remove o último elemento da lista. Se a
        remoção acontecer normalmente a função retorna
        True, se a lista estiver vazia, retorna False
        Exemplos:
         >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.remove_fim()
        True
        >>> l.busca(7)
        -1
        '''
        if self.vazia() == True:
            return False
        else:
            self.fim -= 1
        return True

    def remove_pos(self, pos: int) -> bool:
        '''Remove o elemento da posição definida por *pos*. 
        Se a remoção acontecer normalmente a função retorna
        True, se a lista estiver vazia, retorna False
        Exemplos:
         >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.remove_pos(0)
        True
        >>> l.busca(8)
        -1
        '''
        if self.vazia() == True or pos < 0 or pos >= self.fim:
            return False
        else:
            self.desloca(pos)
        return True
    
    def remove_valor(self, valor: int) -> bool:
        '''Remove o elemento definido por *valor*. 
        Se a remoção acontecer normalmente a função retorna
        True, se a lista estiver vazia, retorna False
        Exemplos:
         >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.remove_valor(8)
        True
        >>> l.busca(8)
        -1
        '''
        if self.vazia() == True:
            return False
        else:
            pos = self.busca(valor)
            if pos == -1:
                return False
            else:
                self.desloca(pos)
                return True 
            

    def imprimeLista(self) -> str:
        '''Retorna uma string com todos os elementos da lista.
        Exemplos:
        >>> l = lista(4)
        >>> l.insere_fim(item(8))
        True
        >>> l.insere_fim(item(5))
        True
        >>> l.insere_fim(item(7))
        True
        >>> l.imprimeLista()
        '8 5 7 '
        '''

        resultado = ''
        for i in range(self.fim):
            resultado += str(self.elementos[i].valor) + ' '
        return resultado 
    
    def insereORD(self, x: item):
        '''Insere o x na lista de forma ordenada.
        Exemplos:
        >>> l = lista(4)
        >>> l.insereORD(item(8))
        >>> l.insereORD(item(5))
        >>> l.insereORD(item(3))
        >>> l.imprimeLista()
        '3 5 8 '
        '''

        if self.cheia() == True:
            return False
        else:
            if self.vazia() == True:
                self.insere_fim(x)
            else:
                for i in range(self.fim):
                    if x.valor < self.elementos[i].valor:
                        self.insere_pos(x, i)
                self.insere_fim(x)

    def troca(self, x: item, y: item) -> bool:
        '''Troca o item x pelo item y na lista.
        Se a troca ocorrer normalmente ela retorna True.
        Se x ou y não existirem na lista, retorna False.
        Exemplos:
        >>> l = lista(4)
        >>> l.insere_fim(item(1))
        True
        >>> l.insere_fim(item(3))
        True
        >>> l.insere_fim(item(4))
        True
        >>> l.troca(item(3), item(4))
        True
        >>> l.troca(item(2), item(5))
        False
        '''

        pos_x = self.busca(x.valor)
        pos_y = self.busca(y.valor)
        if pos_x == -1 or pos_y == -1:
            return False
        else:
            self.elementos[pos_x] = deepcopy(y)
            self.elementos[pos_y] = deepcopy(x)
            return True
