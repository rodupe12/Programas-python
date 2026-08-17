#p004-paga-trabajador.py
#Calucla la paga de un trabajador

print ("\033[2J\033[h", end="")
print ('Calculando la paga de un trabajdor \n')

#Entrada
nombre = input('Dame tu nombre? ')
horas = int(input('Horas? '))
paga = float(input('Paga? '))

#Poceso
tasa = 0.03
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

#Salida
print('\nResumen de pago \n')
print(f'El trabajador {nombre}, trabajo {horas} horas, a una paga de {paga} pesos')
print(f'Paga bruta {pagabruta}')
print(f'Impuesto {impuesto:.2f}')
print(f'Paga neta {paganeta}')