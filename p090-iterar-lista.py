#p090-iterar-lista.py
# Iterar elementos de una lista
# 1 por elemento, 2 por indice, 3 por elemento sumando 2, 4, por indice sumando 10, 5 con enumerate

nums = [2, 4, 6, 8, 10, 12, 14, 16]

print('\033[H\033[J')  # Limpiar la pantalla])
print('Iterar elementos de una lista')

#iterar por elemento
print('\nIterar por elemento:')
for n in nums:
    print(n, end=' ')
print()

# Iterar por indice
print('\nIterar por indice:')
for i in range(len(nums)):
    print(f'Índice {i}: {nums[i]}')

# Iterar por elemento sumando 2
print('\nIterar por elemento sumando 2:')
for n in nums:
    print(n + 2, end=' ')
print()

# Iterar por indice sumando 10
print('\nIterar por indice sumando 10:')
for i in range(len(nums)):
    print(f'Índice {i}: {nums[i] + 10}')

# Iterar con enumerate
print('\nIterar con enumerate:')
for i, n in enumerate(nums):
    print(f'Índice {i}: {n}')
