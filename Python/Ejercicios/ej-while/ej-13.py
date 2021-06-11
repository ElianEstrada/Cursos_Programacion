###Tablas de multiplicar con el ciclo While###
#str() -> convertir una variable a string
num_tabla = int(input("Ingrese la tabla de multiplicar que desa ver: "))

contador = 1

while(contador <= 20):
    #1 x 1 = 1
    #1 x 2 = 2
    #1 x 3 = 3
    print(f"{num_tabla} x {contador} = {num_tabla * contador}")
    #print(str(num_tabla) + " x " + str(contador) + " = " + str(num_tabla * contador))
    contador += 1

