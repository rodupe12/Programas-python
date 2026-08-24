#p024-verificar-numero-v2.py
#Verificar si un numero entero es positivo negativo o cero V2

print ("\033[2J\033[h", end="")
print ('Verificar si un numero entero es positivo negativo o cero \n')

numero = int(input('Dame un numero entero ? '))

if numero > 0 :
    print('El numero es POSITIVO 👍')
else: 
    if numero < 0:
        print ('EL numero es NEGATIVO 👎')
    else: 
        if numero == 0:
            print ('El numero es CERO 🤷‍♂️')

print('\nAqui terminan las decisiones')
