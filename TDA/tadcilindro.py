from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Cilindro:
    altura: float
    raio: float

    def cria_cilindro(altura: float, raio: float) -> Cilindro:
        cilindro = Cilindro(altura, raio)
        return cilindro
    
    def imprime_altura(alt: Cilindro):
        print('A altura do cilindro é', alt.altura)

    def imprime_raio(r: Cilindro):
        print('O raio do cilindro é', r.raio)

    def area_cilindro(cilindro: Cilindro) -> float:
        return (2*3.14*cilindro.raio*(cilindro.raio + cilindro.altura))
    
    def volume_cilindro(cilindro: Cilindro) -> float:
        return (3.14*((cilindro.raio)**2)*cilindro.altura)
        