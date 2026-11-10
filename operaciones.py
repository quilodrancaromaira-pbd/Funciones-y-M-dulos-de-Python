# operaciones.py

def saludar_estudiante(nombre):
    """Funcion que recibe un nombre e imprime un saludo."""
    print(f"¡Hola {nombre}! Bienvenido al taller de programación.")

def sumar(a, b):
    """Función que retorna la suma de dos números."""
    resultado = a + b
    return resultado


def calcular_promedio(nota1, nota2, nota3):
    """Calcula y retorna el promedio de tres notas."""
    # Tú código aquí:
    nota1 = float(input("Ingrese su nota"))
    nota2 = float(input("Ingrese su segunda nota"))
    nota3 = float(input("Ingrese su tercera nota"))

    promedio = (nota1 + nota2 + nota3) / 3
    print("Su promedio es: ", promedio)
    # 1. Suma las tres notas y divídelas entre 3.
    # 2. Retorna el resultado obtenido.
    pass

def es_par(numero):
    """Retorna True si el número es par, o False si es impar."""
    # Tú código aquí:
    numero = float(input("Ingrese su numero: "))
    if numero % 2 == 0:
        print("Su numero es par", numero)
    else:
        print("Su numero es impar", numero)

    # Pista: Utiliza el operador módulo (%) -> numero % 2 == 0
    pass
