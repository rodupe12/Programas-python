#p008-entrada-con-espacio.py
#Leer datos multiples separados por un espacio u otro caracter

print ("\033[2J\033[h", end="")
print ('Leer datos multiples separados por un espacio u otro caracter \n')

print ('Dame tres numeros separados por un espacio ')

n1,n2,n3 = input().split()

n1,n2,n3 = int(n1), int(n2), int(n3)

print('Los valores introducidos son ')
print(n1,n2,n3)