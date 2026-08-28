#p041-aceptar-estudiante-v2.py
#La "Universidad Kitty Kat SA" solo acepta estudiantes que cumplan con los siguientes requisitos: 
# ser mujer, ser mayor de 21 años y tener un promedio entre 8 y 9.5. 
# Escribe un programa que solicite el nombre, sexo (h/m), edad y tres calificaciones de un aspirante. El programa 
# debe evaluar los datos y mostrar un mensaje claro que indique si el estudiante fue aceptado. Si no es aceptado, el 
# mensaje debe especificar la razón del rechazo (ya sea por no cumplir con el sexo, la edad o el promedio requerido).

print ("\033[2J\033[h", end="")
print ('Apartir de algunos parametro de elige a un estudiante dentro de una universidad\n')

nombre = input('Dame tu nombre ? ')
sex = input('Sexo (h/m) : ').upper()
edad = int(input('Edad : '))
c1,c2,c3 = map(float, input('Ingrese sus calificaciones sepada por (espacio): ').split())

prom = (c1 + c2 + c3) / 3

if sex == 'M':
    if edad > 21:
        if prom >= 8 and prom <= 9.5:
            print(f'Estudiante {nombre} aceptado')
        else:
            print('El estudiante no cumple con el promedio requerido ')
    else:
        print('El estudiante no cumple con la edad suficiente para ingresar ')
elif sex == 'H':
    print('Solo se aceptan estudiantes mujeres')
else:
    print('El sexo no esta bien ingresado')

print('\nProceso terminado')
