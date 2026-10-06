##p103-resumen-ventas_v2.py
#Transforma una lsita de ventas usando una funcion y comprecion de listas
#La transmformacion aplica 3 pasos en una misma funcion
# la funcion prosesa la tranformacion, luego en el programa principal es llamada

#Esta funcion aplica 3 trasnformaciones a cada elemento que le llega ocmo parametro( una venta)
# regresa el resultado transformadocion

print('\033[2J\033[1;1H') #Borrar pantalla
#20 ventas de ejemplo que incluyan decimales y valores menores a 1000
ventas = [1000.50, 2000.75, 3000.25, 400.10, 500.90, 1500.60, 2500.80, 3500.40, 4500.20, 5500.30, 600.70, 700.80, 800.90, 900.10, 1000.20, 1100.30, 1200.40, 1300.50, 1400.60, 1500.70]

def transformar_venta(venta):
    #aplica 10% de descuento si la venta es mayor o igual a 1000, de lo contrario aplica 5% de descuento
    if venta >= 1000:
        venta_descuento = venta * 0.9
    else:
        venta_descuento = venta * 0.95
    #si las ventas con descuento son mayores a 1000, se redondea a 2 decimales, de lo contrario se redondea a 1 decimal
    return round(venta_descuento, 2) if venta_descuento > 1000 else round(venta_descuento, 1)

print('Resumen de ventas ')

ventas_transformadas = [transformar_venta(v) for v in ventas]

print('Ventas originales:', ventas)
print('Ventas trasnformadas:', ventas_transformadas)
