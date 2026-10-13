#p120-reporte-ventas.py
#Crear una lista de diccionarios para representar un reporte de ventas


#Borrar pantalla
print('\033[H\033[J')

compras = []

print("\Registro de compras de la tienda \n")
n = int(input("Número de compras a registrar: "))


for i in range(1,n+1):
    print(f'\nCompra {i}:')
    compra = {
        "cliente" : input("Nombre : "),
        "producto": input("Producto : "),
        "cantidad": int( input("Cantidad : ")),
        "precio"  : float(input("Precio : "))
    }
    compras.append(compra)

#Consolidar las compras por cliente

clientes = {} 
#####print('\n--- Lista de Compras Registradas ---\n',compras)
for compra in compras:
    cliente = compra["cliente"]
    if cliente not in clientes:
        clientes[cliente] = {"total_gastado": 0, "total_gastado": 0.0}
    clientes[cliente]["total_producto"] += compra["cantidad"]
    clientes[cliente]["total_gastado"] += compra["cantidad"] * compra["precio"]

#Mostrar reporte consolidado por cliente
print('\nReporte consolidado por cliente:')
for cliente, datos in clientes.items():
    print("Cliente :", cliente)
    print("Cantidad Total de Productos :", datos["cantidad"])
    print("Subtotal a Pagar : $", datos["subtotal"])
    print()

print('\nDiccionario de Clientes con totales',clientes)


