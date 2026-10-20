#p130-conjunto-personas.py
#Dos listas se transforman en conjuntos y porteriormente se realizan algunas operaciones

#Borrar pantalla
print('\033[H\033[J')

lista1 = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista2 = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

A = set(lista1)
B = set(lista2)

print("Conjunto A:", A)
print("Conjunto B:", B)

union = A | B
print("Union (A | B):", union)

interseccion = A & B
print("Interseccion (A & B):", interseccion)

diferencia = A - B
print("Diferencia (A - B):", diferencia)

diferencia_simetrica = A ^ B
print("Diferencia simetrica (A ^ B):", diferencia_simetrica)

print("{Pablo, Mateo} es subconjunto de B:", {"Pablo", "Mateo"} <= B)
print("A es superconjunto de {Reynaldo, Angelica}:", A >= {"Reynaldo", "Angelica"})
print('"Pedro" esta en A:', "Pedro" in A)
print('"Lilia" no esta en B:', "Lilia" not in B)
