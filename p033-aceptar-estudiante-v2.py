#p033-aceptar-estudiante-v2.py
#Aceptar estudiantes en base a edad y calificaciones (Utilizando AND)
#Las condiciones edad >= 18 y c1 y c2 >= 2

print ("\033[2J\033[h", end="")
print ('Aceptar estudiantes en base a edad y calificaciones (Utilizando AND) \n')

nombre = input('Dame tu nombre ? ')
edad = int(input('Dame tu edad ? '))

if edad >= 18:
    print(f'\n{nombre}, Continuamos con el proceso ..')
    print('Dame tus 2 calificaciones separadas por ENTERs ? ')
    c1 = float(input())
    c2 = float(input())
    if c1 >= 8 and c2 >= 8:
        print(f'{nombre} Bienvenido a la universidad ') 
    else:
        print(f'\n{nombre} , No aceptamos calificaciones menores a 8..')
else:
    print(f'\n{nombre}, no aceptamos menores de edad.. ')

print('\nProceso terminado')