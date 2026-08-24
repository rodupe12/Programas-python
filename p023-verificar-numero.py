#p023-verificar-numero.py
#Verificar si un numero entero es positivo negativo o cero

print ("\033[2J\033[h", end="")
print ('Verificar si un numero entero es positivo negativo o cero \n')

numero = int(input('Dame un numero entero ? '))

if numero > 0 :
    print('El numero es POSITIVO 👍')
if numero < 0:
    print ('EL numero es NEGATIVO 👎')
if numero == 0:
    print ('El numero es CERO 🤷‍♂️')

print('\nAqui terminan las decisiones')