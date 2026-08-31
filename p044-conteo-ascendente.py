#p044-conteo-ascendente.py
#Imprimir numeros de 1 a 100 usando un while

print ("\033[2J\033[h", end="")
print ('Imprimir numeros de 1 a 100 usando un while\n')

c=1
while c <= 100:
    print(f'{c} ',end='')
    c += 1

print('\nProceso terminado')


