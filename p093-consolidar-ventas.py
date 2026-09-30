#p093-consolidar-ventas.py
#Una empresa tiene 2 sucuarsales y desea consolidar las ventas de cada una de ellas en una sola lista
#Se ingresa n ventas para cada sucursal el usuario lo define
#Las consolida en una sola lista y muestra la suma total de ventas, el promedio, la venta mas alta y la mas baja.

ventass1 = []
ventass2 = []
ventas_consolidadas = []

print('\033[H\033[J')

n = int(input('Ingrese las ventas para la primera sucursal: '))

#Ingresar ventas para la primera sucursal
for i in range(n):
    ventas = float(input(f'Ventas {i + 1}: '))
    ventass1.append(ventas)

#Ingresar ventas para la segunda sucursal
n = int(input('Ingrese las ventas para la segunda sucursal: '))
for i in range(n):
    ventas = float(input(f'Ventas {i + 1}: '))
    ventass2.append(ventas)

#Consolidar ventas en una sola lista
ventas_consolidadas = ventass1 + ventass2
print('\nVentas consolidadas:')
for i, venta in enumerate(ventas_consolidadas, start=1):
    print(f'Venta {i + 1}: {venta}')

#Total de ventas en dinero
total_ventas = sum(ventas_consolidadas)
print(f'\nTotal de ventas: {total_ventas}')
