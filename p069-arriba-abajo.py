#p069-arriba-abajo.py
#Imprime numeros de 1 a n o de n a 1 segun lo decidas

print ("\033[2J\033[h", end="")
print ('Imprime numeros de 1 a n o de n a 1 segun lo decidas')

print('[ 1 ] voy de 1 a n ')
print('[ 2 ] voy de n a 1 ')
op = int(input('Elige ? '))

if op == 1:
    print('\nVamos hacia arriba de 1 a n')
    n = int(input('Hasta donde ? '))
    for x in range(1, n+1, 1):
        print(f'{x} ', end='')
elif op == 2:
    print('\nVamos hacia arriba de 1 a n')
    n = int(input('Desde donde ? '))
    for x in range(n, 0, -1):
        print(f'{x} ', end='')
else:
    print('\n\nOpcion Erronea')

print('\n\n Proceso terminado')

