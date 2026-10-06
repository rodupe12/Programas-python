##p102-aplanar-matriz.py
#Aplana una matriz de 2 dimensiones en una lista de 1 dimension usando comprecion de listas

print('\033[2J\033[1;1H') #Borrar pantalla
print('Aplana una matriz de 2 dimensiones en una lista de 1 dimension usando comprecion de listas')

matriz = [[1, 2, 3], [-4, 5, 6], [-7, 8, 9]]

#se aplana la matriz usando comprecion de listas
aplanada = [elemento for fila in matriz for elemento in fila]
positivos = [elemento for fila in matriz for elemento in fila if elemento > 0]
negativos = [elemento for fila in matriz for elemento in fila if elemento < 0]
print('Matriz original:', matriz)
print('Matriz aplanada:', aplanada)
print('Elementos positivos:', positivos)
print('Elementos negativos:', negativos)

