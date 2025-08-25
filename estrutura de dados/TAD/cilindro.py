from tadcilindro import *

def entrada():
    altura = 10
    raio = 5
    cilindro = Cilindro.cria_cilindro(altura, raio)
    print('A área do cilindro é', Cilindro.area_cilindro(altura, raio))

    cilindro.imprime_altura()
    cilindro.imprime_raio()

entrada()