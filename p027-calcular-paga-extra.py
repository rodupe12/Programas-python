#p027-calcular-paga-extra.py
#Calcula la paga de un trabajador considerando horas extras 

print ("\033[2J\033[h", end="")
print ('Calcula la paga de un trabajador considerando horas extras \n')

print ('Dame tus datos')
nombre = input('Nombre : ')
horas = int(input('Horas : '))
pago_hora = float(input('Pago x Hora : '))

horas_normales = 40
pago_normal = horas_normales * pago_hora
horas_extra = pago_extra = 0

if horas > 40:
    pago_normal = 40 * pago_normal
    horas_extra = horas - 40
    pago_extra = horas_extra * (pago_hora*2)
    
else:
    pago_normal = horas * pago_normal

total = pago_normal + pago_extra

print('Calculo de pagos')
print(f'El trabajdor {nombre} trabajo {horas} horas a una pafga de {pago_hora}')
print(f'Pago normal : {pago_normal}')
print(f'Horas Extra : {horas_extra}')
print(f'Pago Extra : {pago_extra}')
print(f'TOTAL. : {  total}')
