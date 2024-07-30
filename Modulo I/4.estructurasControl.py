"""1...sentencias condicionales if,elif, else"""
"""

if: Evalúa una condición y ejecuta el bloque de código si la condición es verdadera.
elif: (abreviatura de "else if") Evalúa otra condición si las condiciones anteriores son falsas.
else: Ejecuta un bloque de código si todas las condiciones anteriores son falsas.

"""
#ejemplos usuario y contraseña
usuario = "admin"
contraseña = "1234"
 
usuario_entrada = input("Ingrese usuario: ")
contraseña_entrada = input("Ingrese contraseña: ")

if usuario == usuario_entrada  and contraseña_entrada == "1234":
    print("Bienvenido al sistema")
else:
    print("Usuario o contraseña incorrectos")
 
#ejemplo elif

nota = 2.9
if nota >= 3:
    print("Aprobado")
elif nota >= 4.5:
    print("Aprobado con merito")
elif nota < 3:
    print("Reprobado")

"""2... ciclos for y while"""
#while
i = 1

while i <= 10:
    print(i)
    i = i + 1
    #i += 1
print("Fin del programa")

#ciclo for
for i in range(1,11):
    print(i)
    #i += 1
print("Fin del programa")

#ejemplo while con usuario y contrasena
usuario = "admin"
contraseña = "1234"
intentos = 3
while intentos > 0:
    usuario_entrada = input("Ingrese usuario: ")
    contraseña_entrada = input("Ingrese contraseña: ")
    if usuario == usuario_entrada  and contraseña_entrada == "1234":
        print("Bienvenido al sistema")
        break
    else:
        print("Usuario o contraseña incorrectos")
        intentos -= 1
        print(f"Le quedan {intentos} intentos usuario bloqueado")
