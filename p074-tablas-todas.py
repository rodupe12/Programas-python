#p074-tablas-todas.py
#Imprime las tablas de multiplicar de 1 a 10, del 1 al 10

print ("\033[2J\033[h", end="")
print ('Imprime las tablas de multiplicar de 1 a 10, del 1 al 10)')

t = int(input('Hasta que tabla ?           ... '))
n = int(input('Hasta que numero la tabla ? ... '))

for i in range (1, t + 1):
    print('')
    print(f'Tabla del {i}')

    for j in range(1, n+1):
        print(f'{i} x {j} = {i*j}')

    print()
print('Proceso terminado')


