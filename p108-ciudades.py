#p108-ciudades.py
#Leer un entero n. Llenar una lista con los primeros n números impares.

#Borrar pantalla
print('\033[2J\033[1;1H')

list_ciu=[]
list_ciuCon = []
while True:
    ciudad = input('Introduzca nombre de ciudad ($ para detener): ')
    if(ciudad == '$'):
        break
    else:
        list_ciu.append(ciudad)
        if ciudad[0].lower() in 'aeiou':
            list_ciuCon.append(ciudad)

print('--- Resultados ---')
print(f'Total de ciudades introducidas: {len(list_ciu)}')
print(f'Lista original: {list_ciu}')
list_ciu.reverse()
print(f'Lista ordenada decendente: {list_ciu}')
print(f'Ciudades que inician con consonante: {len(list_ciuCon)}')
print(f'Lista de ciudades con consonantes inicial: {list_ciuCon}')




