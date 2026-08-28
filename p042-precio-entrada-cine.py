#p042-precio-entrada-cine.py
#Crea un programa para la taquilla de un cine que determine el precio de una entrada según la edad del cliente. 
# El programa debe solicitar la edad y mostrar el precio correspondiente, siguiendo estas reglas: 
# Menores de 5 años: Entran gratis.
# Niños (5 a 12 años): Pagan $5.
# Adultos (13 a 64 años): Pagan $10.
# Tercera edad (65 años o más): Pagan $7.

print ("\033[2J\033[h", end="")
print ('Determina el precio de los boletos del cine apartir de la edad\n')

edad  = int(input('Edad del cliente : '))


if edad < 5: 
    print('Entrada gratis')
elif edad >= 5 and edad <= 12: 
    print('El precio de la entrada es $5. ')
elif edad >= 13 and edad < 65: 
    print('El precio de la entrada es $10. ')
elif edad > 65: 
    print('El precio de la entrada es $7. ')

print('\nProceso terminado')