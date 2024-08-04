"""
realizar una aplicación que permita registrar profesores y estudiantes, los cuales se guarden en una lista. Cada profesor o estudiante tiene como atributos su nombre, edad, especialidad/grado. Además, cada persona tiene un método que muestra su información. Crear un menú de opciones que permita ingresar profesores o estudiantes, mostrar todos los profesores y estudiantes, o salir del programa.
"""

from modelos.profesor import Profesor
from modelos.estudiante import Estudiante


def ingresar_datos_persona(tipo):
    nombre = input(f"Ingrese el nombre del {tipo}: ")
    edad = int(input(f"Ingrese la edad del {tipo}: "))
    return nombre, edad

def ingresar_profesor():
    nombre, edad = ingresar_datos_persona("profesor")
    especialidad = input("Ingrese la especialidad del profesor: ")
    return Profesor(nombre, edad, especialidad)

def ingresar_estudiante():
    nombre, edad = ingresar_datos_persona("estudiante")
    grado = input("Ingrese el grado del estudiante: ")
    return Estudiante(nombre, edad, grado)

def mostrar_personas(personas):
    for persona in personas:
        print(persona.mostrar_informacion())

def main():
    profesores = []
    estudiantes = []

    while True:
        print("\nMenú:")
        print("1. Ingresar Profesor")
        print("2. Ingresar Estudiante")
        print("3. Mostrar Profesores")
        print("4. Mostrar Estudiantes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            profesor = ingresar_profesor()
            profesores.append(profesor)
        elif opcion == '2':
            estudiante = ingresar_estudiante()
            estudiantes.append(estudiante)
        elif opcion == '3':
            print("\nProfesores:")
            mostrar_personas(profesores)
        elif opcion == '4':
            print("\nEstudiantes:")
            mostrar_personas(estudiantes)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()