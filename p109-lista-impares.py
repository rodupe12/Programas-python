#p109-lista-impares.py
# Leer un entero n. Llenar una lista con los primeros n números impares.

#Borrar pantalla
print('\033[2J\033[1;1H')

while True:
    try:
        n = int(input('Introduzca la cantidad de números impares (n): '))
    except ValueError:
        print('Entrada inválida. Introduzca un entero no negativo.')
        continue
    if n >= 0:
        break
    print('La cantidad debe ser un entero no negativo.')

impares = [2 * i + 1 for i in range(n)]
print('--- Generación de Lista ---')
print(f'Lista de los primeros {n} números impares: {impares}')

print('--- Cálculos ---')
suma = sum(impares)
promedio = suma / n if n else 0
print(f'Suma de los números: {suma}')
print(f'Promedio de los números: {promedio}')

divisibles_por_tres = [numero for numero in impares if numero % 3 == 0]
print('--- Divisibles entre 3 ---')
print(f'Números divisibles entre 3: {divisibles_por_tres}')
print(f'Suma de los números divisibles entre 3: {sum(divisibles_por_tres)}')

while True:
    try:
        buscado = int(input('Introduzca elemento a buscar: '))
        break
    except ValueError:
        print('Entrada inválida. Introduzca un número entero.')

print('--- Búsqueda ---')
if buscado in impares:
    print(f'Result: El elemento {buscado} está en la lista en la posición (índice) {impares.index(buscado)}.')
else:
    print(f'Result: El elemento {buscado} no está en la lista.')
