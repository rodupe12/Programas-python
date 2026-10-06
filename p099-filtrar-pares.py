##p099-filtrar-pares.py
# Filtrar los números de pares de una lista de numeros introducidos usando comprecion de listas

print('\033[2J\033[1;1H') #Borrar pantalla
print('Filtrar los números pares de una lista de numeros introducidos usando comprecion de listas')

cant = int(input('Ingrese la cantidad de numeros que desea introducir: '))
numeros = []

#Se introducen los numero en la lista
for i in range(cant):
    num = int(input(f'Ingrese el numero {i + 1}: '))
    numeros.append(num)

#Se filtran los numeros pares usando comprecion de listas
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]

print('los numeros introducidos son:', numeros)
print('los numeros pares son:', pares)
print('los numeros impares son:', impares)
