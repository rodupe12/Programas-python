# p126-procesar-diccionario.py
# Combina dos listas, las mustra de diferentes formas y suma el saca el promedio de los sueldos

#Borrar pantalla
print('\033[H\033[J')


nombres = ["Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"]
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]

nomina = dict(zip(nombres, sueldos))

print("Diccionario de nómina:")
print(nomina)

print("\n--- Iterando Llaves (keys) ---")
for llave in nomina.keys():
    print(llave)

print("\n--- Iterando Valores (values) ---")
for sueldo in nomina.values():
    print(sueldo)

print("\n--- Iterando Llave y Valor (accediendo por llave) ---")
for llave in nomina:
    print(f"{llave} -> {nomina[llave]}")

print("\n--- Iterando Llave y Valor (items) ---")
for item in nomina.items():
    print(item)

sumaS = sum(nomina.values())
promS = sumaS / len(nomina)

print("\n--- Cálculos ---")
print(f"Suma total de los sueldos: {sumaS:.2f}")
print(f"Promedio de sueldo: {promS:.2f}")
