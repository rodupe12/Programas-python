#p002-area-circulo.py
#>Calcular el area de un circulo

import math # Importar la libreria de constantes y funciones matematicas

print ("\033[2J\033[h", end="")
print('Calculando el area de un circulo \n')

radio = float(input('Dame el radio? '))

#Area = math.pi * radio ** 2
area = math.pi * math.pow (radio, 2)

print(f'El círculo de radio {radio:.2f} tiene un area de {area:.2f}')