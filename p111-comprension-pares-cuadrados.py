#p111-comprension-pares-cuadrados.py
# Generar los cuadrados de los números pares entre 1 y n.

#Borrar pantalla
print('\033[2J\033[1;1H')

while True:
    try:
        n = int(input('Introduzca el límite n: '))
    except ValueError:
        print('Entrada inválida. Introduzca un entero no negativo.')
        continue
    if n >= 0:
        break
    print('El límite debe ser un entero no negativo.')

numeros = list(range(1, n + 1))
cuadrados_pares = [numero ** 2 for numero in numeros if numero % 2 == 0]

print('--- Resultados ---')
print(f'Lista original (1 a {n}): {numeros}')
print(f'Cuadrados de números pares: {cuadrados_pares}')
print(f'Suma de cuadrados: {sum(cuadrados_pares)}')

