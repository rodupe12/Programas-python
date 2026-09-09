#p070-suma-pares-impares.py
#Imprime numeros pares o impares de 1 a n segun decidas

print ("\033[2J\033[h", end="")
print ('Imprime numeros pares o impares de 1 a n segun decidas')

print('[ 1 ] voy de 1 a n con pares')
print('[ 2 ] voy de 1 a n con impares')
op = int(input('Elige ? '))
suma = 0

if op == 1:
    print('\nVoy de 1 a n con pares')
    n = int(input('Hasta donde ? '))
    for x in range(2, n+1, 2):
        print(f'{x} ', end='')
        suma = suma + x 
        print('Suma = ' + str(x))
elif op == 2:
    print('\nVoy de 1 a n con impares')
    n = int(input('Hasta donde ? '))
    for x in range(1, n+1, 2):
        print(f'{x} ', end='')
        suma = suma + x 
        print('Suma = ' + str(x))    
else:
    print('\n\nOperacion Erronea')

print('\n\n Proceso terminado')