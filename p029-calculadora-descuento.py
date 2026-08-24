#p029-calculadora-descuento.py
#Simular una calculadora de descuentos basada en el monto de la cantidad que compra


print ("\033[2J\033[h", end="")
print ('Simular una calculadora de descuentos basada en el monto de la cantidad que compra \n')

compra = float(input('Total de compra ? '))
descuento = porsentaje = 0

if compra > 2000:
    porsentaje = 0.20
elif compra > 1000:
    porsentaje = 0.10
elif compra > 500:
    porsentaje = 0.5


descuento = compra * porsentaje
total = compra - descuento

print ('\n Resumen de la compra')
print(f'Total de la compra      : {compra:,.2f}')
print(f'Prorsentaje descuento   : {porsentaje*100}%')
print(f'Descuento               :{descuento}')
print(f'Total a pagar           : {total:,.2f}')



