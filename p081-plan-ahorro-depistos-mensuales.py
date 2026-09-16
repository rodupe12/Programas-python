##p081-plan-ahorro-depistos-mensuales.py
# El programa simulará un plan de ahorro. Deberá solicitar al usuario un monto inicial, 
# un depósito mensual fijo, una tasa de interés mensual (porcentaje), y el número total de meses del plan. 
# El programa debe mostrar una tabla que detalle, para cada mes, el saldo inicial, el interés ganado en ese mes, y el saldo final. 
# El interés se calcula sobre el saldo inicial antes de sumar el nuevo depósito.

print ("\033[2J\033[h", end="")

miA = float(input('Monto inicial de ahorro: '))
depM = float(input('Deposito mensual: '))
tiaM = float(input('Tasa de interés mensual (%): '))
mes = int(input('Meses simulados: '))

sAcum = miA
final = 0 
inte = 0

print('\n--- Plan de Ahorro Detallado ---')
for i in range(1,mes+1):
    inte =  sAcum * (tiaM/100)
    fina = sAcum + inte + depM
    print(f'Mes {i}: Saldo Inicial: ${sAcum:.2f} | Interés: ${inte:.2f} | Saldo Final: ${fina:.2f}')
    sAcum = fina

print(f'\nAl final de mes, tendria ${fina:.2f}')