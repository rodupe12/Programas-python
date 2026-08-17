#p008b-entrada-multiple.py
#Entrada multiple de valores con funcion map

print ("\033[2J\033[h", end="")
print ('Entrada multiple de valores con funcion map \n')

print ('Dame tres numeros separados por un espacio ')

n1, n2, n3 = map(int, input().split('_'))

print("Los valores introducidos son ")
print(n1, n2, n3)