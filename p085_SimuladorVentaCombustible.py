# p085-simulador-venta-combustible.py
# Sistema interactivo para estación de servicio

while True:
    print("\n" + "=" * 45)
    print("           ESTACIÓN DE SERVICIO - MENÚ        ")
    print("=" * 45)
    print("1. Venta de Combustible")
    print("2. Simulación de Rendimiento")
    print("3. Clasificador de Cliente")
    print("4. Salir")
    print("=" * 45)

    opcion_principal = input("Seleccione una opción (1-4): ")

    if opcion_principal == "1":
        print("\n--- DESPACHO DE COMBUSTIBLE ---")
        print("1. Magna / Regular")
        print("2. Premium")
        print("3. Diésel")

        tipo_combustible = ""
        while tipo_combustible == "":
            opcion_combustible = input("Seleccione tipo (1-3): ")
            if opcion_combustible == "1":
                tipo_combustible = "Magna"
            elif opcion_combustible == "2":
                tipo_combustible = "Premium"
            elif opcion_combustible == "3":
                tipo_combustible = "Diésel"
            else:
                print("Error: Seleccione 1, 2 o 3.")

        # Validación de precio
        precio_valido = False
        while not precio_valido:
            entrada_precio = input("Ingrese el precio por litro ($): ")
            try:
                precio_litro = float(entrada_precio)
                if precio_litro > 0:
                    precio_valido = True
                else:
                    print("Error: El precio debe ser mayor a 0.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

        # Validación de litros
        litros_validos = False
        while not litros_validos:
            entrada_litros = input("Ingrese la cantidad de litros a cargar: ")
            try:
                litros = float(entrada_litros)
                if litros > 0:
                    litros_validos = True
                else:
                    print("Error: Los litros deben ser mayores a 0.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")

        # Cálculos de venta
        total_pago = precio_litro * litros

        # APLICACIÓN DE // Y % (Cálculo logístico: bidones de 20 litros)
        bidones_completos = int(litros // 20)
        litros_sueltos = litros % 20

        # Impresión de ticket
        print("\n" + "=" * 40)
        print("            TICKET DE VENTA             ")
        print("=" * 40)
        print(f"Combustible       : {tipo_combustible:>20}")
        print(f"Litros cargados   : {litros:>18.2f} L")
        print(f"Precio por litro  : ${precio_litro:>19.2f}")
        print("-" * 40)
        print(f"Total a liquidar  : ${total_pago:>19.2f}")
        print("-" * 40)
        print("Desglose de empaque de referencia (20L):")
        print(f" - Bidones llenos : {bidones_completos:>20}")
        print(f" - Litros reman.  : {litros_sueltos:>18.2f} L")
        print("=" * 40)

    elif opcion_principal == "2":
        print("\n--- SIMULADOR DE RENDIMIENTO Y DESGASTE ---")

        # Odómetro inicial
        km_valido = False
        while not km_valido:
            entrada = input("Ingrese odómetro actual (km): ")
            try:
                km_actual = float(entrada)
                if km_actual >= 0:
                    km_valido = True
                else:
                    print("Error: El odómetro no puede ser negativo.")
            except ValueError:
                print("Error: Ingrese un valor numérico.")

        # Rendimiento base
        rend_valido = False
        while not rend_valido:
            entrada = input("Ingrese rendimiento nominal (km/L): ")
            try:
                rendimiento = float(entrada)
                if rendimiento > 0:
                    rend_valido = True
                else:
                    print("Error: El rendimiento debe ser mayor a 0.")
            except ValueError:
                print("Error: Ingrese un valor numérico.")

        # Km por mes
        km_mes_valido = False
        while not km_mes_valido:
            entrada = input("Promedio de kilómetros al mes: ")
            try:
                km_mes = float(entrada)
                if km_mes > 0:
                    km_mes_valido = True
                else:
                    print("Error: Los km mensuales deben ser mayores a 0.")
            except ValueError:
                print("Error: Ingrese un valor numérico.")

        # Meses a proyectar
        meses_validos = False
        while not meses_validos:
            entrada = input("Cantidad de meses a proyectar: ")
            try:
                total_meses = int(entrada)
                if total_meses > 0:
                    meses_validos = True
                else:
                    print("Error: Debe proyectar al menos 1 mes.")
            except ValueError:
                print("Error: Ingrese un número entero.")

        print("\n" + "=" * 70)
        print("                      PROYECCIÓN MENSUAL                              ")
        print("=" * 70)
        print(f"{'Tiempo':^12} | {'Odómetro':>12} | {'Consumo (L)':>14} | {'Eficiencia':>12}")
        print("-" * 70)

        odometro_acumulado = km_actual

        for mes in range(1, total_meses + 1):
            odometro_acumulado += km_mes

            # APLICACIÓN DE // Y % (Conversión de meses a Años y Meses)
            anios = mes // 12
            meses_resto = mes % 12

            # APLICACIÓN DE ** (Factor de pérdida de eficiencia por envejecimiento)
            # Factor de degradación exponencial muy leve: (1 - 0.002) ** mes
            factor_desgaste = (0.998) ** mes
            rendimiento_ajustado = rendimiento * factor_desgaste
            consumo_mes = km_mes / rendimiento_ajustado

            tiempo_str = f"A {anios} M {meses_resto}"
            print(f"{tiempo_str:^12} | {odometro_acumulado:>9.1f} km | {consumo_mes:>12.2f} L | {factor_desgaste * 100:>11.1f}%")

        print("=" * 70)

    elif opcion_principal == "3":
        print("\n--- CLASIFICADOR DE CLIENTE ---")
        volumen_valido = False
        while not volumen_valido:
            entrada = input("Ingrese el volumen mensual comprado (L): ")
            try:
                litros_cliente = float(entrada)
                if litros_cliente >= 0:
                    volumen_valido = True
                else:
                    print("Error: El volumen no puede ser negativo.")
            except ValueError:
                print("Error: Ingrese un número válido.")

        # Estructura if / elif / else con operadores lógicos
        if litros_cliente < 100:
            categoria = "Regular"
            beneficio = "Tarifa base, sin descuento por volumen."
        elif litros_cliente >= 100 and litros_cliente <= 500:
            categoria = "Premium"
            beneficio = "3% de bonificación en monedero electrónico."
        else:
            categoria = "Flotilla"
            beneficio = "Tarifa mayorista y crédito a 30 días."

        print("\n" + "=" * 42)
        print("          CATEGORÍA ASIGNADA              ")
        print("=" * 42)
        print(f"Volumen informado : {litros_cliente:>18.2f} L")
        print(f"Nivel de cliente  : {categoria:>20}")
        print(f"Beneficio activo  : {beneficio}")
        print("=" * 42)

    elif opcion_principal == "4":
        print("\nSaliendo del simulador de combustible. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor elija un número del 1 al 4.")
        continue