from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Ponto:
    x: float
    y: float

    def cria_ponto(a: float, b: float) -> Ponto:
        p = Ponto(a,b)
        return p

    def distancia(p1: Ponto, p2: Ponto) -> float:
        return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2) ** (1/2)
    
    def imprime(p1: Ponto):
        print('Coordenada x: ', p1.x)
        print('Coordenada y: ', p1.y)