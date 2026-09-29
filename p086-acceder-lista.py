#p086-acceder-lista.py
# Acceder a elementos de una lista

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print('\033[H\033[J')  # Limpiar la pantalla])

print('Acceder a elementos de una lista')

print('\nLongitud y contenido de la lista:')
print(f'Longitud: {len(nums)}')
print(f'Contenido: {nums}')

print('\nPor indice positivo:')
print(f'Elemento enel indice 0 y 5: {nums[0]} y {nums[4]}')

print('\nPor indice negativo:')
print(f'Elemento en el indice -6 y -10  : {nums[-10]} y {nums[-6]}')

print('\nPor ramgo:')
print(f'De 2 a 5: (sin incluir el 5)');
print(f'Elementos: {nums[2:5]}')

print('\nPor saltos:')
print(f'Elemento con saltos de 2: {nums[::2]}')
print(f'Elemento con saltos de 3: {nums[::3]}')