#p018-area-volumen-cilindro.py
#Crea un programa que calcule el área y volumen de un cilindro. 
# Pide al usuario que ingrese el radio (R) y la altura (h) del cilindro. 
# Las fórmulas para el cálculo de área y de volumen son: Area = 2 π (R + h) ----- Volumen = π * R2 * h

import math as mt

print ("\033[2J\033[h", end="")
print ('Calcula el area y el volumen de un cilindro \n')

#Entreda 
r=float(input('Ingrese el radio del cilindro (m): '))
h=float(input('Ingrese la altura del cilindro (m): '))

#Proceso
area = 2*mt.pi*(r + h) 
volumen = mt.pi*(r**2)*h

#Salida

print(f'El Area del cilindro es {area:.2f}, y tiene un volumen de {volumen:.2f}. ')