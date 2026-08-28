#p040-calculo-notas.py
#Escribe un programa que calcule el promedio de 5 calificaciones ingresadas por el usuario. 
# Basado en el promedio, el programa deberá mostrar uno de los siguientes mensajes:
# Menor a 6: "Quedas reprobado"
# Desde 6 hasta menos de 7: "Pasas de panzazo"
# Desde 7 hasta menos de 8: "Muy bien, puedes mejorar"
# Desde 8 hasta menos de 9: "Excelente, sigue así" 
# Desde 9 hasta 10: "Perfecto, tu esfuerzo valió la pena

print ("\033[2J\033[h", end="")
print ('A partir de 5 calificaciones el programa devuelve un mensaje dependiendo del promedio de las calificaciones\n')

c1, c2, c3, c4, c5 = map(int, input('Ingresa 5 calificaciones separdas por (ESPACIO): ').split())

prom = (c1 + c2 + c3 + c4 + c5) / 5


if prom >= 0 and prom <= 10:
    print(f'El promedio: {prom}')
    if prom < 6: 
        print('Quedas reprobado')
    elif prom >= 6 and prom < 7: 
        print('Pasas de panzazo')
    elif prom >= 7 and prom < 8: 
        print('Muy bien, puedes mejorar')
    elif prom >= 8 and prom < 9: 
        print('Excelente, sigue así')
    elif prom >= 9 and prom < 10:
        print('Perfecto, tu esfuerzo valió la pena')
else:
    print('Alguna calificación fuera de rango')