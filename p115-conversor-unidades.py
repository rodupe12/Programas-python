#p115-conversor-unidades.py
#Crear un conversor de unidades de longitud
# Definir un diccionario conversiones que almacene los
# facotres para convertir 'km' a 'm', 'cm', 'mm' a metros

#Borrar la pantalla
print("\033[H\033[J")

#Definir un diccionario conversiones
conversiones = {
    'km': 1000,
    'm': 1,
    'cm': 0.01,
    'mm': 0.001
}

#solicitar un usuario que ingrese la cantidad y la unidad e origen y valida uidades validas
Cantidad = float(input("Ingrese la cantidad a convertir: "))
while True:
    unidad_origen = input("Ingrese la unidad de origen (km, m, cm, mm): ")
    if unidad_origen in conversiones:
        break
    else:
        print("Unidad de origen inválida. Intente nuevamente.")

#Mostrar el resultado de la conversion en metros
metros = Cantidad * conversiones[unidad_origen]
print('Resultado de la conversión:')
print(f"{Cantidad} {unidad_origen} = {metros:.4f} metros.")


