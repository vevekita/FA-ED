from __future__ import annotations
from dataclasses import dataclass

class BancoHoras:
    Horas: int
    Minutos: int

    def __init__(self, horas: int, minutos: int):
        '''Cria um novo banco de horas com a quantidade 
        de *horas* e *minutos*'''
        self.Horas = horas
        self.Minutos = minutos

    def cria_banco(horas: int, minutos: int) -> BancoHoras:
        banco = BancoHoras(horas, minutos)
        return banco

    def DepositaHorasMinutos(self, horas: int, minutos: int):
        '''Adiciona a quantidade de *horas* e *minutos* em um 
        banco de horas existente
        >>> b = BancoHoras(2,30)
        >>> b.DepositaHorasMinutos(1,10)
        >>> b.consulta()
        '3:40'
        '''
        horasAdicionadas = self.Horas + horas
        minutosAdicionados = self.Minutos + minutos

        if minutosAdicionados > 60:
            minutosAdicionados = minutosAdicionados - 60
            horasAdicionadas = horasAdicionadas + 1

        self.Horas = horasAdicionadas
        self.Minutos = minutosAdicionados

        
    def SaqueHorasMinutos(self, horas: int, minutos: int):
        '''Diminui a quantidade de *horas* e *minutos* do saldo
        existente no banco de horas. Caso o saldo seja insuficiente
        não faz nada
        >>> b = BancoHoras(3,20)
        >>> b.SaqueHorasMinutos(1,30)
        >>> b.consulta()
        '1:50'
        >>> b1 = BancoHoras(3,20)
        >>> b1.SaqueHorasMinutos(3,30)
        >>> b1.consulta()
        '3:20'
        '''
        saqueHoras = self.Horas
        saqueMinutos = self.Minutos

        if self.Horas >= horas and self.Minutos >= minutos:
            saqueHoras -= horas
            saqueMinutos -= minutos
        elif self.Horas > horas and minutos > self.Minutos:
            saqueHoras = self.Horas - horas - 1
            saqueMinutos = self.Minutos - minutos + 60
        
        self.Horas = saqueHoras
        self.Minutos = saqueMinutos


    def consulta(self):
        '''Retorna a quantidade de horas e minutos do banco de horas
        transformados em uma string
        Exemplos:
        >>> b = BancoHoras(1,20)
        >>> b.consulta()
        '1:20'
        >>> b1 = BancoHoras(2,45)
        >>> b1.consulta()
        '2:45'
        '''

        return str(self.Horas) + ':' + str(self.Minutos)