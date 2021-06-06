persona1 = int(input("Persona 1, Ingrese su edad: "))

numero1 = 0
numero2 = 0

nombre = ''
decimal = 0.0
bolean = True

if (persona1 >= 18):
    print("Usted es mayor de 18 años por lo tanto puede participar")
    numero1 = float(input("Persona1, ingrese un número del 0 al 100: "))
else: 
    print("Usted es menor de edad, no puede participar")

persona2 = int(input("Persona 2, Ingrese su edad: "))

if (persona2 >= 18):
    print("Usted es mayor de 18 años por lo tanto puede participar")
    numero2 = float(input("Persona2, ingrese un número del 0 al 100: "))
else: 
    print("Usted es menor de edad, no puede participar")


if (numero1 > numero2):
    print("La persona 1 ingreso el número: ", numero1, " por lo tanto gano 100 dolares")
    print("La persona 2 no gano nada")
else: 
    print("La persona 2 ingreso el número: ", numero2, " por lo tanto gano 100 dolares")
    print("La persona 1 no gano nada")