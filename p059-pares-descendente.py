#p059-pares-descendente.py
#Imprimir los números pares y su suma total en un rango descendente desde 100 hasta un número n que elija el usuario.

while True:

    print ("\033[2J\033[h", end="")
    print ('Imprime los numeros pares decendentes, de 100 asta el numero que elija el usuario')

    n = int(input('Introduce un número límite (menor a 100) ? '))

    if n >= 100 : continue

    suma = 0
    i = 100
    print('Numeros pares: ',end='')

    while i >= n:
        print(f', {i}',end='')
        suma += i
        i -= 2
    print(f'\nLa suma de los impares: {suma}')


    if input('\nDesea continuar (S/N) ? ').upper() == 'N' : break
print('\nProceso terminado')