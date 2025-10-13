from TADex1LE import *

def cria_lista(arranjo: list[int]) -> lista:
    if arranjo == []:
        return lista()
    else:
        resultado = lista()
        for i in arranjo:
            resultado.insere_fim(item(i))
        return resultado 
    
def concatena_listas(lista1: lista, lista2: lista):
    ptr = lista2.primeiro
    while ptr != None:
        lista1.insere_fim(ptr.dado)
        ptr = ptr.prox

def encadeadas_crescente(lista1: lista, lista2: lista):
    ptr2 = lista2.primeiro
    while ptr2 != None:
        ptr1 = lista1.primeiro
        pos = 0
        # Encontra a posição correta para inserir
        while ptr1 != None and ptr1.dado.valor < ptr2.dado.valor:
            ptr1 = ptr1.prox
            pos += 1
        lista1.insere_pos(ptr2.dado, pos)
        ptr2 = ptr2.prox

def main():
    le = cria_lista([1, 4, 7])
    le2 = cria_lista([0, 2, 3, 6, 9])
    print(le.n_celulas())
    encadeadas_crescente(le, le2)
    while le.vazia() != True:
        print(le.primeiro.dado.valor)
        le.remove_inicio()

main()