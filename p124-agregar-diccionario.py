# p124-agregar-diccionario.py
# Muestra las ventas iniciales y agrega nuevos vendedor


#Borrar pantalla
print('\033[H\033[J')

ventas = {
    "Juan": 1550,
    "Jose": 2600,
    "Maria": 2220,
}

print("Ventas iniciales: ")
print(ventas)

ventas["Rocio"] = 2500
ventas["Mateo"] = 1567

ventas.update({"Andrea": 9567})
ventas.update({"Miguel": 1234})

print("Ventas actualizadas: ")
print(ventas)
