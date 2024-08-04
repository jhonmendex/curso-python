#  Herencia es un concepto en el que una clase puede heredar atributos y metodos de otra clase. 
# Esto permite reutilizar codigo y crear clases mas especificas a partir de una clase base.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Starting the vehicle")

    def stop(self):
        print("Stopping the vehicle")   


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def tanquear(self):
        print("Refueling the car")

my_car = Car("Toyota", "Camry", 2020, "Gasoline")
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry
print(my_car.year)  # Output: 2020
my_car.start()  # Output: Starting the vehicle
my_car.refuel()  # Output: Refueling the car
my_car.stop()  # Output: Stopping the vehicle

"""
El polimorfismo es uno de los principios fundamentales de la programación orientada a objetos (OOP). 
En Python, el polimorfismo permite que objetos de diferentes clases puedan ser tratados de la misma manera, 
incluso si estos objetos implementan métodos de manera diferente. Esto se logra mediante la definición de métodos en 
una clase base que pueden ser sobrescritos por las clases derivadas.
"""
class Animal:
    def sonido(self):
        raise NotImplementedError("Debes implementar el método sonido en la subclase")

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    def sonido(self):
        return "Miau"
 
def hacer_sonido(animal):
    print(animal.sonido())

perro = Perro()
gato = Gato()

hacer_sonido(perro)  # Imprime: Guau
hacer_sonido(gato)   # Imprime: Miau
