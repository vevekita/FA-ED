# Considere uma lista de pessoas que tenha o nome, CPF e naturalidade. 
# Faça uma função que retorne o nome das pessoas que são naturais de 'Maringá'
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    CPF: str
    naturalidade: str

def pessoas_naturais(pessoas: list[Pessoa]) -> list[str]:
    '''
    Recebe uma lista de pessoas com nome, CPF e naturalide.
    Retorna uma outra lista apenas com os nomes das pessoas que são de Maringá.
    Exemplos:
    >>> pessoas_naturais([Pessoa('Emilyn', '12345678900', 'Maringá'), Pessoa('Joana', '98765432100', 'Maringá'), Pessoa('Marianna', '65432198700', 'Londrina')])
    ['Emilyn', 'Joana']
    '''

    naturais: str = []
     
       