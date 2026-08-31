#p047-conteo-descendente-v2.py
##Imprimir numeros de 100 a  n usando un while

print ("\033[2J\033[h", end="")
print ('Imprimir numeros de n a 1 usando un while\n')

n = int (input(' Desde donde ? '))
m = int (input('Decrementos  ? '))

c= n
while c >= n:
    print(f'{c} ',end='')
    c -= m

print('\nProceso terminado')


