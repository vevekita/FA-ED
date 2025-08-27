from tadcilindro import *

def entrada():
    altura = 10
    raio = 5
    cilindro = Cilindro.cria_cilindro(altura, raio)
    print('A área do cilindro é', cilindro.area_cilindro())
    print('O volume do cilindro é', cilindro.volume_cilindro())

    cilindro.imprime_altura()
    cilindro.imprime_raio()

entrada()