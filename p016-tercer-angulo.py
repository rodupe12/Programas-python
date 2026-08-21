#p016-tercer-angulo.py
#Escribe un programa que determine el tercer ángulo de un triángulo. 
# El programa debe pedir al usuario que ingrese las medidas de dos ángulos del triángulo. 
# Utiliza la siguiente fórmula para encontrar el ángulo faltante: angulo3 = 180 – (angulo1 + angulo2)

#Rodrigo D

print ("\033[2J\033[h", end="")
print ('Calcula el angulo faltante de un traingulo, con los otros dos ángulos \n')

#Entreda 

print ('Ingrese los valores de los ángulos del traingulo separado por "espacio"')
an1,an2 = input().split()
an1= float(an1)
an2= float(an2)
#Proceso
an3 = 180 - (an1 + an2)

#Salida

print(f'El angulo faltante del triángulo es {an3}')