#p015-hipotenusa-triangulo.py
#Crea un programa que calcule la longitud de la hipotenusa de un triángulo rectángulo. 
# El programa debe solicitar al usuario que ingrese la longitud de los dos lados (catetos) del triángulo. 
# Para el cálculo, utiliza la siguiente fórmula: hipotenusa = raizcuadrada( longlado1 * lognlado1 + longlado2 * longlado2 )

#Rodrigo D

import math as mt

print ("\033[2J\033[h", end="")
print ('Calcula la longitud de la hipotenusa de un triángulo rectángulo \n')

#Entreda 
l1=float(input('Ingrese la longitud del primer lado del triángulo rectángulo: '))
l2=float(input('Ingrese la longitud del segundo lado del triángulo rectángulo: '))

#Proceso
hip = mt.sqrt( (l1*l1) + (l2*l2) )

#Salida

print(f'El valor de la hipotenusa del triángulo rectángulo con lados {l1} y {l2} es: {hip}')

