#p068-conteo-descendente-for-v2.py
#Imprime numeros de 100 a n en decrmentos de m usando for

print ("\033[2J\033[h", end="")
print ('Imprime numeros de 100 a n en decrmentos de m usando for')

n = int(input('Desde donde ? '))
m = int(input('Intervalos  ? '))


for i in range(n, 0 , - 1):
    print(i)

print('\n Proceso terminado')