#p035-tipo-triangulo.py
#Clasificar un triangulo segun la longitud de sus lados

print ("\033[2J\033[h", end="")
print ('Clasificar un triangulo segun la longitud de sus lados\n')

lado_a = float(input('Longitud del lado a : '))
lado_b = float(input('Longitud del lado b : '))
lado_c = float(input('Longitud del lado c : '))

if lado_a == lado_b and lado_b == lado_c:
    print(f'\n Es un traingulo EQUILATERO , todos sus lados son iguales')
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print(f'\n Es un triangulo ISOCELES , al menos dos lados iguales')
else:
    print(f'\n Es un traingulo ESCALENO , todos sus lados son diferentes')

print('\nProceso terminado')


