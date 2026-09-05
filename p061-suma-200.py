#p061-suma-200.py
#Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. 
# Al terminar, mostrar cuántos números se introdujeron y la suma final.

while True:

    print ("\033[2J\033[h", end="")
    print ('Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200\n')
    suma = i = n = 0

    while suma  <= 200:

        print(f'Suma actual: {suma}.  ',end = '')
        n = int(input('Introduce un número: '))
        i += 1
        suma += n

    print('Meta de 200 alcanzada. ')
    print(f'La suma final: {suma}')
    print(f'Total de números introducidos: {i}')

    if input('\nDesea continuar (S/N) ? ').upper() == 'N' : break
print('\nProceso terminado')