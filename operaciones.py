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

    prom = (nota1 + nota2 + nota3) / 3
    
    return prom
    # 1. Suma las tres notas y divídelas entre 3.
    # 2. Retorna el resultado obtenido.
    pass

def es_par(numero):
    """Retorna True si el número es par, o False si es impar."""
    # Tú código aquí:
    numero_evaluar = int(input("Ingrese su numero: "))
    if numero_evaluar % 2 == 0:
        return numero_evaluar % 2 == 0
    # Pista: Utiliza el operador módulo (%) -> numero % 2 == 0
    pass
