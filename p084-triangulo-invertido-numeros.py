#p084-triangulo-invertido-numeros.py
#Solicitar al usuario un número entero n que determinará la altura de un triángulo numérico invertido. 
# El programa debe imprimir n renglones. El primer renglón contendrá los números de 1 a n, 
# el segundo de 1 a n-1, y así sucesivamente hasta que el último renglón contenga solo el número 1.

print ("\033[2J\033[h", end="")

n = int(input('Dame un número? '))

r = n
for i in range(1, n+1):
    for j in range (1, r+1):
        print(j, end='')
    r -= 1
    print()