#p136-segundo-examen-parcial.py
# Registro de vuelos de una aerolínea

vuelos = []

print("REGISTRO DE VUELOS")
print("Ingrese * o deje vacio el numero de vuelo para terminar.")

while True:
    numero_vuelo = input("\nIngrese el numero de vuelo: ").strip()

    # Condicion para finalizar
    if numero_vuelo == "*" or numero_vuelo == "":
        break

    # Validar los datos del vuelo
    origen = input("Ingrese el origen: ").strip()
    destino = input("Ingrese el destino: ").strip()
    aerolinea = input("Ingrese la aerolinea: ").strip()

    # Validar cantidad de pasajeros
    try:
        pasajeros = int(input("Ingrese la cantidad de pasajeros: "))

        if pasajeros < 0:
            print("Error: los pasajeros no pueden ser negativos.")
            continue

    except ValueError:
        print("Error: ingrese un numero entero para los pasajeros.")
        continue

    # Validar tarifa
    try:
        tarifa = float(input("Ingrese la tarifa: "))

        if tarifa < 0:
            print("Error: la tarifa no puede ser negativa.")
            continue

    except ValueError:
        print("Error: ingrese un valor numerico para la tarifa.")
        continue

    # Validar campos de texto
    if origen == "" or destino == "" or aerolinea == "":
        print("Error: origen, destino y aerolinea son obligatorios.")
        continue

    # Crear el diccionario
    vuelo = {
        "numero_vuelo": numero_vuelo,
        "origen": origen,
        "destino": destino,
        "aerolinea": aerolinea,
        "pasajeros": pasajeros,
        "tarifa": tarifa
    }

    # Almacenar el vuelo
    vuelos.append(vuelo)

    print("Vuelo registrado correctamente.")

# Obtener los destinos unicos
destinos_unicos = set()

for vuelo in vuelos:
    destinos_unicos.add(vuelo["destino"].strip().title())

lista_vuelos = []

for vuelo in vuelos:
    tupla = (
        vuelo["numero_vuelo"],
        vuelo["aerolinea"],
        vuelo["destino"]
    )
    lista_vuelos.append(tupla)

# 1. Datos crudos
print("\n--- DATOS CRUDOS ---")
print(vuelos)


# 2. Formato tabular
print("\n--- FORMATO TABULAR ---")
print(f"{'| Numero vuelo':<15}{'| Origen':<20}{'| Destino':<20}"
      f"{'| Aerolinea':<20}{'| Pasajeros':>12}{'| Tarifa':>12}")

print("-" * 99)

for vuelo in vuelos:
    print(f"|{vuelo['numero_vuelo']:<14}"
          f"|{vuelo['origen']:<19}"
          f"|{vuelo['destino']:<19}"
          f"|{vuelo['aerolinea']:<20}"
          f"|{vuelo['pasajeros']:<14}"
          f"|${vuelo['tarifa']:>11.2f}")

# 3. Destinos unicos
print("\n--- DESTINOS UNICOS ---")
print(destinos_unicos)
print("Total de destinos unicos:", len(destinos_unicos))


# 4. Registro inmutable (lista de tuplas)
print("\n--- REGISTRO INMUTABLE ---")
print(lista_vuelos)


# ==========================================
# RESUMEN DEL REGISTRO
# ==========================================

print("\n--- RESUMEN DEL REGISTRO ---")

total_vuelos = len(vuelos)
print("Total de vuelos registrados:", total_vuelos)

if total_vuelos > 0:

    # Vuelos por aerolinea
    vuelos_aerolinea = {}

    for vuelo in vuelos:
        aerolinea = vuelo["aerolinea"]

        if aerolinea not in vuelos_aerolinea:
            vuelos_aerolinea[aerolinea] = 0

        vuelos_aerolinea[aerolinea] += 1

    print("\nCantidad de vuelos por aerolinea:")

    for aerolinea, cantidad in vuelos_aerolinea.items():
        print(f"{aerolinea}: {cantidad}")


    # Vuelos por ciudad de destino
    vuelos_destino = {}

    for vuelo in vuelos:
        destino = vuelo["destino"].strip().title()
        if destino not in vuelos_destino:
            vuelos_destino[destino] = 0

        vuelos_destino[destino] += 1

    print("\nCantidad de vuelos por ciudad de destino:")

    for destino, cantidad in vuelos_destino.items():
        print(f"{destino}: {cantidad}")


    # Total y promedio de pasajeros
    total_pasajeros = sum(vuelo["pasajeros"] for vuelo in vuelos)
    promedio_pasajeros = total_pasajeros / total_vuelos

    print("\nTotal de pasajeros:", total_pasajeros)
    print(f"Promedio de pasajeros por vuelo: {promedio_pasajeros:.2f}")


    # Total y promedio de tarifas
    total_tarifas = sum(vuelo["tarifa"] for vuelo in vuelos)
    promedio_tarifas = total_tarifas / total_vuelos

    print(f"Suma total de tarifas: ${total_tarifas:.2f}")
    print(f"Tarifa promedio: ${promedio_tarifas:.2f}")


   # Vuelo mas caro y mas barato
    vuelo_caro = vuelos[0]
    vuelo_barato = vuelos[0]

    for vuelo in vuelos[1:]:
        if vuelo["tarifa"] > vuelo_caro["tarifa"]:
            vuelo_caro = vuelo

        if vuelo["tarifa"] < vuelo_barato["tarifa"]:
            vuelo_barato = vuelo
            
    print("\nVuelo mas caro:")
    print("Numero de vuelo:", vuelo_caro["numero_vuelo"])
    print(f"Tarifa: ${vuelo_caro['tarifa']:.2f}")

    print("\nVuelo mas barato:")
    print("Numero de vuelo:", vuelo_barato["numero_vuelo"])
    print(f"Tarifa: ${vuelo_barato['tarifa']:.2f}")

else:
    print("No hay vuelos registrados para generar estadisticas.")

print("\nFin del programa.")
