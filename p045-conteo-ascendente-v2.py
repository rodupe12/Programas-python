#p045-conteo-ascendente-v2.py
#Imprimir numeros de 1 a  n usando un while

print ("\033[2J\033[h", end="")
print ('Imprimir numeros de 1 a n usando un while\n')

n = int (input('Hasta donde ? '))
m = int (input('Ingrementos ? '))

c=1
while c <= n:
    print(f'{c} ',end='')
    c += m

print('\nProceso terminado')


