#p113-calificaciones-estudiante.py
#Procesar calificaciones de un estudiante con un diccionario

#Borrar la pantalla
print("\033[H\033[J")

#Crear dos listas, una de materias y otra de calificaciones
materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
calificaciones = [8.5, 9.0, 7.5, 6.0, 8.0]

#Crear un diccionario para almacenar las materias y calificaciones
calificaciones_estudiante = dict(zip(materias, calificaciones))

#Mostrar las calificaciones del estudiante
print(f"Calificaciones del estudiante: {calificaciones_estudiante} --- {len(calificaciones_estudiante)} elementos \n")

# Agregar dos nuevas calificaciones al diccionario
calificaciones_estudiante['Educación Física'] = 9.5
calificaciones_estudiante['Arte'] = 8.0

#Actualizar la calificación de tres materias
calificaciones_estudiante['Matemáticas'] = 9.0
calificaciones_estudiante['Física'] = 9.5
calificaciones_estudiante['Historia'] = 7.0

print(f"Calificaciones del estudiante actualizadas: {calificaciones_estudiante} --- {len(calificaciones_estudiante)} elementos \n")

#elimincar 2 calificaciones del diccionario usando pop
calificaciones_estudiante.pop('Química')
calificaciones_estudiante.pop('Lengua')
print(f"Calificaciones del estudiante eliminadas: {calificaciones_estudiante} --- {len(calificaciones_estudiante)} elementos \n")

#mostrar el par llave-valor de las calificaciones del estudiante, y promedir las caficaciones
print('Las calificaciones del estudiante son:')
total = 0
for materia, calificacion in calificaciones_estudiante.items():
    print(f' - {materia} : {calificacion}')
    total += calificacion
promedio = total / len(calificaciones_estudiante)
print(f'\nEl promedio de las calificaciones del estudiante es: {promedio:.2f}')

