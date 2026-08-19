#p012-funcion-matematicas-equacion.py
#Ejemplifica el uso de funciones matematicas dentro de mat

import math as mt # as mt para darle un aleas y sea mas facil llamrlo

print ("\033[2J\033[h", end="")
print ('Operadores de asignacion en Python \n')

# Evaluar la función f(x, y) = 3x2 + √(x2 + y2) + e^(ln(x))

x = int(input('Valor de x : '))
y = int(input('Valor de y : '))

fxy = 3 * mt.pow(x,2) + mt.sqrt( mt.pow(x,2) + mt.pow(y,2) ) + mt.exp( mt.log(x) )
fxy2 = 3 * x**2 + mt.sqrt( x**2 + y**2 ) + mt.exp( mt.log(x) )

print(f'El resultado es : {fxy:,.2f}')
print(f'El resultado 2 es : {fxy2:,.2f}')