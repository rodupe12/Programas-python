#p087-modificar-lista.py
#Modificar elementos de una lista

#Borrar pantalla
print('\033[H\033[J')  # Limpiar la pantalla])
print('Modificar elementos de una lista')

califs = [10, 9, 8.5, 6.5, 9.8, 7, 5, 6.2, 9.5]

print('\nLongitud y contenido de la lista:')
print(f'Longitud: {len(califs)}')
print(f'Contenido: {califs}')

print('\nModificar elementos del 1 al 3:')
califs[0] = 11
califs[1] = 10
califs[2] = 9
print(f'Contenido actualizado: {califs}')
