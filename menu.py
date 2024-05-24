import sys
from funciones import sumar, restar, dividir, multiplicar, factorial

resultados = []

def ingresar_operando():
    """Pide al usuario que ingrese un operando"""
    while True:
        try:
            operando = float(input("Ingrese un operando: "))
            return operando
        except ValueError:
            print("Ingrese un número válido.")

def calcular_todas_las_operaciones(op1, op2):
    """Realiza todas las operaciones y muestra los resultados"""
    resultadosuma={sumar(op1, op2)}
    resultadoresta={restar(op1, op2)}
    resultadodividir={dividir(op1, op2)}
    resultadomultiplicar={multiplicar(op1, op2)}
    resultadofactorial_a={factorial(op1)}
    resultadofactorial_b={factorial(op2)}

    resultados.append(f"El resultado de {op1}+{op2} es: {resultadosuma}")
    resultados.append(f"El resultado de {op1}-{op2} es: {resultadoresta}")
    resultados.append(f"El resultado de {op1}/{op2} es: {resultadodividir}")
    resultados.append(f"El resultado de {op1}*{op2} es: {resultadomultiplicar}")
    resultados.append(f"El factorial de {op1} es: {resultadofactorial_a} y El factorial de {op2} es: {resultadofactorial_b}")

def main():
    op1 = op2 = 0
    results = []
    while True:
        print("\nSeleccione una opción:")
        print(f"1. Ingresar 1er operando (A={op1})")
        print(f"2. Ingresar 2do operando (B={op2})")
        print("3. Calcular todas las operaciones")
        print("4. Mostrar resultados")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Ingrese una opción válida.")
            continue

        if opcion == 1:
            op1 = ingresar_operando()
        elif opcion == 2:
            op2 = ingresar_operando()
        elif opcion == 3:
            if op1 == 0 or op2 == 0:
                print("Ingrese ambos operandos primero.")
            else:
                calcular_todas_las_operaciones(op1, op2)
        elif opcion == 4:
                print("\nResultados:")
                print("\n".join(resultados))
        elif opcion == 5:
            sys.exit("Adiós.")
        else:
            print("Ingrese una opción válida.")

main()