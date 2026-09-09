#p071-suma-promedio-numeros.py
#Calcula la suma y el primedio de n calificaciones

while True:
    print ("\033[2J\033[h", end="")
    print ('Calcula la suma y el primedio de n calificaciones')

    n =int(input('Cuantas calificaciones ? '))
    suma = 0

    strcals=''
    for i in range(1, n+1, 1):
        
        cal = int(input(f'Calificacion {i} :'))
        suma += cal
        strcals = strcals + str(cal) + ' '

    print(f'Los numeros fueron: {strcals}')
    print(f'La suma es.       :  {suma}')
    print(f'El promedio es.   : {suma/n}')

    if input('\nDesea continuar (S/N) ? ').upper() == 'N' : break
print('\n\n Proceso terminado')
