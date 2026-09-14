#p076-piramide-caracter.py
#Imprime piramide de caracteres

print ("\033[2J\033[h", end="")
print ('Imprime piramide de caracteres')

altura = int(input('De Renglones quieres la piramide ? '))
c = input('Caracter ? ')
espacios = caracteres= 0

for i in range(1, altura + 1):
    espacios = altura - i
    caracteres = 2 * i - 1
    for e in range(espacios):
        print(' ',end='')
    for j in range (caracteres):
        print(c, end='')
    print()

