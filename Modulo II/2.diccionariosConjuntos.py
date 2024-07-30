"""diccionarios y conjuntos en python
"""


# Create a dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

 # Access values by key
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # Output: dict_values(['John', 30, 'New York'])
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
print(len(my_dict))  # Output: 3
print(my_dict.get("age"))  # Output: 30
print(my_dict.pop("age"))  # Output: 30

#agregar elementos al diccionario
my_dict["age"] = 31
print(my_dict)
my_dict["occupation"] = "Engineer"
print(my_dict)

#conjuntos en python
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
print(conjunto) #imprime {1, 2, 3, 4, 5}
print(conjunto2) #imprime {3, 4, 5, 6, 7}
print(conjunto.union(conjunto2)) #imprime {1, 2, 3, 4, 5, 6, 7}
print(conjunto.intersection(conjunto2)) #imprime {3, 4, 5}
print(conjunto.difference(conjunto2)) #imprime {1, 2}
print(conjunto.symmetric_difference(conjunto2)) #imprime {1, 2, 6, 7}
print(conjunto.isdisjoint(conjunto2)) #imprime False
print(conjunto.issubset(conjunto2)) #imprime False

#agregar elementos al conjunto
conjunto.add(6) #agrega un elemento al conjunto
print(conjunto)

#recorrido de conjuntos
for elemento in conjunto:
    print(elemento)
    if elemento == 3:
        break
    
#recorrido de diccionarios
for clave, valor in my_dict.items():
    print(clave, valor)
    if clave == "age":
        break
    


