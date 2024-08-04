from usuario import Usuario
from flask import jsonify

class usuarioControlador:
    def __init__(self):
        self.usuarios = [
            Usuario(1, "Santiago", "santiago@gmail.com","123"),
            Usuario(2, "Juan", "juan@gmail.com","456"),
            Usuario(3, "Pedro", "pedro@gmail.com", "789")  
        ]

    def agregar_usuario(self,usuario):
        usuario = Usuario(usuario['id'], usuario['nombre'], usuario['correo'], usuario['contrasena'])
        self.usuarios.append(usuario)
        return jsonify({'mensaje': f'Usuario {usuario} agregado correctamente'}), 201

    def mostrar_usuarios(self):
        usuarios = [usuario.__dict__ for usuario in self.usuarios]
        return  jsonify(usuarios)
            
    def buscar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return jsonify(usuario.__dict__), 200
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
    def eliminar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:        
                self.usuarios.remove(usuario)
                return jsonify({'mensaje': 'Usuario eliminado correctamente'}), 200
        return jsonify({'error': 'Usuario no encontrado'}), 404
    
    def actualizar_usuario(self, id, usuario_actualizado):

          for usuario in self.usuarios:
            if usuario.id == id:
                usuario.nombre = usuario_actualizado["nombre"]
                usuario.correo = usuario_actualizado['correo']
                usuario.contrasena = usuario_actualizado['contrasena']
                return jsonify({'mensaje': 'Usuario actualizado correctamente'}), 200        
          return jsonify({'error': 'Usuario no encontrado'}), 404



 
