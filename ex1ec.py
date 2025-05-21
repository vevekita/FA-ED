from enum import Enum

class IngredientesPizza(Enum):
    QUEIJO = 3.00
    BACON = 4.00
    CEBOLA = 1.00
    AZEITONA = 2.00

class TamanhoPizza(Enum):
    PEQUENA = 1.10
    MEDIA = 1.20
    GRANDE = 1.30

def preco_pizza(ingrediente1: IngredientesPizza, ingrediente2: IngredientesPizza, ingrediente3: IngredientesPizza, tamanho: TamanhoPizza) -> float:
    '''De acordo com o que o usuário deseja em relação ao tamanho e aos ingredientes, calcula-se
    preço total adicionando o preço base aos demais valores do tamanho e dos ingredientes.
    Exemplos:
    >>> tamanho_pizza(IngredientesPizza.QUEIJO, IngredientesPizza.BACON, Ingredientes.CEBOLA, TamanhoPizza.PEQUENA)
    24.5
    >>> tamanho_pizza(IngredientesPizza.QUEIJO, IngredientesPizza.CEBOLA, Ingredientes.AZEITONA, TamanhoPizza.PEQUENA)
    22.5
    >>> tamanho_pizza(IngredientesPizza.CEBOLA, IngredientesPizza.BACON, Ingredientes.AZEITONA, TamanhoPizza.MEDIA)
    25.0
    >>> tamanho_pizza(IngredientesPizza.BACON, IngredientesPizza.QUEIJO, Ingredientes.CEBOLA, TamanhoPizza.MEDIA)
    26.0
    >>> tamanho_pizza(IngredientesPizza.QUEIJO, IngredientesPizza.BACON, Ingredientes.CEBOLA, TamanhoPizza.GRANDE)
    24
    '''

    precoBase = 15.0
    precoPizza = (precoBase * tamanho.value) + ingrediente1.value + ingrediente2.value + ingrediente3.value
    return (precoPizza)
