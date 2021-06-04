#identificador 
#no puede empezar con números ni con _
#siempre empieza con una letra, luego pueden venir letras, números o guiones bajos

#signo de igual '='
#valor a asignar

v_num1 = 10
print(v_num1)
v_num1 = 5
print(v_num1)
v_num2 = 15
print(v_num2)
print(v_num1)

#Tipos de Datos

#primitivos

#Numericos
#entero -> int
#decimal -> float (tambien existe el double)

#Cadenas de texto
#String -> "Hola como estas"
#char -> 'a' 

#Logicos o booleanos
#bool -> solo puede tener 2 valores, verdadero o falso

v_num1 = "Hola como estas"
print(v_num1)


#función para poder saber de que tipo es una variable
#se llama type()
print(type(v_num1)) #-> str -> string

v_num1 = 5

print(type(v_num1)) #-> int -> entero

v_num1 = 12.5

print(type(v_num1))

v_num1 = True #como False

print(type(v_num1))

#Operadores

#Aritmeticos
'''
+ -> suma 
- -> resta
* -> multiplicación
/ -> división
** -> potencia 2**2
% -> modulo (3/2) = 1.5 -> 1 (2/2) -> 0
'''

#Logicos -> siempre devuelven valores lógicos (booleanos) y siempre trabajan con valores lógicos
'''
and
or
not -> sirve para negar
'''

#Relacionales -> siempre devuelven valores lógicos
'''
< -> menor 5 < 3 -> falso
> -> mayor 5 > 3 -> verdadero
<= -> menor igual 5 <= 3 -> falso 
>= -> mayor igual 5 >= 3 -> verdadero 
== -> igualdad 5 == 3 -> falso 
!= -> distinto 5 != 3 -> verdadero

'''

'''

#tarea 1
a = 2
b = 3
c = 4
a = b + c ->que valor toma b, que valor toma c y al final que valor toma a
b = b + 1 
c = 6
a = c + 2
c = b + a
b = c
c = 5 + 2
a = a + b + c + 1
b = 3
c = a + b * c
a = b + 1 

Indicar el valor que van a tener 
todas las variables (a, b y c) a mano y paso por paso.


#tarea 2
Hagan un programa
que pida 2 números al usuario
y que devuleva: 
su suma
su resta
su multiplicación 
y su división


'''