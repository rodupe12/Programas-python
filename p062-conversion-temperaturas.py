#p062-conversion-temperaturas.py
#El usuario debe introducir una temperatura inicial y una final en grados Celsius. 
#El programa mostrará la conversión a grados Fahrenheit para cada grado en ese rango, incrementando de uno en uno.
while True:

    print ("\033[2J\033[h", end="")
    print ('El programa mostrará la conversión a grados Fahrenheit para cada grado de un rango\n')
    ti = int(input('Introduce la temperatura inicial en °C: '))
    tf = int(input('Introduce la temperatura Final   en °C: '))
    if ti > tf: continue

    ta = tc = 0
    ta = ti

    while ta <= tf:
        tc = (ta * 9/5) + 32
        print(f'{ta}°c = {tc:.1f}°F')
        ta += 1

    if input('\nDesea continuar (S/N) ? ').upper() == 'N' : break
print('\nProceso terminado')