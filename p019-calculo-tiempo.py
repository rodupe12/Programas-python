#p019-calculo-tiempo.py
#Diseña un programa que tome una cantidad de horas como un número entero. 
# El programa debe calcular y mostrar el equivalente de ese tiempo en:
# Días (considerando que 1 día tiene 24 horas)
# Minutos (considerando que 1 hora tiene 60 minutos)
# Segundos (considerando que 1 minuto tiene 60 segundos)

print ("\033[2J\033[h", end="")
print ('Combierte una cantidad de horas, en dias, minutos, y segundos \n')

#Entreda 
t=int(input('Ingrese la cantidad de horas a convertir: '))

#Proceso
dias    = t/24
minutos = t*60
segundos    = minutos*60

#Salida

print('\nEl tiempo ingresado en horas es')
print('-'*30)
print(f'Dias {dias:.2f}')
print(f'Minutos {minutos}')
print(f'Segundos {segundos}')
print('-'*30)