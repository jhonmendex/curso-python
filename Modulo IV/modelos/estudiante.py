from modelos.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_informacion(self):
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base}, Grado: {self.grado}"