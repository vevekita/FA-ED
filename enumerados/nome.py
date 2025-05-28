# nome.py
from enum import Enum, auto
from dataclasses import dataclass

class Tamanho(Enum):
    CURTO = auto()
    LONGO = auto()
    MEDIANO = auto()

def tamanho_nome(nome: str) -> Tamanho:
    '''
    >>> tamanho_nome("Ana").name
    'CURTO'
    >>> tamanho_nome("Beatriz").name
    'MEDIANO'
    >>> tamanho_nome("Alexandre").name
    'LONGO'
    '''

    if len(nome) <= 4:
        tamanhoNome: Tamanho = Tamanho.CURTO
    elif len(nome) <= 8:
        tamanhoNome = Tamanho.MEDIANO
    else:
        tamanhoNome = Tamanho.LONGO

    return tamanhoNome