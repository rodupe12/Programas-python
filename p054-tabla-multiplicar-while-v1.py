#p054-tabla-multiplicar-while-v1.py
#Imprime la tabla t de 1 a 10, usando while

while True:

    print ("\033[2J\033[h", end="")
    print ('Imprime la tabla t de 1 a 10, usando while\n')

    t = int(input('Que tabla quieres ? '))
    n = int(input('Hasta donde.      ? '))

    print ('\nImprime la tabla del ' + str(t) )

    c=1
    while c <= n:
        print(f'{c:3} X {t:3} = {c*t}')
        c+=1
    if input('\nDeseas Continuar (S/N) ? ').upper() == 'N' : break

print('\nTerminamos de imprimir las tablas ...')  
    