
'''
a = 2
b = 3
c = 4
a = b + c -> que valor toma b, que valor toma c y al final que valor toma a
b = b + 1 
c = 6
a = c + 2
c = b + a
b = c
c = 5 + 2
a = a + b + c + 1
b = 3
c = a + b * c
a = b + 1 '''

a = 2
b = 3
c = 4
a = b + c                       # a = 3 + 4 -> a = 7
b = b + 1                       # b = 3 + 1 -> b = 4
c = 6
a = c + 2                       # a = 6 + 2 -> a = 8
c = b + a                       # c = 4 + 8 -> c = 12
b = c                           # b = 12
c = 5 + 2                       # c = 7
a = a + b + c + 1               # a = 8 + 12 + 7 + 1 -> a = 28
b = 3
c = a + b * c                   # c = 28 + 3 * 7  -> c = 28 + 21 -> c = 49
a = b + 1                       # a = 3 + 1 -> a = 4

#Veredicto final: 
# a = 4
# b = 3
# c = 49

print(a, b, c) 

