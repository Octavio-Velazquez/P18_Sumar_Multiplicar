def sumar(*numeros):
    """Función que suma los números."""

    resultado = 0

    for numero in numeros:
        resultado = numero + resultado

    return resultado

print(sumar(2,5,7))
print(sumar(657, 78, 54))