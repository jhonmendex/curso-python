"""
Comprender qué son las listas y las tuplas en Python.
Aprender a crear y manipular listas y tuplas.
Conocer las diferencias y usos adecuados de listas y tuplas.
Practicar con ejemplos para consolidar los conceptos.
"""

""" las listas son colecciones ordenadas y mutables de elementos, pueden contener cualquier tipo de elemento"""
#listas
#creacion de una lista
lista = [1, 2, 3, 4, 5]
lista_con_elementos_diferentes = [1, "hola", True, 3.14]
print(lista)
print(lista_con_elementos_diferentes)

#acceso a elementos de la lista
print(lista[0]) #imprime 1
print(lista_con_elementos_diferentes[1]) #imprime "hola"
print(lista[-1]) #imprime 5
print(lista_con_elementos_diferentes[-2]) #imprime True
print(lista[1:4]) #imprime [2, 3, 4]
print(lista_con_elementos_diferentes[1:4]) #imprime ["hola", True, 3.14]
print(lista[:3]) #imprime [1, 2, 3]
print(lista_con_elementos_diferentes[:3]) #imprime [1, "hola", True]
print(lista[3:]) #imprime [4, 5]
print(lista_con_elementos_diferentes[3:]) #imprime [3.14]
print(lista[::-1]) #imprime [5, 4, 3, 2, 1]
print(lista_con_elementos_diferentes[::-1]) #imprime [3.14, True, "hola", 1]
print(lista[::2]) #imprime [1, 3, 5]
print(lista_con_elementos_diferentes[::2]) #imprime [1, "hola", 3.14]
print(lista[1::2]) #imprime [2, 4]
print(lista_con_elementos_diferentes[1::2]) #imprime ["hola", True]
print(lista[1:4:2]) #imprime [2, 4]
print(lista_con_elementos_diferentes[1:4:2]) #imprime ["hola", True]


#manipulacion de listas (mutabilidad)
lista.append(6) #agrega un elemento al final de la lista
print(lista) #imprime [1, 2, 3, 4, 5, 6]
lista.extend([7, 8, 9]) #agrega una lista al final de la lista
print(lista) #imprime [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(0, 0) #inserta un elemento en una posicion especifica
print(lista) #imprime [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.remove(5) #elimina el elemento especificado
print(lista) #imprime [0, 1, 2, 3, 4, 6, 7, 8, 9]
lista.pop() #elimina el ultimo elemento
print(lista) #imprime [0, 1, 2, 3, 4, 6, 7, 8]
lista.pop(0) #elimina el elemento en la posicion especificada
print(lista) #imprime [1, 2, 3, 4, 6, 7, 8]
lista.clear() #elimina todos los elementos
print(lista) #imprime []
lista = [1, 2, 3, 4, 5]
#del lista #elimina la lista
print(lista) #imprime NameError: name 'lista' is not defined
lista = [1, 2, 3, 4, 5]
lista.sort() #ordena la lista
print(lista) #imprime [1, 2, 3, 4, 5]
lista.reverse() #invierte la lista
print(lista) #imprime [5, 4, 3, 2, 1]
lista.sort(reverse=True) #ordena la lista en orden inverso
print(lista) #imprime [5, 4, 3, 2, 1]
lista.sort(reverse=False) #ordena la lista en orden normal
print(lista) #imprime [1, 2, 3, 4, 5]



""" las tuplas son colecciones ordenadas e inmutables de elementos, pueden contener cualquier tipo de elemento"""
#tuplas
#creacion de una tupla
tupla = (1, 2, 3, 4, 5)
tupla_con_elementos_diferentes = (1, "hola", True, 3.14)
print(tupla)
print(tupla_con_elementos_diferentes)
#acceso a elementos de la tupla
print(tupla[0]) #imprime 1
print(tupla_con_elementos_diferentes[1]) #imprime "hola"
print(tupla[-1]) #imprime 5
print(tupla_con_elementos_diferentes[-2]) #imprime True
print(tupla[1:4]) #imprime (2, 3, 4)
print(tupla_con_elementos_diferentes[1:4]) #imprime ("hola", True, 3.14)
print(tupla[:3]) #imprime (1, 2, 3)
print(tupla_con_elementos_diferentes[:3]) #imprime (1, "hola", True)
print(tupla[3:]) #imprime (4, 5)

#manipulacion de tuplas (inmutabilidad)
tupla = (1, 2, 3)
tupla = tupla + (4, 5) #concatena tuplas
print(tupla) #imprime (1, 2, 3, 4, 5)
tupla = tupla[:2] + (0, ) + tupla[2:] #agrega un elemento en una posicion especifica
print(tupla) #imprime (1, 2, 0, 3, 4, 5)
tupla = (1, 2, 3)
tupla = tupla * 2 #repite la tupla
print(tupla) #imprime (1, 2, 3, 1, 2, 3)
tupla = (1, 2, 3)
tupla = tupla[1:2] #crea una subtupla
print(tupla) #imprime (2,)
tupla = (1, 2, 3)
tupla = tupla[1:2] + tupla[2:] #crea una subtupla
print(tupla) #imprime (2, 3)

#recorrido de listas y tuplas
for elemento in lista:
    print(elemento)

for elemento in tupla:
    print(elemento)

#ejemplo de recorrido listas
lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)
    if elemento == 3:
        break
    
    #ejemplo de recorrido tuplas
tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)
    if elemento == 3:
        break



