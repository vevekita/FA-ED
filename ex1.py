from dataclasses import dataclass

@dataclass
class Aluno:
    r_academico: str
    nome: str
    curso: str

def info_aluno(ra: str, nome: str, curso: str) -> Aluno:
    
    return Aluno(ra, nome, curso)

def imprimir_aluno(aluno: Aluno):
    print(aluno)

def main():
    r_a = input("Qual seu RA?")
    nom = input("Qual seu nome?")
    curs = input("Qual seu curso?")
    aluno = info_aluno(r_a, nom, curs) #armazena as informações recebidas dos inputs
    imprimir_aluno(aluno)

if __name__ == '__main__':
    main()
