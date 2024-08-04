from usuarioControlador import usuarioControlador
from flask import Flask
from flask import request
controladorUsuario = usuarioControlador()

app = Flask(__name__)

@app.route('/usuarios', methods=['GET'])
def mostrar_usuarios():
  return controladorUsuario.mostrar_usuarios()

@app.route('/usuarios/<int:id>', methods=['GET'])
def buscar_usuario(id):
 return controladorUsuario.buscar_usuario(id)

@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    return controladorUsuario.agregar_usuario(request.get_json())

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
 return controladorUsuario.eliminar_usuario(id)

@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
 return controladorUsuario.actualizar_usuario(id, request.get_json())

if __name__ == '__main__':
    app.run(debug=True)


