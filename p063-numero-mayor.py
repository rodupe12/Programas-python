#p063-numero-mayor.py
#Leer una serie de números hasta que el usuario ingrese un 0. 
# Al terminar, el programa deberá mostrar cuál fue el número más grande de todos los introducidos.


while True:

    print ("\033[2J\033[h", end="")
    print ('Lee los numeros de usuario asta ingresar 0 y muetra el conteo, muestra cuál fue el número más grande')

    print('Introduce números (0 para terminar): ')

    n = 1
    mayor = 0
    while n != 0:
        n = int(input('> '))
        if mayor < n : mayor = n  

    print('-'*30)
    print(f'El numero mayor fue: {mayor}')


    if input('\nDesea continuar (S/N) ? ').upper() == 'N' : break
print('\nProceso terminado')