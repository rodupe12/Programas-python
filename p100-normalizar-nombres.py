##p100-normalizar-nombres.py
#De una lsita de combres con soacios y mayúsculas,
# se normalizan los nombres en minusculas y sin espacios al inicio o final de cada nombre usando comprecion de listas
# 
print('\033[2J\033[1;1H') #Borrar pantalla
print('Normaliza nombres en minusculas y sin espacios al inicio o final de cada nombre usando comprecion de listas')

nombres = ['  Juan', 'Maria  ', '  Pedro  ', 'Ana', '  Luis  ']

#Se normalizan los nombres usando comprecion de listas
nombres_normalizados = [nombre.strip().lower() for nombre in nombres]

print('Nombres originales:', nombres)
print('Nombres normalizados:', nombres_normalizados)


