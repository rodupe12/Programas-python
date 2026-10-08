#p106-mes-día-nombre.py
# Leer un número de mes y mostrar su nombre y la cantidad de días que tiene.

#Borrar pantalla
print('\033[2J\033[1;1H')

meses = [
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
]
dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    try:
        numero_mes = int(input('Introduzca un número de mes (1-12): '))
    except ValueError:
        print('Entrada inválida. Introduzca un número entero del 1 al 12.')
        continue

    if 1 <= numero_mes <= 12:
        break
    print('El número de mes debe estar entre 1 y 12.')

indice = numero_mes - 1

print('--- Resultados ---')
print(f'Mes: {meses[indice]}')
print(f'Días: {dias_mes[indice]}')

