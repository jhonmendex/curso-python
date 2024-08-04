from modelos.persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def mostrar_informacion(self):
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base}, Especialidad: {self.especialidad}"