#p009-promedio-de-calificaciones.py
#Calcular el promedio de tres calificaciones ingresadoas por los usuarios

print ("\033[2J\033[h", end="")
print ('Calcular el promedio de tres calificaciones ingresadoas por los usuarios \n')

#Entrada
print("Dame 3 valificaciones separadas por espacio ")
cal1,cal2,cal3 = input().split()
cal1,cal2,cal3 = float(cal1), float(cal2), float(cal3)

#Poceso
suma = cal1 + cal2 + cal3
promedio = suma / 3

#salida 

print()
print (f'Las calificaciones son: {cal1}, {cal2}, {cal3} ')
print(f'La suma es: {suma:.2f}, \ny el promedio es {promedio:.2f}')
