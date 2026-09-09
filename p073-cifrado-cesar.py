#p073-cifrado-cesar.py
#Cifra un mensaje con desplazamientos (Cifrado de Cesar)

print ("\033[2J\033[h", end="")
print ('Cifra un mensaje con desplazamientos (Cifrado de Cesar)')

mo = input('Mensaje ? ')
d = int(input('Desplazamientos ? '))

ms = cn = ''

for c in mo:
    if c.isalpha() : # solo letras 
        ca = ord(c)
        #if c.islower():
        #    bd = ord ('a')
        #else:
        #    bd = ord('A')
        bd = ord('a') if c.islower() else ord('A')
        cn = bd + (ca - bd + d) % 26
        ms = ms + chr(cn)
    else:
        ms = ms + c 
print('Mensaje cifrado: ' + ms)

