from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    CPF: str
    nacionalidade: str

def pessoas_naturais(pessoas: list[Pessoa]) -> list[str]:
    '''
    Recebe uma lista de nomes de pessoas que possuem nome, CPF e nacionalidade.
    Depois retorna uma lista com os nomes das pessoas que são naturais de Maringá.
    Exemplos:
    >>> pessoas_naturais([Pessoa('Emilyn', '12345678900', 'Maringá'), Pessoa('Carlos', '98765432100', 'Maringá'), Pessoa('Murilo', '65498732100', 'Campinas')])
    ['Emilyn', 'Carlos']
    >>> pessoas_naturais([Pessoa('Miguel', '12378945600', 'Cianorte'), Pessoa('Thalia', '56412379800', 'Maringá'), Pessoa('Victor', '45612398722', 'Ourinhos')])
    ['Thalia']
    '''
    pessoas_de_maringa = []
    for i in pessoas:
        if i.nacionalidade == 'Maringá':
            pessoas_de_maringa.append(i.nome)
    return pessoas_de_maringa