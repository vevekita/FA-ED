from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Cilindro:
    altura: int
    raio: int

    def cria_cilindro(altura: int, raio: int) -> Cilindro:
        cilindro = (altura, raio)
        return cilindro
    
    def imprime_altura(alt: Cilindro):
        print('A altura do cilindro é', alt.altura)

    def imprime_raio(r: Cilindro):
        print('O raio do cilindro é', r.raio)

    def area_cilindro(alt: Cilindro, r: Cilindro) -> float:
        return (2*3.14*r.raio*(r.raio + alt.altura))
    
    def volume_cilindro(altura: Cilindro, raio: Cilindro) -> float:
        return (3.14*((raio.raio)**2)*altura.altura)
        