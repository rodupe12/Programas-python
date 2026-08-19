#p011-operadores-asignacion.py
#Ejemplificar el uso de operadores de asignacion

print ("\033[2J\033[h", end="")
print ('Operadores de asignacion en Python \n')

x = int(input('Dame el valor de X: '))


x += 5
print(f'Suma 5 a x : {x}')
x -= 3
print(f'Resta 3 a x : {x}')
x *= 2
print(f'Muliplicar x por 2 : {x}')
x /= 4
print(f'Dividir x entre 4 : {x}')
x %= 3
print(f'Modulo 3 de x : {x}')
x **= 2
print(f'x elevado al cuadrado: {x}')
x //= 2
print(f'Dividir x entre 2 entera: {x}')
