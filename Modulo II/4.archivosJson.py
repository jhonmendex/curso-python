"""
manejo de archivos JSON con python
JSON ES UNA FORMA DE REPRESENTAR DATOS EN FORMATO TEXTO
Un objeto JSON es una colección de pares clave-valor.
Una lista JSON es una colección ordenada de valores.
"""
import json
import pprint
file_path = 'datos.json'

#with es lo que se denomina context manager que asegura que los recursos se manejen de manera segura y eficiente. sirve para conexiones a bd

#leer un archivo python, Usar json.load() para leer un archivo JSON y convertirlo en un diccionario de Python.
with open(file_path, 'r') as file:
    data = json.load(file)
    print(type(data))
    pprint.pprint(data)


#escritura de archivos json
datos_nuevos = {
    "nombre": "Jhon",
    "edad": 40,
    "ciudad": "Bogota",
    "hobbies": ["leer", "caminar"]
}

data.append(datos_nuevos)

with open(file_path, 'w') as file:

    json.dump(data, file, indent=4)
    print("Archivo JSON creado correctamente.")



 