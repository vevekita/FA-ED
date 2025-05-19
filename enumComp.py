#Exercício: Considere um cadastro de funcionários. Este cadastro possui o cpf, nome, data de nascimento
#e o setor em que trabalham. A empresa tem o setor de logística, financeiro e manutenção. 
#Organize funções que permitam o cadastro de um funcionário e a partir da informação de um setor, informe
#se o funcionário trabalha nessa seção ou não.
from enum import Enum, auto
from dataclasses import dataclass

class cad_funcionario(Enum):
    logistica = auto()
    financeiro = auto()
    manutencao = auto()

@dataclass
class Funcionario:
    cpf: str
    nome: str
    dataNascimento: str
    setor: cad_funcionario

def cad_func(cpf: str, nome: str, dataNas: str, setor: cad_funcionario) -> Funcionario:
    return Funcionario(cpf, nome, dataNas, setor)

def imprimir_funcionario(cadFuncionario: Funcionario):
    print(cadFuncionario)

def setor_func(setor: int) -> cad_funcionario:
    '''Se o número for 1, 2 ou 3 o funcionario faz parte desse setor
    Exemplos:
    >>> setor_func(1).name
    'logistica'
    >>> setor_func(2).name
    'financeiro'
    >>> setor_func(3).name
    'manutencao'
    '''
    if setor == 1:
        set: cad_funcionario = cad_funcionario.logistica
    elif setor == 2:
        set = cad_funcionario.financeiro
    else:
        set = cad_funcionario.manutencao
    return set

def main():
    cpf = input("Digite seu CPF: ")
    nome = input("Digite seu nome: ")
    dataNascimento = input("Digite sua data de nascimento: ")
    setor = int(input("Digite o número do setor em que trabala ([1]Logística; [2]Financeiro; [3]Manutenção): "))
    cadFuncionario = cad_func(cpf, nome, dataNascimento, setor)
    imprimir_funcionario(cadFuncionario)

if __name__ == '__main__':
    main()