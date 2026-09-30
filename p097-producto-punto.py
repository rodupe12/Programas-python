#p097-producto-punto.py
#Caclulo del producto punto de dos vectores.

v1 = [1, 2, 3]
v2 = [4, 5, 6]

if len(v1) != len(v2):
    raise ValueError("Los vectores deben tener la misma longitud.")
else:
    #calcula el producto punto de los dos ventores y mostrar el resultado.
    producto_punto = 0
    for i in range(len(v1)):
        producto_punto += v1[i] * v2[i]
    # El resultado del producto punto de 
    print("Producto punto:", producto_punto)