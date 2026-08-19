#p013-funciones-matematicas-precios.py 
#Demostar el uso de funciones matematicas de redondeo

import math as mt

print ("\033[2J\033[h", end="")
print ('Demostar el uso de funciones matematicas de redondeo \n')

precio = 15.49234

print(f'Precio Origen $ {precio:.2f}')
print(f'Arriba        $ {mt.ceil(precio):.2f}')
print(f'Abajo         $ {mt.floor(precio):.2f}')
print(f'Truncar       $ {mt.trunc(precio):.2f}')
print(f'Automatico        $ {round(precio):.2f}')
print(f'Automatico        $ {round(precio,3):.3f}')