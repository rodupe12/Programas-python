#p091-lista-de-gastos.py
#Desarrolla una aplicación que almacene gastos en una lista y permita al usuario
# manipularla a través de un menú que se mostrará continuamente hasta que decida salir.

gastos = []

def mostrar_menu():
    print('\033[H\033[J') # Limpiar la pantalla
    print('Aplicacion de gastos')
    print('1. Agregar gasto')
    print('2. Mostrar gastos')
    print('3. Eliminar gasto')
    print('4. Modificar gasto')
    print('5. Ver total de gastos')
    print('6. Salir')

    print('\nElige una opción: ', end='')
    opcion = input()
    return opcion

def main():
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            try:
                gasto = float(input('Ingresa el monto del gasto: '))
                gastos.append(gasto)
                print(f'Gasto de {gasto} agregado correctamente.')
            except ValueError:
                print('Error: monto inválido. No se agregó el gasto.')
        elif opcion == '2':
            if gastos:
                print('Gastos actuales:')
                for i, gasto in enumerate(gastos):
                    print(f'{i + 1}. {gasto}')
            else:
                print('No hay gastos registrados.')
        elif opcion == '3':
            try:
                indice = int(input('Ingresa el número del gasto a eliminar: ')) - 1
                if 0 <= indice < len(gastos):
                    eliminado = gastos.pop(indice)
                    print(f'Gasto de {eliminado} eliminado correctamente.')
                else:
                    print('Gasto no encontrado.')
            except ValueError:
                print('Error: número de gasto inválido. No se eliminó ningún gasto.')
        elif opcion == '4':
            try:
                indice = int(input('Ingresa el número del gasto a modificar: ')) - 1
                if 0 <= indice < len(gastos):
                    nuevo_gasto = float(input('Ingresa el nuevo monto del gasto: '))
                    gastos[indice] = nuevo_gasto
                    print(f'Gasto modificado correctamente a {nuevo_gasto}.')
                else:
                    print('Gasto no encontrado.')
            except ValueError:
                print('Error: número o monto inválido. No se modificó ningún gasto.')
        elif opcion == '5':
            total = sum(gastos)
            print(f'Total de gastos: {total}')
        elif opcion == '6':
            print('Saliendo de la aplicación.')
            break
        else:
            print('Opción inválida. Intenta de nuevo.')

        input('\nPresiona Enter para continuar...')
if __name__ == '__main__':
    main()