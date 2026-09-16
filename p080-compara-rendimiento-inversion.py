##p080-compara-rendimiento-inversion.py
#Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años.  
# El usuario debe ingresar el monto inicial y la tasa de interés anual (porcentaje) para cada uno de los dos fondos, 
# así como el número de años a proyectar. El programa deberá mostrar una tabla comparativa anual y al final
# indicar qué fondo generó un mayor rendimiento.

print ("\033[2J\033[h", end="")

print('--- Fondo de Inversión A ---')
miA = int(input('Monto inicial: '))
tiaA = float(input('Tasa de interés anual (%): '))

print('\n--- Fondo de Inversión B ---')
miB = int(input('Monto inicial: '))
tiaB = float(input('Tasa de interés anual (%): '))

an = int(input('\nAños a proyectar: '))

print('--- Comparación de Rendimientos Anuales ---')
print('Años |   Fondo A         |   Fondo B')
print('-'*45)
mactA = miA
mactB = miB
for i in range(1,an+1):
    mactA = mactA + (mactA*(tiaA/100))
    mactB = mactB + (mactB*(tiaB/100))
    print(f' {i} |   $       {mactA:.2f} | $     {mactB:.2f}')

print('Resultado final: ')
if (mactA > mactB):
    print(f'El Fondo A ($ {mactA:.2f}) superó al Fondo B ($ {mactB:.2f})')
elif(mactA < mactB):
    print(f'El Fondo B ($ {mactB:.2f}) superó al Fondo A ($ {mactA:.2f})')
else:
    print(f'El Fondo A ($ {mactA:.2f}) es igual al Fondo B ($ {mactB:.2f})')