#p089-eliminar-lista.py
#Eliminar elementos de una lista

#Borrar pantalla
print('\033[H\033[J')  # Limpiar la pantalla])
print('Eliminar elementos de una lista')

nums = [10, 20, 30, 40, 50, 60, 70, 10, 20, 99]

print('\nLongitud y contenido de la lista:')
print(f'Longitud: {len(nums)} | Contenido: {nums}')

print('\nEliminar el primer elemento (10):')
nums.remove(10)
print(f'Longitud: {len(nums)} | Contenido: {nums}')

print('Elimina el elemento en la posición 4:')
del nums[4]
print(f'Longitud: {len(nums)} | Contenido: {nums}')

print('\nEliminar el elemento en la posición 6 utillizando pop():')
nums.pop(6)
print(f'Longitud: {len(nums)} | Contenido: {nums}')

print('\nEliminar el último elemento (99):')
nums.pop()
print(f'Longitud: {len(nums)} | Contenido: {nums}')
