#p037-numero-mayor.py
#Escribe un programa que reciba tres números enteros e identifique y muestre cuál de ellos es el mayor.

print ("\033[2J\033[h", end="")
print ('El programa detecta cual es el numero mas grande de tres digitos\n')


n1,n2,n3 = map(int, input('Dame 3 numeros separados por (ESPACIO): ').split())

if (n1 > n2):
    num_mayor = n1
elif (n2 > n3):
    num_mayor = n2
else:
    num_mayor = n3

print(f'El numero mayor es {num_mayor}')







