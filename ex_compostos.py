from dataclasses import dataclass

@dataclass 
class pessoa: # isso aqui serve pra "linkar" variáveis a uma variável. Pensa na caixa de sapatos que possui várias coisas lá dentro.
    nome: str
    idade: int


def mais_velho(p1: pessoa, p2: pessoa) -> pessoa:
    '''
    Devolve o nome da pessoa mais velha entre duas pessoas.
    Exemplo:
    >>> mais_velho(pessoa('Emi', 17), pessoa('Victor', 18)).nome
    'Victor'
    '''
    if p1.idade > p2.idade:
        return p1
    else:
        return p2
    

def main():
    pessoa1 = pessoa('Emi', 17)
    pessoa2 = pessoa('Victor', 18)
    print(mais_velho(pessoa1, pessoa2).nome)

if __name__ == '__main__':
    main()

