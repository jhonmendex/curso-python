"""1...reto: simular una maquina expendedora de comida"""
#maquina expendedora de comida
#1. ingresar dinero
#2. comprar producto
#3. devolver cambio
#4. salir
menu = """
Bienvenido a la maquina expendedora de comida
1. Ingresar dinero
2. Consultar productos
3. Comprar producto
4. Devolver cambio
5. Salir
"""
gaseosa = 3000
papas = 2000
gomitas = 200
dinero = 0

bandera = True
while(bandera):
    print(menu)
    opcion = int(input("Ingrese una opción: "))
    if(opcion == 1):        
        dinero = int(input("Ingrese dinero: "))
        print("Dinero ingresado: ", dinero)
    elif(opcion == 2):
        print("Productos disponibles")
        print("1. Gaseosa $3000 🥤")
        print("2. Papas   $2000 🍟")
        print("3. Gomitas $200 🥑")
    elif(opcion == 3):
        print("Compra realizada")
        producto = int(input("Ingrese el producto a comprar: "))
        if(producto == 1):
            print("Gaseosa $3000")
            dinero = dinero - 3000
            print("Dinero restante: ", dinero)
        elif(producto == 2):
            print("Papas $2000")
            dinero = dinero - 2000
            print("Dinero restante: ", dinero)
        elif(producto == 3):
            print("Gomitas $200")
            dinero = dinero - 200
            print("Dinero restante: ", dinero)
        else:
            print("Producto no disponible")
    elif(opcion == 4):
        print("Devolver cambio")
        print("Dinero restante: ", dinero)
    elif(opcion == 5):
        print("Hasta pronto!")
        bandera = False
    else:
        print("❌!!!Opcion invalida!!!")
    
 
"""reto: realiza un ajuste para que se puedan ingresar monedas de diferentes denominaciones 
100,200,500 y 1000 de tal forma que podamos dar un cambio más exacto 
incrementa la cantidad de productos
"""