#p031-2da-ley-de-newton.py
#Calcular los valores de la 2da ley de newton

print ("\033[2J\033[h", end="")
print ('Calcular los valores de la 2da ley de newton \n')

print(f'[ F ] Fuerza ( f = m * a ) ')
print(f'[ M ] Fuerza ( m = f / a ) ')
print(f'[ A ] Fuerza ( f = f / m ) ')
print('Elige ? ')
op = input().upper()

if op == 'F':
    print('\nCalculando la Fuerza')
    m = float(input('Dame la masa        ? '))
    a = float(input('Dame la aceleracion ? '))
    f = m * a
    print(f'\nLa Fuerza es {f} ')    
elif op == 'M':
    print('\nCalculando la Masa')
    f = float(input('Dame la Fuerza       ?' ))
    a = float(input('Dame la aceleracion  ?' ))
    m = f / a
    print(f'\nLa Masa es {m} ')
elif op == 'A':
    print('\nCalculando la Aceleracion')
    f = float(input('Dame la Fuerza      ?' ))
    m = float(input('Dame la Masa        ?' ))
    a = f / m
    print(f'\nLa Aceleracion es {a} ')
else:
    print('Ingrese una operacion correcto')
    



