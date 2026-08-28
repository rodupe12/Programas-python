#p039-numeros-romanos.py
#Escribe un programa que pida al usuario un número entero entre 1 y 10 y muestre su equivalente en números romanos. 
# Si el número está fuera de este rango, debe mostrar un mensaje de error.

print ("\033[2J\033[h", end="")
print ('Apartir de un numero del 1 a 10, devuelve su numero equivalente en numero romano\n')

num = int(input('ingresa un numero del 1 al 10 : '))

if (num == 1):
    print(f'El numero {num} en numero romano es I ')
elif (num == 2):
    print(f'El numero {num} en numero romano es II ')
elif (num == 3):
    print(f'El numero {num} en numero romano es III ')
elif (num == 4):
    print(f'El numero {num} en numero romano es IV ')
elif (num == 5):
    print(f'El numero {num} en numero romano es V ')
elif (num == 6):
    print(f'El numero {num} en numero romano es VI ')
elif (num == 7):
    print(f'El numero {num} en numero romano es VII ')
elif (num == 8):
    print(f'El numero {num} en numero romano es VIII ')
elif (num == 9):
    print(f'El numero {num} en numero romano es IX ')
elif (num == 10):
    print(f'El numero {num} en numero romano es X ')
else:
    print(f'El numero que ingresaste esta fuera de rango')