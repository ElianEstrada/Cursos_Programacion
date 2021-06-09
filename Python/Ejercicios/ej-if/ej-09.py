precio_helado = 8.0
precio_chocolate = 1.0
precio_fresa = 2.0


nombre = input("Por favor ingrese su nombre: ")
print("Bienvenido " + nombre)

chocolate = input("Quiere Chocolate? [S/N]: ")
#Función que vuelve una cadena a minusculas -> lower()
if (chocolate.lower() == "s"):
    precio_helado = precio_helado + precio_chocolate # -> precio_helado = 9.0

fresas = input("Quiere Fresas? [S/N]: ")

if (fresas.lower() == "s"):
    precio_helado = precio_helado + precio_fresa   # -> precio_helado = 10.0 o precio_helado = 11.0


print("El total a pagar por su helado es: " + str(precio_helado))