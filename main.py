# main.py
# Importamos las funciones desarrolladas en operaciones.py
import operaciones
import conversor

def ejecutar_programa():
    print("=== SISTEMA DE PRUEBAS DE MÓDULOS ===")
    
    # Probando la función de saludo
    operaciones.saludar_estudiante("Estudiante TP")
    
    # Probando la función de suma
    suma_val = operaciones.sumar(15, 25)
    print(f"El resultado de la suma es: {suma_val}")
    
    # Probando la función de promedio (Descomentar al completar el paso 3.1)
    prom = operaciones.calcular_promedio(6.0, 5.5, 7.0)
    print(f"El promedio calculado es: {prom}")
    
    # Probando la función par/impar (Descomentar al completar el paso 3.1)
    numero_evaluar = 8
    print(f"¿El número {numero_evaluar} es par?: {operaciones.es_par(numero_evaluar)}")

    celsius = conversor.celsius_a_fahrenheit(25)
    print(f"La conversion de grados celsius a fahrenheit es: {celsius}")

if __name__ == '__main__':
    ejecutar_programa()