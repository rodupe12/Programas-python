#p025-verificar-suma.py
#Dados 3 numeros enteros, verifica su la suma de los dos primeros es igual al tercero
# 10+20 == 30 (Son iguales) 5+8==5 (So diferentes )

print ("\033[2J\033[h", end="")
print ('Dados 3 numeros enteros, verifica su la suma de los dos primeros es igual al tercero \n')

n1 = int(input('Numero 1 ? '))
n2 = int(input('Numero 2 ? '))
n3 = int(input('Numero 3 ? '))

if n1 + n2 == n3 :
    print(F' {n1} + {n2} = {n3} ✅SON IGUALES')
else:
    print(F' {n1} + {n2} = {n3} ❌SON DIFERENTES')

print('\nFin del programa')


