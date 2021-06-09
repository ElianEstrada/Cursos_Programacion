print("Bienvenidos\n1. Imprmir su nombre\n2. Mostrar operaciones básicas\n3. Salir")
opcion = int(input("Ingrese una opción: "))

if (opcion == 1):
    #Aca se ingresa a la opción 1, para pedir nombre y apellido
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    print(f"Su nombres es: {nombre} y su apellido es: {apellido}")


