#p110-comprension-filtra-palabras.py
# Dada una lista de palabras introducidas por el usuario separadas por espacios, utilizar comprensión de listas
# para crear una nueva lista que contenga solo aquellas palabras que tengan más de 4 caracteres y convertirlas a
# mayúsculas. Imprimir la lista original y la lista filtrada.

#Borrar pantalla
print('\033[2J\033[1;1H')

palabras = list(input("Introduzca palabras separadas por espacios: ").split())
lista_fil = []

for pal in palabras:
    if (len(pal) > 4 ):
        lista_fil.append(pal.upper())
print('--- Resultados ---')
print(f'Lista Original: {palabras}')
print(f'Lista filtrada (>4 caracteres en mayúsculas): {lista_fil}')