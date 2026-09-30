#p092-procesar-calificaciones.py
#Procesa n calificaciones entre 1 y 10 en una lista de hasta introducir 999
#Al final muestra: la lista, suma, promedio, la mas alta, la mas baja,
# Cuantos alumnos mayores al promedio
#validar que no se introduscan letras en lugar de numeros.

calificaciones = []
suma = 0
#Borrar la pantalla
print('\033[H\033[J')  # Limpiar la pantalla

while True:
    try:
        calificacion = float(input("Introduce una calificación entre 1 y 10 (o 999 para terminar): "))
        if calificacion == 999:
            break
        elif 1 <= calificacion <= 10:
            calificaciones.append(calificacion)
            suma += calificacion
        else:
            print("Calificación inválida. Debe estar entre 1 y 10.")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número.")


if calificaciones:
    promedio = suma / len(calificaciones)
    calificacion_maxima = max(calificaciones)
    calificacion_minima = min(calificaciones)
    alumnos_mayores_al_promedio = sum(1 for calif in calificaciones if calif > promedio)
    
    print('Resultados:')
    print(f"Lista de calificaciones: {calificaciones}")
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Calificación más alta: {calificacion_maxima}")
    print(f"Calificación más baja: {calificacion_minima}")
    print(f"Alumnos con calificación mayor al promedio: {alumnos_mayores_al_promedio}")
else:
    print("No se introdujeron calificaciones.")
