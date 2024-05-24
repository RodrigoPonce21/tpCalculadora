import sys
from funciones import sumar, restar, dividir, multiplicar, factorial_a, factorial_b


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
    print(f"El resultado de {op1}+{op2} es: {sumar(op1, op2)}")
    print(f"El resultado de {op1}-{op2} es: {restar(op1, op2)}")
    print(f"El resultado de {op1}/{op2} es: {dividir(op1, op2)}")
    print(f"El resultado de {op1}*{op2} es: {multiplicar(op1, op2)}")
    print(f"El factorial de {op1} es: {factorial_a(op1)} y El factorial de {op2} es: {factorial_b(op2)}")

def main():
    op1 = op2 = 0
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
                print("Primero debe ingresar ambos operandos.")
            else:
                print("Operaciones calculadas. Seleccione la opción 4 para mostrar los resultados.")
        elif opcion == 4:
            if op1 == 0 or op2 == 0:
                print("Primero debe ingresar ambos operandos y calcular las operaciones.")
            else:
                calcular_todas_las_operaciones(op1, op2)
        elif opcion == 5:
            print("Saliendo del programa...")
            sys.exit(0)
        else:
            print("Opción inválida. Intente nuevamente.")

main()