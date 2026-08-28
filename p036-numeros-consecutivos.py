#p036-numeros-consecutivos.py
#Escribe un programa que reciba tres números enteros y determine si son consecutivos. 
# Si lo son, muestra un mensaje de confirmación; de lo contrario, informa que no lo son.

print ("\033[2J\033[h", end="")
print ('Identifica si tres numeros son consecutivos\n')

n1,n2,n3 = input('Dame 3 numeros separados por (ESPACIO): ').split()
n1,n2,n3 = int(n1), int(n2), int(n3)

if (n1 < n2 and n2 < n3):
    if ((n1 + 1) == n2  and (n2 + 1) == n3):
        print(f'Los numeros {n1} , {n2} , {n3} son consecutivos. ')
    else:
        print(f'El numero {n1} < {n2} < {n3} pero no son consecutivos. ')
else:
    print(f'El numero {n1}, {n2}, {n3}, los numeros no son consecutivos. ')