from enum import Enum, auto
from dataclasses import dataclass 

class categoria(Enum):
    HATCH = auto()
    SEDA = auto()
    SUV = auto()
    PICAPE = auto()

@dataclass
class Veiculos:
    marca: str
    modelo: str
    ano: str
    cor: str
    categoria: categoria

# Criar outro tipo composto apenas com as informações de modelo e ano.
@dataclass
class CategoriaCarro:
    modelo: str
    ano: str

def veiculos(carros: list[Veiculos], carroCategoria: categoria) -> list:
    '''
    Recebe uma lista de carros que possuem a marca, o modelo, o ano, a cor e a categoria.
    Dentro da categoria temos hatch, sedã, suv e picape.
    >>> carro1 = Veiculos('Chevrolet', 'Onix', '2019', 'azul', categoria.HATCH)
    >>> carro2 = Veiculos('Hyundai', 'HB20', '2019', 'Vermelho', categoria.HATCH)
    >>> carro3 = Veiculos('Renault', 'Sandero', '2017', 'Rosa', categoria.SUV)
    >>> veiculos([carro1, carro2, carro3], categoria.HATCH)
    [CategoriaCarro[modelo='Onix', ano=2019], CategoriaCarro[modelo='Hyundai', ano=2019]]
    '''
    cars = [CategoriaCarro]
    for i in carros:
        if i.categoria == carroCategoria:
            cars.append(i.modelo)
            cars.append(i.ano)
    return cars
