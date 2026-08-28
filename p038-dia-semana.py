#p038-dia-semana.py
#Escribe un programa que solicite un número entero del 1 al 7 y muestre el día de la semana correspondiente, 
# considerando que 1 es domingo y 7 es sábado. Si el número ingresado está fuera de ese rango,
# debe mostrar un mensaje de error.

print ("\033[2J\033[h", end="")
print ('El programa devuelve un dia de la semana dependiendo del numero que ingrese \n')

num = int(input('Dame un numero del 1 al 7 : '))

if (num == 1):
    print('El dia es Lunes')
elif (num == 2):
    print('El dia es Martes')
elif (num == 3):
    print('El dia es Miercoles')
elif (num == 4):
    print('El dia es Jueves')
elif (num == 5):
    print('El dia es Viernes')
elif (num == 6):
    print('El dia es Sábado')
elif (num == 7):
    print('El dia es Domingo')
else:
    print(f'El numero {num} esta fuera de rango')