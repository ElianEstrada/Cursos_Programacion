import os
import platform

#Solicitar al usuario 2 números


if platform.system() == 'Linux':
    os.system('clear')
else: 
    os.system('cls')

#función int()
#función float()

#int() -> cuando queramos datos enteros
#float() -> cuando queramos datos decimales

v_num1 = float(input("Ingrese un número: "))                       #3
v_num2 = input("Ingrese otro número: ")                     #4
v_num2 = float(v_num2)

print(f"El resultado de la suma es: {v_num1 + v_num2}")     #7
print(f"El resultado de la resta es: {v_num1 - v_num2}")
print(f"El resultado de la multiplicación es: {v_num1 * v_num2}")


#Estructura de control 
#Condicionales

#if - else 
#if - else el else es opcional 
#elif de lo contrario si 

if (v_num2 == 0):
    #lo que quiero que pase si es verdadero
    print("No se puede dividir por 0")
else:
    #lo que quiero que pase si es falso
    print(f"El resultado de la división es: {v_num1 / v_num2}")