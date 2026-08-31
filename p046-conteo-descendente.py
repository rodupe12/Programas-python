#p046-conteo-descendente.py
#Imprimir numeros de 100 a 1 usando un while

print ("\033[2J\033[h", end="")
print ('Imprimir numeros de 100 a 1 usando un while\n')

c=100
while c >= 1:
    print(f'{c} ',end='')
    c -= 1

print('\nProceso terminado')

