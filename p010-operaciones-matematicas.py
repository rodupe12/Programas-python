#p010-operaciones-matematicas.py
#Demostrar el uso de los operadores aritmeticos 

print ("\033[2J\033[h", end="")
print('-' * 50)
print ('Calculadora de Operaciones aritmeticas \n')
print('-' * 50)

x = float(input('Valor de x : '))
y = float(input('Valor de y : '))

suma = x + y
resta = x - y
multi = x * y
divi = x / y
modu = x % y
pot = x ** y
dive = x // y


print('Resultado de las operaciones realizadas\n')

print(f'Numero: {x} , {y} ')
print(f'Suma:  {suma:>20.2f}')
print(f'Resta: {resta:>20.2f}')
print(f'Multi: {multi:>20.2f}')
print(f'Divi:  {divi:>20.2f}')
print(f'Mod:   {modu:>20,.2f}')
print(f'Dive:  {dive:>20.2f}')

print('=' * 50)


