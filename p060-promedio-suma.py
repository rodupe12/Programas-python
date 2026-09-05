#p060-promedio-suma.py
#Leer números introducidos por el usuario hasta que ingrese un 0. Al finalizar,
#  mostrar el conteo total de números, la suma y el promedio de la serie.

while True:

    print ("\033[2J\033[h", end="")
    print ('Lee los numeros de usuario, asta ingresar 0 y muetra el conteo, la suma y el promedio')

    print('Introduce números (0 para terminar): ')
    n = 1
    suma = i = prom = 0
    while n != 0:
        n = int(input('> '))
        i += 1
        suma += n

    prom = (suma) / (i -1)    
    print(f'Se introdujeron {i - 1} números')
    print(f'La suma es: {suma}')
    print(f'El promedio es: {prom}')


    if input('\nDesea continuar (S/N) ? ').upper() == 'N' : break
print('\nProceso terminado')