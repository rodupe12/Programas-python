#p052-tabla-conversion.py
#Imprimir una tabla de conversion de Peso a Dolar

print ("\033[2J\033[h", end="")
print ('Imprimir una tabla de conversion de Peso a Dolar\n')

tc = 16.80 # Establecemos el tipo de cambio
print(f'Tipo de cambio: {tc}')
while True:
    print('-'* 40)
    while True:
        inicial = float(input('Valor inicial del rango ? '))
        final  = float(input('Valor final del rango   ? '))
        if inicial <= final and inicial > 0 and final > 0 :break
        else: print('Inicial debe ser menos a final') 

    c = inicial
    print('\npeso\tDolar')
    print('-' * 30)
    while c <= final:
        print(f'{c:>10.2f} {c/tc:>10.2f}')
        c+=1
    print('-' * 30)

    if input('\nDame continuar (S/N) ? ').upper() == 'N' : break

print('\nTerminamos de imprimir las tablas ...')