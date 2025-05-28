from dataclasses import dataclass

@dataclass
class Tempo:
    horas: int
    minutos: int

def tempo(temp: int) -> Tempo:
    t_hora = temp // 60
    t_min = temp % 60

    return Tempo(t_hora, t_min)


def main():
    t_total = int(input("Digite o tempo total em minutos:"))
    horario = tempo(t_total)
    print(horario)

if __name__ == '__main__':
    main()
