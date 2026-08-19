#p014-funciones-trigonometricas.py
#Demostrar el uso de funciones trigonometricas y de convercion de grados

import math as mt

print ("\033[2J\033[h", end="")
print ('Demostrar el uso de funciones trigonometricas y de convercion de grados \n')

angulo = int(input('Dame un angulo en grados : '))

radianes = mt.radians(angulo)

seno = mt.sin(radianes)
coseno = mt.cos(radianes)
tangente = mt.tan(radianes)

grados = mt.degrees(radianes)

salida = ('\nResumen de funciones trigonometricas y convercion\n'
f'El seno es {seno:.4f}\n'
f'El coseno es {coseno:.4f}\n'
f'La tangente es {tangente:.4f}\n'
f'El angulo de {angulo} grados, equivale a {radianes:.4f}'
)
print(salida)