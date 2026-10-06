##p098-cuadrados-lista.py
#Genera cuadrados usando comprecion de listas

#Borrar pantalla
print('\033[2J\033[1;1H')

print('Cuadrados de 1 a n usando compresión de listas')
n = int(input('Ingrese el valor de n: '))

numeros = list(range(1, n + 1))
cuadrados = [x**2 for x in numeros] # Comprenpresion de lsitas para calcular los cuadrados

print(f'Los numeros del 1 al {n} son: {numeros}')
print(f'Los cuadrados del 1 al {n} son: {cuadrados}')

