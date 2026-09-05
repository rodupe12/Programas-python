#p064-verificar-palindromo.py
#Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. 
#Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).

while True:

    print ("\033[2J\033[h", end="")
    print ('Ingrese un número entero y determinar si es un palíndromo')

    n = input('Introduce un número para verificar si es palíndromo: ? ')
    i = len(n)
    j = 0
    res = False
    while j < i:
        if n[j] == n[i-1]: res = True 
        else: 
            res = False
            break
        i -= 1
        j += 1

    if res == True:
        print(f'El numero {n} es palíndromo')
    else:
        print(f'El numero {n} no es palíndromo')

    if input('\nDesea continuar (S/N) ? ').upper() == 'N' : break
print('\nProceso terminado')