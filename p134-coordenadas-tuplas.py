#p134-coordenadas-tuplas.py
#

zacatecas = ("Zacatecas", 22.77, -102.58)
guadalupe = ("Guadalupe", 22.75, -102.52)

print("Coordenadas de Zacatecas:")
print("Tipo    :", type(zacatecas))
print("Ciudad  :", zacatecas[0])
print("Latitud :", zacatecas[1])
print("Longitud:", zacatecas[2])

print("\nAcceso con indices negativos:")
print("Ciudad  :", zacatecas[-3])
print("Latitud :", zacatecas[-2])
print("Longitud:", zacatecas[-1])

print("\nCoordenadas de Guadalupe:")
print("Tipo    :", type(guadalupe))
print("Ciudad  :", guadalupe[0])
print("Latitud :", guadalupe[1])
print("Longitud:", guadalupe[2])

nombre, latitud, longitud = zacatecas
print(f"\n{nombre}: ({latitud}, {longitud})")

nombre, latitud, longitud = guadalupe
print(f"{nombre}: ({latitud}, {longitud})")

for ubicacion in (zacatecas, guadalupe):
    print("\nUbicacion:", ubicacion[0])
    print("Coordenadas:", ubicacion[1:])

# Desempaquetar coordenadas para calcular el punto medio aproximado
_, lat1, lon1 = zacatecas
_, lat2, lon2 = guadalupe
centro = (round((lat1 + lat2) / 2, 2), round((lon1 + lon2) / 2, 2))
print("\nPunto medio aproximado:", centro)

# Crear otra tupla con el codigo de Zacatecas
ampliada = zacatecas + ("ZAC",)
print("Nueva tupla Zacatecas:", ampliada)
print("Original sin cambios:", zacatecas)

# Las tuplas son inmutables; intentar reemplazar un elemento directamente causaria TypeError.
print("'Zacatecas' pertenece a la tupla:", "Zacatecas" in zacatecas)

