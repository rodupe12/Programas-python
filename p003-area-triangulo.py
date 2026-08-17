#p003-area-triangulo.py
#Calcula el área de un traingulo

print ("\033[2J\033[h", end="")

print('Calculando el área de un triángulo \n')

print('Dame la Base y la Altura del triangulo separados por <ENTER>')
base,altura = int(input()), int(input())
area = (base*altura)/2

print(f'El Area del traingulo es: {area}')