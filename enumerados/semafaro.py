# semafaro.py
from enum import Enum, auto
from dataclasses import dataclass

class Semafaro(Enum):
    VERDE = auto()
    AMARELO = auto()
    VERMELHO = auto()

def cor_semafaro(cor: Semafaro) -> Semafaro: #AQUI EU PEGO AS VARIÁVEIS DA CLASSE, AO INVÉS DE USAR STRINGS
    '''Indica a próxima cor do semáfaro de acordo com a cor atual.
    Produz:
    'verde' se a cor atual for vermelho.
    'amarelo' se a cor atual for verde.
    'vermelho' se a cor atual for amarelo.
    Exemplos:
    >>> cor_semafaro(Semafaro.VERDE).name #PEGO A CLASSE E ESCOLHO UMA OPÇÃO DO QUE PODE SER A SAÍDA.
    'AMARELO'
    >>> cor_semafaro(Semafaro.AMARELO).name
    'VERMELHO'
    >>> cor_semafaro(Semafaro.VERMELHO).name
    'VERDE'
    '''

    if cor == Semafaro.VERDE: 
        semafaro: Semafaro = Semafaro.AMARELO

    elif cor == Semafaro.AMARELO:
        semafaro = Semafaro.VERMELHO

    else:
        semafaro = Semafaro.VERDE

    return semafaro 