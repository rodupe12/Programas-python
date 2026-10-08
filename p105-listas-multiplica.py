#p105-listas-multiplica.py
# Leer dos listas, cada una con 5 elementos numéricos. 
# Crear una tercera lista multiplicando los elementos de las dos listas correspondientes. 
# Imprimir las tres listas.

#Borrar pantalla
print('\033[2J\033[1;1H')

while True:
    listaA = list(map(int, input("Introduzca 5 números para la Lista A: ").split()))
    #listaA = list(int,input('Introduzca 5 números para la Lista A: ').split)
    listaB = list(map(int, input("Introduzca 5 números para la Lista B: ").split()))   
    if len(listaA) == len(listaB) == 5:
        break
    else:
        print('Las listas deben de tener la misma magnitud y ser solo 5 valores')
        continue

listaC = [listaA[i] * listaB[i] for i in range(len(listaA))]
print('\n--- Resultados---')
print(f'Lista A: {listaA} ')
print(f'Lista B: {listaB} ')
print(f'Lista C (A * B): {listaC} ')






