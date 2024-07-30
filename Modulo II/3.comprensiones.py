"""comprensiones de listas, tuplas 
[nueva_lista for elemento in iterable if condición]

Las comprensiones de listas y diccionarios son una forma concisa y eficiente de crear listas y diccionarios en Python. P
"""
#comprension de listas
numeros = [1, 2, 3, 4, 5]
cuadrados = [numero**2 for numero in numeros]
print(cuadrados) #imprime [1, 4, 9, 16, 25]

#filtrar elementos de una lista
numeros = [1, 2, 3, 4, 5]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares) #imprime [2, 4]

#convertir caracteres a mayusculas
palabras = ["hola", "mundo"]
mayusculas = [palabra.upper() for palabra in palabras]

"""
comprensiones de diccionarios
{clave: valor for elemento in iterable if condición}
"""
#crear un diccionario con los numeros y sus cuadrados
numeros = [1, 2, 3, 4, 5]
cuadrados = {numero: numero**2 for numero in numeros}
print(cuadrados) #imprime {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#Filtrar y transformar elementos en un diccionario:
palabras = ["hola", "mundo", "python", "es", "genial"]
longitudes = {palabra: len(palabra) for palabra in palabras if len(palabra) > 3}
print(longitudes)  # {'hola': 4, 'mundo': 5, 'python': 6, 'genial': 6}