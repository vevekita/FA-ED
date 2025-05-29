from enum import Enum
from dataclasses import dataclass

class RegiaoFrete(Enum):
    SUL = 1.0
    SUDESTE = 1.1
    CENTRO = 1.2
    NORDESTE = 1.3
    NORTE = 1.4

@dataclass
class DimensaoProduto:
    Largura: float
    Comprimento: float
    Altura: float

@dataclass
class Produto:
    Codigo: str
    Nome: str
    Preco: float
    Estoque: int
    Peso: float
    Dimensoes: DimensaoProduto

def calculo_frete(produto: Produto, regiao: RegiaoFrete) -> float:
    '''
    De acordo com o produto e a região recebida calcula-se o frete.
    Exemplos:
    >>> calculo_frete(Produto('0001','Sapato', 60.0, 500, 0.5, DimensaoProduto(25.0, 5.5, 10.0 )), RegiaoFrete.SUL )
    2.225
    '''

    freteBase = produto.Peso * 0.5
    freteVolume = (produto.Dimensoes.Largura * produto.Dimensoes.Comprimento * produto.Dimensoes.Altura) * 0.001
    freteSeguro = produto.Preco * 0.01
    freteTotal = (freteBase + freteVolume + freteSeguro) * regiao.value
    return (freteTotal)