#p066-conteo-ascendente-for-v2.py
# Numero de 1 a n en intervalos de m usando for

print ("\033[2J\033[h", end="")
print ('Numero de 1 a n en intervalos de m usando for')

n = int(input('Hasta donde ? '))
m = int(input('Intervalos ? '))

for i in range(1, n+1, m):
    print(i)

print('\nProceso terminado')