#p114-nombres-edades.py
#Censo de nombres y edades en un diccionario, hasta <enter> vario

#Borrar la pantalla
print("\033[H\033[J")

#Crear un diccionario para almacenar los nombres y edades
censo = {}

#Solicitar al usuario que ingrese nombres y edades hasta que ingrese un nombre vacío
while True:
    nombre = input("Ingrese un nombre (o presione <enter> para finalizar): ")
    if nombre == "":
        break
    censo[nombre] = int(input(f"Ingrese la edad de {nombre}: "))

#Mostrar el censo de nombres y edades
print(f"\nCenso de nombres y edades: {censo} --- {len(censo)} elementos \n")

# Resumen del censo
print("Resumen del censo:")

for nombre, edad in censo.items():
    print(f" - {nombre} : {edad} años")

suma_edades = sum(censo.values())           #suma de las edades
promedio_edades = suma_edades / len(censo) if censo else 0 ##Promedio de edad, evitar division por cero 
print(f"\nPromedio de edades: {promedio_edades:.2f} años")
