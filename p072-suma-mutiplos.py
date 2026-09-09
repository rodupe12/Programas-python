#p072-suma-mutiplos.py
#Imprime numeros de 1 a n, solo los multiplos de m


print ("\033[2J\033[h", end="")
print ('Imprime numeros de 1 a n, solo los multiplos de m')

m = int (input('Que multiplos quieres ? '))
n = int (input('Iniciamos en 1 hasta donde ? '))

c= s = 0
for i in range(1, n+1):
    if i % m == 0:
        print(f'{i} ', end='')
        c += 1
        s += i

print(f'\nCunatos multiplos fueron {c} ')
print(f'Suma de los multiplos de {m} = {s}')