"""
La encapsulación es otro de los principios fundamentales de la programación orientada a objetos (OOP). En Python, la encapsulación se refiere a la práctica de restringir el acceso a ciertos componentes de un objeto y de proteger los datos internos del mismo. Esto se logra mediante el uso de atributos y métodos privados y protegidos.

Tipos de encapsulación
Atributos Públicos:
Son accesibles desde cualquier lugar, tanto dentro como fuera de la clase.
No tienen prefijos especiales.

Atributos Protegidos:
Son accesibles dentro de la clase y en las subclases.
Se denotan con un guion bajo inicial (_atributo).

Atributos Privados:
Son accesibles solo dentro de la clase donde se definen.
Se denotan con dos guiones bajos iniciales (__atributo).
"""
 
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre          # Atributo público
        self._edad = edad             # Atributo protegido
        self.__cuenta_bancaria = 1000 # Atributo privado

    def mostrar_nombre(self):
        return self.nombre

    def _mostrar_edad(self):
        return self._edad

    def __mostrar_cuenta_bancaria(self):
        return self.__cuenta_bancaria

    def mostrar_cuenta_bancaria(self):
        return self.__mostrar_cuenta_bancaria()

persona = Persona("Juan", 30)

# Acceso a atributos y métodos
print(persona.nombre)               # Acceso permitido: Juan
print(persona.mostrar_nombre())     # Acceso permitido: Juan

print(persona._edad)                # Acceso permitido pero desaconsejado: 30
print(persona._mostrar_edad())      # Acceso permitido pero desaconsejado: 30

# print(persona.__cuenta_bancaria)  # Acceso denegado: AttributeError
# print(persona.__mostrar_cuenta_bancaria())  # Acceso denegado: AttributeError

# Acceso a través de un método público
print(persona.mostrar_cuenta_bancaria())  # Acceso permitido: 1000