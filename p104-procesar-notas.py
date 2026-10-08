#p104-procesar-notas.py
#Leer un nuimero indeterminado de notas entre 0 y 100

#Borrar pantalla
print('\033[2J\033[1;1H')

calif=[]
while True:
    nota=int(input('Introduzca nota (0 para detener): '))
    if (nota == 0):
        break
    if (0 > nota or nota >100):
        print(f'Entrada invalida "{nota}" ')
        continue
    else:   
        calif.append(nota)

suma_cal = sum(calif)           #suma de las edades
promedio_cal = suma_cal / len(calif) if calif else 0
valor_maximo = max(calif)
valor_minimo = min(calif)
#Hacer una lista con los que tienen un promedio menor
alum_men_prom = [cal for cal in calif if cal > promedio_cal]
print('\n--- Resultados ---')
print(f'Total de notas introducidas: {len(calif)} ')
print(f'Lista de notas: {calif}')
print(f'Suma de notas: {suma_cal}')
print(f'Promedio de notas: {promedio_cal:.2f}')
print(f'Nota Máxima: {valor_maximo}')
print(f'Nota mínima: {valor_minimo}')
print(f'Notas menores al promedio ({promedio_cal:.2f}): {len(alum_men_prom)}')
print(f'lista de notas menores al promedio: {alum_men_prom}')



