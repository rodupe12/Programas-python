#p050-conteo-numeros.py
# El usuario introduce n numeros parar con 999, se suma y se cuentan

print ("\033[2J\033[h", end="")
print ('El usuario introduce n numeros parar con 999, se suma y se cuentan\n')

c = suma = cp = cn = cz = 0

while True:
    num = int(input('Numero ? '))
    if  num == 999: break
    suma += num # acomulando
    if num > 0:
        cp += 1 #Contando
    elif num < 0:
        cn += 1 #Contando
    else:
        cz += 1 #Contando



print ('\nResumen de los calculos')
print(f'\n Cuantos. : {c}')
print(f'\nSuma.     : {suma}')
print(f'\nPos.      : {cp}')
print(f'\nNeg.      : {cn}')
print(f'\nZer.      : {cz}')

print('\nProceso terminado')