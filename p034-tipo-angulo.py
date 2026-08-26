#p034-tipo-angulo.py
#Dado un angulo en el rango de 0 a 360 identificar que tipo de angulo es

print ("\033[2J\033[h", end="")
print ('Dado un angulo en el rango de 0 a 360 identificar que tipo de angulo es \n')

ang = int(input('Angulo ? '))

if ang >= 0 and ang <= 360:
    print('Tu angulo es: ' , end='')
    if ang < 90: 
        print('AGUDO')
    elif ang == 90: 
        print('RECTO')
    elif ang > 90 and ang<180: 
        print('OBTUSO')
    elif ang == 180: 
        print('LLANO')
    elif ang > 180 and ang < 360 : 
        print('CONCAVO')
    elif ang == 360: 
        print('CERRADO')
else:
    print('Angulo fuera de rango')

print('Proceso terminado')