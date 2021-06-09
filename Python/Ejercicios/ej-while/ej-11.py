#ciclo while -> va permitir ejecutar un bloque de código
#hasta que se cumpla cierta condición

#Estructura del while
#'while' ( condicion ) ':' # si es verdadera reipte, si es falsa se detiene
#   bloque de código    

num1 = 5
num2 = 3
contador = 1

while (num1 > num2):
    if (contador == 3):
        num2 = 6
    print(contador)
    contador = contador + 1
    

print(num2)