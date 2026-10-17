#p123-modificar-diccionario.py
#CreaR un diccionario llamado paises, modificar los valores de sus llaves y mostrar el diccionario modificado

#Borrar pantalla
print('\033[H\033[J')

paises = {
    "Argentina": 100,
    "Brasil": 200,
    "Colombia": 300,
    "Chile": 400,
    "Ecuador": 500,
    "Bolivia": 600,
    "Jamaica": 700,
}

print("Diccionario inicial:")
print(paises)

paises["Brasil"] = 250
paises["Chile"] = 450
paises.update({"Bolivia": 650})
paises.update({"Jamaica": 750})

print("\nDiccionario modificado:")
print(paises)
