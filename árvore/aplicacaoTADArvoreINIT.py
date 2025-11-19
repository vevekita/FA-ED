# Crie uma aplicação. 
# - Insira alguns nós da árvore.
# - Use a função InOrdem para verificar se as chaves foram inseridas corretamente. 
# - Remova nós intermediários e verifique novamente a listagem dos nós restantes.

from TADArvoreINIT import *

def entrada():
    arv = arvore()
    arv.insere(item(2))
    arv.insere(item(3))
    arv.insere(item(5))
    arv.insere(item(1))
    arv.insere(item(6))
    arv.insere(item(4))

    arv.InOrdem()
