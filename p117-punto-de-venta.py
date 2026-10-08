#p117-punto-de-venta.py
#Crear un sistema simple de punto de centa (pos) para un puesto de comida.

comida = {
    'Hamburguesa': 5.0,
    'Papas Fritas': 2.5,
    'Refresco': 1.5,
    'Hot Dog': 3.0,
    'Pizza': 8.0
}

#Mostrar memu: Mostrar al usiario los productos disponibles y sus precios, iterando sobre el diccionario comida
print('Menu de productos disponibles:')
for producto, precio in comida.items():
    print(f" - {producto}: ${precio:.2f}")

#Tomar orden: preguntar al usuario que desea ordenar en un buble
# si el producto no esta en el menu, informarle.
# Si el producto existe, solicite la cantidad.
orden = {}
while True:
    producto = input("Ingrese el producto que desea ordenar (o presione <enter> para finalizar): ")
    if producto == "":
        break
    if producto not in comida:
        print("Producto no disponible. Intente nuevamente.")
        continue
    cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
    if producto in orden:
        orden[producto] += cantidad
    else:
        orden[producto] = cantidad
#Mostrar el subtotal por producto y el total generar de la compra
print("\nResumen de la orden:")
total_general = 0
for producto, cantidad in orden.items():
    subtotal = comida[producto] * cantidad
    total_general += subtotal
    print(f" - {producto}: {cantidad} x ${comida[producto]:.2f} = ${subtotal:.2f}")

print(f"\nTotal general: ${total_general:.2f}")

