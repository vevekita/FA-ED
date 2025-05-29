#Uma biblioteca precisa de um sistema para gerenciar as informações e o status de seus livros. Cada livro possui 
#informações como título, autor, ISBN, ano de publicação e gênero. Além disso, é importante rastrear se um livro
#está disponível, emprestado ou em manutenção.
#a) Implemente uma função chamada verificar_genero_livro. Esta função deve retornar True se o livro.genero for 
#igual ao genero_desejado, e False caso contrário.
#b) Implemente uma função chamada livro_disponivel. Esta função deve retornar True se o livro.status for igual a 
#DISPONIVEL, e False caso não.
#c) Implemente uma função chamada emprestar. Esta função deve verificar se o livro está disponível para empréstimo
#usando livro_disponivel. Se o livro estiver disponivel, a função deve alterar o status do livro para EMPRESTADO e
#retornar True. Caso contrário, a função deve retornar False.

from enum import Enum, auto
from dataclasses import dataclass

class Status(Enum):
    DISPONIVEL = auto()
    EMPRESTADO = auto()
    MANUTENCAO = auto()

@dataclass
class Livros:
    Titulo: str
    Autor: str
    ISNB: str
    Ano_de_Publicacao: int
    Genero: str
    status: Status

def verificar_genero_livro(genero: Livros) -> bool:
    '''Retorna True se o gênero do livro for igual ao gênero desejado, e False caso não.
    Exemplo:
    >>> verificar_genero_livro('Romance') #mesma coisa do de baixo
    True
    >>> verificar_genero_livro('Suspense')
    False
    '''
    if Livros.Genero == genero:
        genero_desejado = True
    else:
        genero_desejado = False
    return genero_desejado

def livro_disponivel(livro: Livros) -> bool:
    '''Retorna True se o status do livro estiver disponível e False caso não.
    Exemplos:
    >>> livro_disponivel(Livros('Jogos de Herança', 'Lynn Barnes', '987654', 2019, 'Drama', Status.DISPONIVEL)
    True
    >>> livro_disponivel(Livros('Jogos de Herança', 'Lynn Barnes', '987654', 2019, 'Drama', Status.EMPRESTADO)
    False
    '''
    if Status.DISPONIVEL == livro.status:
        status_livro = True
    else:
        status_livro = False
    return status_livro

def emprestar()




    