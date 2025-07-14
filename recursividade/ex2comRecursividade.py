def fatorial(n: int) -> int:
    '''
    Calcula o fatorial do número n;
    Exemplos.
    >>> fatorial(3)
    6
    >>> fatorial(5)
    120
    '''
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

# def main():
#     n: int = int(input('Digite um número:'))
#     print('Fatorial:', fatorial(n))

# if __name__ == '__main__':
#     main()

print(fatorial(5))
