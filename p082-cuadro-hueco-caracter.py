#p082-cuadro-hueco-caracter.py
#El programa debe solicitar al usuario que ingrese el tamaño del lado de un cuadrado y el carácter con el que se dibujará. 
# Luego, deberá imprimir en la consola un "cuadrado hueco", donde el carácter solo se utilice para dibujar el contorno del mismo.

l = int(input('De que tamño será el lado del cuadrado? '))
c = input('Qué caracter quieres usar ? ')
espacios = l-2

for i in range (1,l+1):
    print(c, end='')
print()    
for i in range (1,l):
    
    print(c, end='')
    for i in range (espacios):
        print(' ', end='')
    print(c, end='')
    print()

for i in range (1,l+1):
    print(c, end='')
    print 

    
    