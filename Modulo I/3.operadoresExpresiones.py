"""1... Operadores aritméticos, relacionales y lógicos"""
#operadores aritmeticos
suma = 5 + 3
resta = 10 - 4
multiplicacion = 3 * 2
division = 15 / 3
modulo = 17 % 3
exponente = 2 ** 3
division_entera = 15 // 2
print(modulo)

#operadores relacionales
mayor_que = 5 > 3
menor_que = 3 < 5
igual = 5 == 5
diferente = 5 != 3
mayor_o_igual = 5 >= 5
menor_o_igual = 3 <= 5
print(igual)

#operadores lógicos
y_logico = True and False
o_logico = True or False
negacion = not True
print(y_logico)
#ejemplo
usuario = True
contrasena = False
inicio_sesion = usuario or contrasena
print("inicio de sesion", inicio_sesion)

"""2... Expresiones condicionales"""
""" Las expresiones son combinaciones de valores, variables y operadores que Python evalúa y produce un valor."""
#https://recursos.pacoelchato.com/img/YBHU7L482hY4Ry7xUqLAmGk4iJPdx9oxVaGU9pGl.png
a = 10
b = 5
c = 2

# Ejemplo de expresión aritmética
resultado = (a + b) * c  # resultado será 30

# Ejemplo de expresión relacional
comparacion = (a > b)  # comparacion será True

# Ejemplo de expresión lógica
logica = (a > b) and (b > c)  # logica será True

# Ejercicio 3
es_adulto = False
tiene_permiso = False

print("es_adulto y tiene_permiso:", es_adulto and tiene_permiso)
print("es_adulto o tiene_permiso:", es_adulto or tiene_permiso)
print("no es_adulto:", not es_adulto)