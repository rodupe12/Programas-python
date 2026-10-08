#p107-listas-aleatorios-suma.py
#Leer nombres de ciudades en una lista, continuando hasta que el usuario introduzca el carácter $. Imprimir:

import random


#Borrar pantalla

listaA = []
listaB = []
for i in range(10):
    listaA.append(random.randint(1, 20))
    listaB.append(random.randint(1, 20))

print('--- Listas Generadas ---')
print(f'Lista A: {listaA}')
print(f'Lista A: {listaB}')

listaC = []
for i in range(len(listaA)):
    if ((listaA[i] % 2) != 0 and (listaB[i] % 2) != 0):
        listaC.append(listaA[i] + listaB[i])
    else:
        listaC.append(0)

print('---Resultado (Suma solo si A[i] y B[i] son ambos impares) ---')
print(f'Lista C: {listaC}')



