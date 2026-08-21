#p022-resistencia-equivalente-paralelo.py
#Crea un programa que calcule la resistencia total o equivalente de un circuito con cuatro resistencias en paralelo. 
# El programa debe solicitar al usuario que ingrese el valor de cada una de las cuatro resistencias (R1, R2, R3 y R4).
# Luego, debe calcular la resistencia total usando la siguiente fórmula:

print ("\033[2J\033[h", end="")
print ('Calcula la distancia entre dos puntos en un plano carteciano \n')

#Entreda
print ('Ingrese los 4 valores de las resistencias separado por " , " ')
r1,r2,r3,r4 = input().split(',')

r1= float(r1)
r2= float(r2)
r3= float(r3)
r4= float(r4)

#Proceso
resistenciaT = 1/( 1/r1 + 1/r2 + 1/r3 + 1/r4)

#Salida

print(f'La resistencia total es: {resistenciaT:.2f}')
