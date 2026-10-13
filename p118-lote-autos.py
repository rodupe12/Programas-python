#p118-lote-autos.py
#Crear una lista de diccionarios para almacenar los datos de varios autos
autos = [
    {'marca':'Toyota','modelo':'Camry','año':2020,'precio':25000},
    {'marca':'Honda', 'modelo':'Civic','año':2019,'precio':22000},
    {'marca':'Ford',  'modelo':'Focus','año':2021,'precio':23000}
]

#Borrar pantalla
print("\033[H\033[J")

autos.append({'marca':'Chebrolet',  'modelo':'Malibu','año':2022,'precio':23000})

# Mostrar los datos de cada auto en la lista
print(f'\nTodos los autos: {autos} - {len(autos)} elementos')
print('Datos de cada auto: ')
for auto in autos:
    print(auto)
    print()

#Mostra los datos en forma de tabla
print('Datos de los autos en frma de tabla:')
print(f"{'Marca':<15} {'Modelo':<15} {'Año':<5} {'Precio':<10}")
for auto in autos:
    print(f"{auto ['marca']:<15} {auto['modelo']:<15} {auto['año']:<5} ${auto['precio']:<10,.2f}")

#Mostrar los autos en forma de registro
print('\nDatos de los autos en forma de registro:')
for auto in autos:
    for k, v in auto.items():
        print(f'{k}: {v}')
    print()


