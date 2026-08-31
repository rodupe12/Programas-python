#p051-adivina-numero.py
# Permite adivinar un numero generado al azar enrte 1 y 50

import random

print ("\033[2J\033[h", end="")
print ('Permite adivinar un numero generado al azar enrte 1 y 50\n')
print('He pensado un numero enrte 1 y 50, adivna cual es ')

ns = random.randint(1,50)

while True:
    intento = int(input('Cual es ? '))
    ci += 1
    if intento < ns :
        print('Demasiado bajo intenta con un numero mas alto')
    elif intento > ns:
        print('Demasiado alto intenta con un numero mas bajo')
    else:
        print(f'Felicidades adivinaste el numero en {ci} intentos')
        print(f'El numero era : ', ns)
        break

print('\nProseso terminado')

