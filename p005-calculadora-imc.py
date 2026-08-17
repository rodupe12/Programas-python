#p005-calculadora-imc.py
#Calcular el indice de masa corporal

print ("\033[2J\033[h", end="")
print ('Calcular el indice de masa corporal IMC \n')

peso_kg = float(input('Ingresa tu peso en Kilogramos? '))
altura_m = float(input('Ingresa tu altura en metros? '))

imc = peso_kg / (altura_m ** 2)

print(f'Tu IMC es: {imc:.2f}')
