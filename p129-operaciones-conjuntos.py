#p129-operaciones-conjuntos.py
#Operaciones con conjuntos

c1 = {1, 2, 3, 4, 5}
c2 = {5, 6, 7, 8, 9, 10}
c3 = {9, 10, 11, 12, 13}
c4 = {3, 4, 5}

#Borrar pantalla
print('\033[H\033[J')

print("--- Conjuntos Base ---")
print(f'c1: {c1}')
print(f'c2: {c2}')
print(f'c3: {c3}')
print(f'c4: {c4}')

#Union de conjuntos
print("\nUnion de conjuntos")
print(f"c1 union c2: {c1.union(c2)}")
print(f"c1 union c3: {c1 | c3}")

#Intersección de conjuntos
print("\nIntersección de conjuntos")
print(f"c1 intersección c2: {c1.intersection(c2)}")
print(f"c2 intersección c3: {c2 & c3}")

#Diferencia de conjuntos
print("Diferencia de conjuntos")
print(f"c1 diferencia c4 (Elementos en c1, no en c4):{c1.difference(c4)}")
print(f"c2 diferencia c3 (Elementos en c2, no en c3): {c2 -c3}")

#Diferencia simétrica entre nconjuntos
print("\n--- Diferencia Simétrica ( ^ ) ---")
print(f"c1 dif. simétrica c2 (Elementos en c1 o c2, no en ambos): {c1.symmetric_difference(c2)}")
print(f"c2 dif. simétrica c3: {c2 ^ c3}")

#Subconjuntos y superconjuntos
print("\n--- Subconjuntos ( <= ) ---")
print(f"¿c4 es subconjunto de c1? : {c4.issubset(c1)} True)")
print(f"¿c3 es subconjunto de c2? : {c3 <= c2} (False)")

print("\n--- Superconjuntos ( >= ) ---")
print(f"¿c1 es superconjunto de c4? : {c1.issuperset(c4)} (True)")
print(f"¿c2 es superconjunto de c3? : {c2 >= c3} (False)")

print("\n--- Pertenencia ( in / not in ) ---")
print(f"¿Está el 2 en c1? : {2 in c1} (True)")
print(f"¿No está el 6 en c1? : {6 not in c1} (True)")



