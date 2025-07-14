def fatorial(n: int) -> int:
    '''
    Calcula o fatorial do número n;
    Exemplos.
    >>> fatorial(3)
    6
    >>> fatorial(5)
    120
    '''
    fat: int = 1
    for i in range(2, n + 1):
        fat = fat * i
    return fat

# def main():
#     n: int = int(input('Digite um número:'))
#     resultado: int = fatorial(n)
#     print(resultado)

# if __name__ == '__main__':
#     main()

print(fatorial(5))