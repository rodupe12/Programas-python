#p057-interes-simple.py
#Calcula los años necesarios para alcanzar una meta de ahorro

print ("\033[2J\033[h", end="")
print ('Calcula los años necesarios para alcanzar una mera de ahorro\n')

ci = float(input('Capital inicial ? '))
ti = float(input('Tasa de interes anual (%) ? '))
ma = float(input('Meta de ahorro ? '))

ca = ci
años = iaf = 0
td = (ti/100)

while ca <= ma:
    print(f'{años:2} - {ca:>15,.2f}')
    iaf = ca * td
    ca += iaf
    años += 1

print(f'Para llegar a {ma} debemos pasar {años} años, el capital es {ca}\n')
