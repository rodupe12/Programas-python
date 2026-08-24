#p026–convertir-temperaturas-v2.py
#Convierte temperatura de centigrados a farenheid y viceversa

print ("\033[2J\033[h", end="")
print ('Convierte temperatura de centigrados a farenheid y viceversa \n')
print('[ 1 ] Convertir de Farenheit a Celcius')
print('[ 2 ] Convertir de Celcius a Farenheit ')
op = int(input('Elije ? '))

if op==1:
    print('\nConvertir de Farenheit a Celcius')
    f = float(input('Dame la temperatura en grados Farenheit? '))
    c = (f - 32 ) * 5/9
    #print('Los grados celcius son: ' + str(c))
    print(f' {f} grados Farenheit, equivale a {c} Celcius')

else:
    if op==2:
        print('\nConvertir de celcius a Farenheit')
        c = float(input('Dame la temperatura en grados celcius? '))
        f = (c * 9 / 5) + 32
        #print('Los grados Farenhait son: ' + str(f))
        print(f' {c} Celcius, equivale a {f} Farenheit')
    else:
        print('\nOperacion INVALIDA')

print('\nPrograma Finalizado ..')
