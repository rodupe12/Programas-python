#p116-conversion-divisas.py
#Implementar un conversor de divisas a pesos mexicanos (mxn).
# Definir un diccionario conversiones con las tasas 
# de cambio (ej. 'USA', 'EUR', 'GBP', 'JPY', 'CAD')

#Borrar la pantalla
print("\033[H\033[J")

# Definir un diccionario conversiones con las tasas de cambio
conversiones = {
    'USD': 18.50,  # Dólar estadounidense
    'EUR': 20.00,  # Euro
    'GBP': 25.00,  # Libra esterlina
    'JPY': 0.17,   # Yen japonés
    'CAD': 14.50   # Dólar canadiense
}

# Mostrar las opciones de divisas disponibles
print("Opciones de divisas disponibles:")
for divisa in conversiones:
    print(f" - {divisa}")

#Solicitar al usuario que ingrese la cantidad y la divisa de origen, y valida divisas validas
cantidad = float(input("Ingrese la cantidad a convertir: "))
while True:
    divisa_origen = input("Ingrese la divisa de origen (USD, EUR, GBP, JPY, CAD): ")
    if divisa_origen in conversiones:
        break
    else:
        print("Divisa de origen inválida. Intente nuevamente.")

# Mostrar el resultado de la conversión a pesos mexicanos
tasa_cambio = cantidad * conversiones[divisa_origen]
print('Resultado de la conversión:')
print(f"{cantidad} {divisa_origen} = {tasa_cambio:.2f} MXN.")


