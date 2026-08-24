#p028-retira-cuenta.py
#Simula el retiro de dinero de una cuenta con validacion

saldo_cuenta = 1500.00

print ("\033[2J\033[h", end="")
print ('Simula el retiro de dinero de una cuenta con validacion \n')

cantidad_retiro = float(input(f'Cantidad a retirar de la cuenta con saldo: {saldo_cuenta} ? '))

if cantidad_retiro > 0:
    print('\nProcedemos al retiro ... ')
    if cantidad_retiro <= saldo_cuenta:
        nuevo_saldo = saldo_cuenta - cantidad_retiro
        print(f'\nRetiro exitoso, tu nuevo saldo es : {nuevo_saldo}')
    else:
        print(f'Quiere retirar {cantidad_retiro} pero tiene {saldo_cuenta} NO TE ALCANZA')
else:
     print('\nLa cantidad de retiro debe de ser un numero positivo')

print('\nGracias por usar nuestros servicios')


