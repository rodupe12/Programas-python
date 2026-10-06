#p103-resumen-ventas.py
#Transforma y filtra ventas con comprecion de listas

print('\033[2J\033[1;1H') #Borrar pantalla
print('Transforma y filtra ventas con comprecion de listas')    

ventas = [1000, 2000, 3000, 400, 500]

#ventas mayores a 1000 aplica 10% de descuento, menos a 1000 aplica 5% de descuento
ventas_descuento = [v * 0.9 if v >= 1000 else v * 0.95 for v in ventas]

#Saques ventas relevantes si son mayores a 1000
Ventas_relevantes = [v for v in ventas if v > 1000]

print('Ventas originales:', ventas)
print('Ventas con descuento:', ventas_descuento)
print('Ventas relevantes (mayores a 1000):', Ventas_relevantes)



