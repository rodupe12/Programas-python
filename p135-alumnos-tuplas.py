#p135-alumnos-tuplas.py
#
alumnos = (
    ("Ana", "ISC", (9, 10, 9, 8)),
    ("Luis", "ISW", (8, 8, 9, 10)),
    ("Mar", "ISC", (10, 9, 10, 10)),
)

# Mostrar los registros y la cantidad de alumnos
print("Registros de alumnos:", alumnos)
print("Total de alumnos:", len(alumnos))

# Recorrer los alumnos mediante desempaquetado y calcular sus promedios
for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"Nombre: {nombre}, Carrera: {carrera}, Promedio: {promedio:.2f}")

# Crear los pares de nombres y promedios
promedios = tuple((nombre, sum(calificaciones) / len(calificaciones)) for nombre, _, calificaciones in alumnos)
print("Pares (nombre, promedio):", promedios)

# Identificar al alumno con el promedio mas alto
mejor_promedio, nom = max((promedio, nombre) for nombre, promedio in promedios)
print(f"Alumno con mejor promedio: {nom} con {mejor_promedio:.2f}")

# Consultar las calificaciones usando indices y metodos de tupla
for alumno in alumnos:
    nombre = alumno[0]
    calificaciones = alumno[2]
    print(
        f"{nombre} -> Conteo de 10s: {calificaciones.count(10)}, "
        f"Indice de primera calificacion: {calificaciones.index(calificaciones[0])}"
    )

# Ordenar los pares por promedio de menor a mayor
ordenados = tuple((nombre, promedio) for promedio, nombre in sorted((promedio, nombre) for nombre, promedio in promedios))
print("Ordenados por promedio:", ordenados)

# Agregar un alumno creando una tupla nueva, sin cambiar la original
nueva_tupla_alumnos = alumnos + (("Eva", "ISC", (9, 9, 10)),)
print("Tupla original intacta:", alumnos)
print("Nueva tupla con Eva:", nueva_tupla_alumnos)

