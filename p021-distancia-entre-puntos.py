#p021-distancia-entre-puntos.py
#Crea un programa que calcule la distancia entre dos puntos en un plano cartesiano. 
# El programa debe pedir al usuario que ingrese las coordenadas del punto A (x1,y1) y las coordenadas del punto B (x2,y2). 
# Utiliza la siguiente fórmula para calcular la distancia: /(x2 - x1)2 + (y2-y1)2 

import math as mt

print ("\033[2J\033[h", end="")
print ('Calcula la distancia entre dos puntos en un plano carteciano \n')

#Entreda 
print ('Ingrese los valores de las cordenadas "x1" , "y1": ')
x1,y1 = input().split(',')
x1= int(x1)
y1= int(y1)

print ('Ingrese los valores de las cordenadas "x2" , "y2": ')
x2,y2 = input().split(',')
x2= int(x2)
y2= int(y2)

#Proceso
distancia = mt.sqrt( (x2 - x1)**2 + (y2-y1)**2 )

#Salida

print(f'La distancia entre los dos puntos es: {distancia}')