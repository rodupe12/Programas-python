#p075-triangulo-caracter.py
#Dibuja un cuadrado del caracter deseado


print ("\033[2J\033[h", end="")
print ('Dibuja un cuadrado del caracter deseado')

r = int(input('De cuantos por cuatos r x r ? '))
c = input('Caracter ? ')

for i in range(1, r+1):
    for j in range (1, i+1):
        print('*', end='')
    print()
