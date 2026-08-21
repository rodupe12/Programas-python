#p017-convertir-temperatura.py
#Desarrolla un programa que convierta una temperatura de grados Celsius a grados Fahrenheit. 
# El programa debe solicitar al usuario una temperatura en Celsius y luego mostrar el resultado en Fahrenheit. 
# La fórmula para la conversión es: farenheit = (celcius × 9/5) + 32

print ("\033[2J\033[h", end="")
print ('Convierte la temperatura de grados Celsius a grados Fahrenheit \n')

#Entreda 
temCel=float(input('Ingrese la temperatura en grados celsius: '))

#Proceso
temFar = (temCel * (9/5)) + 32

#Salida

print(f'El valor de la temperatura en grados farenheit es: {temFar}')