#p112-datos-estudiante.py
# Gestion de datos de un estudiante con un diccionario

#Borrar la pantalla
print("\033[H\033[J")

#crear un diccionario para almacenar los datos del estudiante
estudiante = {
    'nombre': 'Juan Pérez',
    'edad': 20,
    'carrera': 'Ingeniería de Sistemas',
    'email': 'juan.perez@universidad.com'
}
print(f"Datos del estudiante: {estudiante} --- {len(estudiante)} elementos \n")

#Modificar un dato del estudiante
estudiante['edad'] = 21
estudiante['email'] = 'juanito@universidad.com'
print(f"Datos del estudiante actualizados: {estudiante} --- {len(estudiante)} elementos \n")

#agregar un nuevo dato al estudiante
estudiante['promedio'] = 8.5
print(f"Datos del estudiante con promedio agregado: {estudiante} --- {len(estudiante)} elementos \n")

#mostrar las llaves del diccionario
print('Las llaves de son:')
for key in estudiante.keys():
    print(f' - {key}')

#mostrar los valores del diccionario
print('\nLos valores son:')
for value in estudiante.values():
    print(f' - {value}')

# Mostrar las llaves y valores del diccionario
print('las llaves y valores del diccionario son:')
for key, value in estudiante.items():
    print(f' - {key} : {value}')
