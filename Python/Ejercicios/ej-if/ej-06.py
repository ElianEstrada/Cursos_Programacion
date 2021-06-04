#if es la condición padre -> este siempre tiene que ir.
#opcionalmente
#elif una condición alterna -> no siempre tiene que ir. Esta se ejecutara si el if da falso
#else -> sino comodin o default 

""" 5 >= 4 #-> si o que no -> verdadero y falso
5 <= 4
5 < 4
5 > 4
5 == 4
5 != 4 #Diferente  """

#Operadores
v_num1 = 5
v_num2 = 4

#5 y 4
print(v_num1 > v_num2)          #True
print(v_num1 >= v_num2)         #True
print(v_num1 < v_num2)          #False
print(v_num1 <= v_num2)         #False
print(v_num1 == v_num2)         #False
print(v_num1 != v_num2)         #True


if (v_num1 != v_num2):
    print("entro")
else: 
    print("no entro")



'''

#los que todavía no lo dominan bien
van a pedir 2 edades
y van a comparar cual de los dos es mayor.
y el que se mayor le van a dar 100 dolares.
#Imprimir que gano 100 dolares -> para el mayor.
#Imprimir que no gano nada -> para el menor

'''


'''

Hacer un menu con 3 opciones
1. Imprima su nombre
2. Muestre operaciones básicas
3. Salir

en la primera opción:
pidan su nombre y apellido
y muestren su nombre completo

en la 2da opción: 
quiero que pidan 2 numeros eh indiquen
su suma, su resta, su multiplicación, su división
y cual de los dos es mayor.

en la 3ra opción: 
Que termine la aplicación.

'''