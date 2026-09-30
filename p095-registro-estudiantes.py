#p095-registro-estudiantes.py
#Registro de estudiantes para evento
#Se esta organizando un evento y necesitamos registrar a los estudiantes.
#El programa debe permitir al usuario introducir el nombre y la edad de cada persona
#El regrsitro termina cuando se introduce un* como nombre.
#Al final, el sistema debe mostrar dos informes:
#Una lista de todos los asistentes que no son mayores de edad (18 años o mas)
#El nombre y la edad de la persona con mayor edad para entregarle un reconocimiento

print('\033[H\033[J')
nombre = []
edades = []

while True:
    nombre_estudiante = input('Ingrese el nombre del estudiante (o * para terminar): ')
    if nombre_estudiante == '*':
        break
    try:# calidar que la edad sea un numero entero
        edad_estudiante = int(input('Ingrese la edad del estudiante: '))
        if edad_estudiante < 0:
            print('Edad inválida. Por favor, ingrese un número entero positivo.')
            continue #Si la edad es negativa, se solicita nuevamente el nombre y la edad
        nombre.append(nombre_estudiante)
        edades.append(edad_estudiante)
    except ValueError:
        print('Edad inválida. Por favor, ingrese un número entero.')

if nombre_estudiante:
    #filtrar los estudiantes que no son mayores de edad
    for i in range(len(nombre)):
        if edades[i] < 18:
            print(f'El estudiante {nombre[i]} no es mayor de edad con {edades[i]} años.')
    #Encontrar el estudiante con mayor edad
    max_edad = max(edades)
    indice_max_edad = edades.index(max_edad)
    print(f'El estudiante con mayor edad es {nombre[indice_max_edad]} con {max_edad} años.')

