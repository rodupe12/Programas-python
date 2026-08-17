#p006-conversor-temperatura.py
# Covertir una temperatura de grados Celcius a grados Farenheit

print ("\033[2J\033[h", end="")
print ('Covertir una temperatura de grados Celcius a grados Farenheit \n')

#f = ( float(input("Grados Celsius")) * 9 / 5.0 ) + 32

c = float(input('Grados Celcius: '))
f = (c * 9 / 5) + 32

print (f'La temperatura de {c} Grados Celcius, en gados Farenheit es: {f}')