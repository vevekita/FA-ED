def quantidade_azulejos(alturaParede: float, larguraParede: float) -> int:
    '''Calcular a quantidade de azulejos que serão necessários para azulejar 
    uma parede que possui altura e largura em metros, 
    levando em consideração que cada azulejo é quadrado e mede 20cm, 
    além de que não haverá azulejos perdidos e nem cortes.
    Exemplos:
    >>> quantidade_azulejos(4, 3)
    300
    >>> quantidade_azulejos(6, 7)
    1050
    '''

    area = alturaParede * larguraParede 
    quantidadeAzulejos = area / 0.04

    if(quantidadeAzulejos / int(quantidadeAzulejos) == 1):
        return(int(quantidadeAzulejos))
    else:
        return(int(quantidadeAzulejos) + 1)