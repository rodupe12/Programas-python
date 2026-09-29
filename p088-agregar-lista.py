#p088-agregar-lista.py
#Agregar elementos a una lista

#Borrar pantalla
print('\033[H\033[J')  # Limpiar la pantalla])
print('Agregar elementos a una lista')

nums = [10, 20, 30, 40, 50, 60, 70, 10, 20, 99]

print('\nLongitud y contenido de la lista:')
print(f'Longitud: {len(nums)} | Contenido: {nums}')

print('\nAgregar 90 y 100 al final de la lista:')
nums.append(90)
nums.append(100)
print(f'Longitud: {len(nums)} | Contenido: {nums}')

print('\n Insertar 80 en la posicion 4')
nums.insert(4, 80)
print(f'Longitud: {len(nums)} | Contenido: {nums}')

print('\nExtender la lista con otra lista [110, 120, 130]')
nums.extend([110, 120, 130])
print(f'Longitud: {len(nums)} | Contenido: {nums}')
