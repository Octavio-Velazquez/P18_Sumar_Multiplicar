def multiplicar(*numeros):
    """Función que suma los números."""

    resultado = 1

    for numero in numeros:
        resultado = numero * resultado

    return resultado

print(multiplicar(2,5,7))

print(multiplicar(5,5))