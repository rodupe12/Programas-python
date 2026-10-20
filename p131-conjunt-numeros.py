#p131-conjunt-numeros.py
#Crea tres conjuntos y muestra sus operaciones y preguntas

#Borrar pantalla
print('\033[H\033[J')

lista1 = [50, 60, 70, 80, 90, 100, 200]
lista2 = [60, 90, 100, 300, 400, 500]
lista3 = [10, 20, 60, 90, 70, 100, 600, 700]

A = set(lista1)
B = set(lista2)
C = set(lista3)

print("Conjunto A:", A)
print("Conjunto B:", B)
print("Conjunto C:", C)

union_A_B = A | B
print("Union (A | B):", union_A_B)

union_B_C = B | C
print("Union (B | C):", union_B_C)

diferencia_A_C = A - C
print("Diferencia (A - C):", diferencia_A_C)

diferencia_simetrica_B_C = B ^ C
print("Diferencia simetrica (B ^ C):", diferencia_simetrica_B_C)

interseccion_B_C = B & C
print("Interseccion (B & C):", interseccion_B_C)

print("¿A es subconjunto de B?", A <= B)
print("¿C es subconjunto de A?", C <= A)
print("¿El numero 100 esta en A?", 100 in A)
print("¿El numero 60 esta en A, B y C?", 60 in A and 60 in B and 60 in C)
print("¿El numero 900 no esta en C?", 900 not in C)
