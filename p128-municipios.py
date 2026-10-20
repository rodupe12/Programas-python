#p128-municipios.py
#Gestion de un patron municipal utilizando conjuntos

municipios = {'Zacatecas', 'Guadalupe', 'Fresnillo', 'Jerez', 'Sombrerete', 'Fresnillo'}

#Borrador de pantalla
print('\033[H\033[J')

print('Padron de municipios\n')
print('=======================')
print(f'La colección es del tipo : {type(municipios)}')
print(f'Longitud del padrón : {len(municipios)}')
print(f'Padrón original : \n{municipios}\n')

print("\nLista de municipios registrados:")
for mun in municipios:
    print(mun, end=' | ')

#Consultar si un municipio esta registrado
print(f'\n\n¿Está Zacatecas en el padrón?: {"Zacatecas" in
municipios}')

#Alta al padron de municipios
print('\nAgregar un municipio al padron')
municipios.add("Teul")
print(f'Municipios registrados: {municipios} - {len(municipios)}')

otros_municipios = {"Luis Moya", "Ojocaliente", "Tepetongo"}
municipios.update(otros_municipios)
print(f'Alta con Update() (varios): \n{municipios}\n')

#Eliminar un municipio del padron utilizando remove()
print("\n--- Bajas del Padrón ---")
municipios.remove('Zacatecas')
print(f'Baja con Remove() (Zacatecas): \n{municipios}\n')

#Elimina un municipio del padron con discard()
municipios.discard("Ojocaliente")
print(f'Baja con Discard() (Ojocaliente): \n{municipios}\n')

#Elimina un municipio del padron con pop()
mun_eliminado = municipios.pop()
print(f'Baja con Pop() (elemento arbitrario): \n{municipios} \nEliminado: {mun_eliminado}\n')

municipios.clear()
print(f'Padrón vaciado con Clear(): \n{municipios}\n')


