"""
La programación orientada a objetos es un paradigma de programación que permite crear objetos y trabajar con ellos
En Python, la programación orientada a objetos se implementa mediante clases y objetos
Las clases son plantillas para crear objetos, y los objetos son instancias de las clases
En Python, todas las clases heredan de la clase base object

Definición del Método __init__:

def __init__(self, nombre, apellido):
__init__ es un método especial en Python conocido como el inicializador o constructor de la clase.
self es una referencia a la instancia actual de la clase y se utiliza para acceder a las variables que pertenecen a la clase.
nombre y apellido son parámetros que se pasan al crear una nueva instancia de la clase.
Asignación de Atributos:

self.nombre = nombre
Esta línea asigna el valor del parámetro nombre al atributo nombre de la instancia.
self.nombre es una variable de instancia que pertenece a la instancia específica de la clase.
self.apellido = apellido
Similarmente, esta línea asigna el valor del parámetro apellido al atributo apellido de la instancia.
self.apellido es otra variable de instancia.
"""

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola mi nombre es', self.nombre, self.apellido)


#instancia de un objeto
usuario1 = Usuario('Juan', 'Perez')
usuario2 = Usuario('Karla', 'Lara')
print(usuario1.nombre)
print(usuario2.nombre)
usuario1.saludo()
usuario2.saludo()

#definir una clase factura
class Factura:
    def __init__(self, descripcion, cantidad, precio):
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio = precio

    def calcular_total(self):
        return self.cantidad * self.precio

#crear una instancia de la clase factura
factura1 = Factura('Producto A', 10, 20)
print(factura1.descripcion)
print(factura1.cantidad)
print(factura1.precio)
print(factura1.calcular_total())
