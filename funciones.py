def sumar(x, y):
    """Calcula la suma de dos números"""
    return x + y

def restar(x, y):
    """Calcula la resta de dos números"""
    return x - y

def dividir(x, y):
    """Calcula la división de dos números, siempre que y sea distinto de cero"""
    if y == 0:
        raise ValueError("No es posible dividir por cero")
    return x / y

def multiplicar(x, y):
    """Calcula el producto de dos números"""
    return x * y

def factorial_a(n):
    """Calcula el factorial de un número"""
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial_a(n - 1)

def factorial_b(n):
    """Calcula el factorial de un número"""
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial_b(n - 1)