#p083-rombo-caracter.py
#Solicitar al usuario un número entero impar n que representará la altura y el ancho máximo de un rombo. 
# El programa deberá dibujar el rombo utilizando el carácter que el usuario elija.

print ("\033[2J\033[h", end="")

altura = int(input('Dame un número impar para la altura: ? '))
c = input('¿Qué carácter quieres usar? ')
espacios = caracteres= 0
altura = int((altura + 1)/2)

for i in range(1, altura+1):
    espacios = altura - i
    caracteres = 2 * i - 1
    for e in range(espacios):
        print(' ',end='')
    for j in range (caracteres):
        print(c, end='')
    print()
for i in range(altura-1,0,-1):
    espacios = altura - i
    caracteres = 2 * i - 1
    for e in range(espacios):
        print(' ',end='')
    for j in range (caracteres):
        print(c, end='')
    print()
