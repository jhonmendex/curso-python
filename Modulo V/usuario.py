class Usuario:
    def __init__(self, id, nombre, correo, contrasena):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

    def  __str__(self):
        return f"nombre: {self.nombre}, correo: {self.correo}, contrasena: {self.contrasena}"
    

    