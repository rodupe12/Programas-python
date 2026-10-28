#p133-alumnos-tuplas.py
#Registron de alumnos una tupla de tuplas


#Creamos una tupla donde cada elemento es otra tupla que contiene los datos
# de cada estudiante

alumnos = (
    ('Ana','ISC',(9,10,9)),
    ('Luis','ITC',(8,9,10)),
    ('María','ISD',(10,8,9))
)

#Imprime el total de alumnos
print('Registro de alumnos: ')
print('Total de alumnos: ', len(alumnos))

#Imprime sobre las tuplas de alumos y calcula el promedio de calificaciones
for nombre, carrera, calificaciones in alumnos:
    promedio = sum(calificaciones) / len (calificaciones)
    print(f'{nombre} - {carrera} - {calificaciones} : {promedio:.2f}')

#Imprime los datos del primer alumno usando undices
primero_alumno = alumnos[0]
print('\nDatos del primer alumno: ')
print('Nombre: ', primero_alumno[0])
print('Carrera: ', primero_alumno[1])
print('Calificaciones: ', primero_alumno[2])

#Creamos la tupla de promedio usando comprecion de tuplas
promedio = tuple (
    (nombre, sum(notas) / len (notas)) for nombre, _, notas in alumnos
)

print('\nPromedio de los alumnos:', promedio)

#crear tupla con los nombres de los alumnos
#Usando comprecion de tuplas
nombre = tuple(nombre for nombre, _, _ in alumnos)
print('\nNombre de los alumnos',nombre)