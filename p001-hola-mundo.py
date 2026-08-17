#p001-hola-mundo.py
#Descripcion
#
print('Leyendo datos y enviando saludos' )

#Borrar la pantalla de la terminal
print ("\033[2J\033[h", end="")

#Leer datos
nombre = input('Dame tu Nombro? ')
edad = int(input('Dame la edad? '))
peso = float(input('Dame el peso? '))

print(f'{nombre} Bienvenido a python, tu edad {edad}, tu peso es {peso}kg')

print()