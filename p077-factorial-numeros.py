#p077-factorial-numeros.py
#Calcular el factorial de n numeros

print ("\033[2J\033[h", end="")
print ('Calcular el factorial de n numeros')
try:
    n = int(input('Hasta que numero ? '))


    for x in range(1, n+1):

        print(f'{n}! = ', end = '')
        f = 1
        for i in range(1, x+1):
            #print (f'{i} x ', end='')
            print(f"{i}{' x ' if i < x else ' '}", end='')
            f = f * i

        print(f'= {f:,}')
except ValueError:
    print('Solo se aceptan numeros enteros')



