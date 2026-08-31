#p049-sumar-consecutivos.py
# Sumanumeros hasta que el total sea >= 100

print ("\033[2J\033[h", end="")
print ('Sumanumeros hasta que el total sea >= 100\n')

c = 0
s = 0
while c <= 200:
    c += 1
    s += c
    print(f'{c} ',end='')
    if s >= 100 :break

print (f'\nLa suma {s} despues de {c} numeros')



