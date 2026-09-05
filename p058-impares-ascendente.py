#p058-impares-ascendente.py
#Imprimir los números impares y su suma total en un rango ascendente desde 1 hasta un número n que elija el usuario.
while True:

    print ("\033[2J\033[h", end="")
    print ('Imprime los numeros impares y su suma total, de 1 hasta n')

    n = int(input('Introduce el numero limite ? '))

    if n < 1 : continue

    suma = 0
    i = 1
    print('Numeros impares: ',end='')
    while i <= n:
        print(f', {i}',end='')
        suma += i
        i += 2
    print(f'\nLa suma de los impares: {suma}')


    if input('\nDesea continuar (S/N) ? ').upper() == 'N' : break
print('\nProceso terminado')