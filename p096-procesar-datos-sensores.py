#p096-procesar-datos-sensores.py
#Procesamiento de datos de sensores
# Se tienen dos sensores que recogen 10 mediciones numéricas cada uno.
# Necesitamos un programa que realice las siguientes tareas:
from random import randint

print('\033[H\033[J')  # Limpiar la pantalla

sensor1 = []
sensor2 = []

#Genere dos listas con 10 números aleatorios (entre 1 y 10) para simular los datos de cada sensor y las muestre.
mediciones = 10

for _ in range(mediciones):
    sensor1.append(randint(1, 10))
    sensor2.append(randint(1, 10))

print("Datos del Sensor 1:", sensor1)
print("Datos del Sensor 2:", sensor2)

#Aplique una "transformación" a los datos, que consiste en elevar al cuadrado cada medición en ambas listas.

for i in range(mediciones):
    sensor1[i] = sensor1[i] ** 2
    sensor2[i] = sensor2[i] ** 2
print("\nDatos del Sensor 1 después de la transformación:", sensor1)
print("Datos del Sensor 2 después de la transformación:", sensor2)

# Cree una tercera lista que contenga la suma combinada de los datos
# transformados de ambos sensores (la suma del primer elemento de la lista 1 con
# el primero de la lista 2, y así sucesivamente).
Total_suma = []
for i in range(mediciones):
    Total_suma.append(sensor1[i] + sensor2[i])
print("Suma combinada de los datos transformados:", Total_suma)

#Muestre las listas transformadas y la lista combinada final.
print("\nResumen de los datos procesados:")
print("Sensor 1 transformado:", sensor1)
print("Sensor 2 transformado:", sensor2)
print("Suma combinada de los datos transformados:", Total_suma)