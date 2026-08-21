#p020-numero-suerte.py
#Escribe un programa que solicite al usuario su año de nacimiento como un número entero de cuatro dígitos. 
# A partir de este dato, el programa debe:
# Mostrar cada uno de los dígitos individuales del año. Por ejemplo, si el año es 1995, debe mostrar "1", "9", "9", "5".
# Calcular y mostrar la suma de los dígitos individuales del año. Siguiendo el ejemplo anterior, la suma sería 1 + 9 + 9 + 5 = 24.

print ("\033[2J\033[h", end="")
print ('Suma los numeros individuales del año de nacimiento \n')

#Entreda 
año=int(input('Ingrese su año de nacimiento: '))

#Proceso
d1 = int(año/1000)
d2 = int((año%1000) / 100)
d3 = int((año%100) / 10)
d4 = int(año%10)
suma = d1 + d2 + d3 + d4

#Salida

print(f'Los valores de tu año de nacimiento son "{d1}", "{d2}", "{d3}", "{d4}"')
print(f'\nLa suma de los valores {d1} + {d2} + {d3} + {d4} = {suma}')
