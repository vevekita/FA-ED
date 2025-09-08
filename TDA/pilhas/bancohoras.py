from TADBancoHorasInicial import *

def entrada():
    Horas = 2
    Minutos = 30
    bancohoras = BancoHoras.cria_banco(Horas, Minutos)

    print(bancohoras.consulta())

entrada()