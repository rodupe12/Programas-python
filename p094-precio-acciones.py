#p094-precio-acciones.py
#Analisis de precios de acciones diarias
#Dada una lista de cierre de una accion durante la semana
#Encontrar el precio mas alto, el mas bajo, y el dia en que ocurrieron.

print('\033[H\033[J')
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
precios = [150.25, 152.30, 149.80, 151.00, 153.75, 154.20, 150.90]

precio_mas_alto = max(precios)
precio_mas_bajo = min(precios)
indice_mas_alto = precios.index(precio_mas_alto)
indice_mas_bajo = precios.index(precio_mas_bajo)

print('Analisis de precios de acciones diarias')
print(f'Precio más alto: {precio_mas_alto} el día {dias[indice_mas_alto]}')
print(f'Precio más bajo: {precio_mas_bajo} el día {dias[indice_mas_bajo]}')



