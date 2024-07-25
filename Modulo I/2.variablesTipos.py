"""1...variables y tipos"""
"""
Las variables son contenedores para almacenar datos.
Permiten a los programadores etiquetar y manipular datos en sus programas.
Es la representación simbolida de un dato
"""

#ej1
numero = 10
nombre = "Juan"
altura = 1.75
es_alto = True


"""2...reglas de nomenclatura"""
"""Los nombres de las variables deben comenzar con una letra (a-z, A-Z) o un guion bajo (_).
El resto del nombre puede incluir letras, números y guiones bajos.
Ejemplos de nombres válidos: mi_variable, variable2, _variable.
camelCase  -> primerNombre
PascalCase -> PrimerNombre
snake_case -> primer_nombre
lowercase  -> primernombre
uppercase  -> PRIMERNOMBRE
uppercase snake_case -> PRIMER_NOMBRE
"""

# Ejemplo quiero calcular el salario de una persona a partir del valor de la hora y la cantidad

valor_hora = 10500
cantidad_horas = 8
salario = valor_hora * cantidad_horas

print("El salario de la persona es: ",salario)

"""3...Tipos de datos básicos"""
#Enteros: Números enteros, positivos o negativos, sin decimales.
cantidad_productos = 10
temperatura = -5

#Flotantes: Números con decimales.
precio = 99.99
descuento = 0.25
total = precio * (1 - descuento)

#Cadenas: Cadena de caracteres, representan texto.
nombre = "Juan"
mensaje = 'Hola, "mundo"'
mensaje2 = "Hola, 'mundo'"

#boleanos
es_alto = True
tiene_descuento = False
es_jubilado = False
es_jubilado = True

"""4...conversiones de tipos"""
#es necesaria la conversion de tipos para poder operar con diferentes tipos de datos
#ejemplo
valor_hora = 5
cantidad_horas = input("Ingrese la cantidad de horas: ")
salario = valor_hora * cantidad_horas
print("el salario es", salario)
#convertir un numero a un string
numero = 42 
numero_str = str(numero)
print(type(numero_str))
print(numero_str)
#convertir un string a un numero
numero_str = "42"
numero = int(numero_str)
print(type(numero))
print(numero_str)
#convertir un numero a un flotante
numero = 42
numero_float = float(numero)
print(type(numero_float))
print(numero_float)
#convertir string a booleano
cadena = "True"
booleano = bool(cadena)
print(type(booleano))
print(booleano)
#convertir string a flotante
cadena = "3.14"
flotante = float(cadena)
print(type(flotante))
print(flotante)