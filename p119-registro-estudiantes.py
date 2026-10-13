#p119-registro-estudiantes.py
# Crear una lista de diccionarios para representar un registro de estudiantes

estudiantes = [
    {'nombre':'Carlos','edad':45,'carrera':'Ingenieria','promedio':8.5} ,
    {'nombre':'Rocio','edad':35,'carrera':'Medicina','promedio':9.2},
    {'nombre':'Maria','edad':22,'carrera':'Arquitectura','promedio':8.7}
]
#Borrar pantalla de la consola
print('\033[H\033[J')

#Mostrar los datos de cada estudiate en la lista
print(f'\nTodos los studiantes: {estudiantes} - {len(estudiantes)} elementos')

#Captura de datos en un nuevo estudiante, hasta nombre vacio

print('\nCaptura de nuevos estudiantes')
print('-'*60)
while True:
    print(f'Datos Estudiante:')
    datos = {}
    nombre = input('Nombre ? ')
    if nombre!='':
        datos['nombre'] = nombre
        datos['edad'] = int(input('Edad? '))
        datos['carrera'] = input('Carrera ? ')
        datos['promedio'] = float(input('Promedio? '))
        estudiantes.append(datos)
        print('Estudiante {nombre} agrefados correctamente.')
    else: break

print(f'\nGrupo de estudiantes completo:\n{'-'*60}\n{estudiantes} - {len(estudiantes)}')

print('\nDatos en forma de Tabla:')
print('-'*60)
for k in estudiantes[0].keys():
    print(f'{k:<13}', end='')
print('')
for alumno in estudiantes:
    for v in alumno.values():
        print(f'{v:<13}', end='')
    print('')

#Mostrar los datos en forma de registro
print('\nDatos en forma de Registro y Cálculo de Promedios:')
print('-'*60)

for est in estudiantes:
    for k,v in est.items():
        print(f'{k:<10} : {v}')
    print()

# Calcular la suma y el promedio de los promedios de los estudiantes 
suma_promedio = sum(estudiantes['promedio'] for estudiantes in estudiantes)
promedio_general = suma_promedio / len(estudiantes)
print(f'\nLa suma de los prmedios: {suma_promedio}')
print(f'El promedio general de los estudiantes: {promedio_general:.2f}')



