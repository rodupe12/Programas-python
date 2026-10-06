##p101-clasificar-temperaturas.py
# Clasifica las tempreraturas en grados centigrados en fria, templada y calida, usando comprecion de listas

print('\033[2J\033[1;1H') #Borrar pantalla
print('Clasifica las tempreraturas en grados centigrados en fria, templada y calida, usando comprecion de listas')

temp = [15, 22, 30, 18, 25, 10, 28, 35, 20]

#Calsificacion de temperatura grados centirados centigrados 

clasificacion = [
                'Fria' if t < 20 else
                'Templada' if 20 <= t < 30 else
                'Calida' for t in temp]

print('Las temperaturas son:', temp)
print('La clasificacion de las temperaturas es:', clasificacion)



