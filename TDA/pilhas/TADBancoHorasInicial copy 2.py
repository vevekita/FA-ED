from __future__ import annotations
from dataclasses import dataclass

class BancoHoras:
    Minutos: int

    def __init__(self, minutos: int):
        self.Minutos = minutos

    def cria_banco(minutos: int) -> BancoHoras:
        banco = BancoHoras(horas, minutos)
        return banco

    def DepositaHorasMinutos(self, minutos: int):
        minutosAdicionados = self.Minutos + minutos

        self.Minutos = minutosAdicionados

        
    def SaqueHorasMinutos(self,  minutos: int):
        saqueMinutos = self.Minutos - minutos
        if self.Minutos < minutos:
            saqueMinutos = self.Minutos
        self.Minutos = saqueMinutos


    def consulta(self):

        return str(self.Minutos)