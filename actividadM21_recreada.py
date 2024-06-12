#Clase anterior: Actividad_13

print('Funcion CATCH:')
def catch():
    try: #se intenta abrir el archivo pero no se encuentra y se salta a except
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError: #ocupa el except y hace print
        print('No puedo abrir el file.log')

catch()

print('Funciones TRY, EXCEPT:')
try:
    # Intenta abrir el archivo
    with open('test.txt', 'r') as file:
        # Si el archivo existe, realiza alguna operación
        print("El archivo 'test.txt' fue encontrado.")
        # Aquí podrías realizar operaciones adicionales con el archivo, como leer su contenido
except FileNotFoundError:
    # Si el archivo no existe, maneja la excepción
    print("El archivo 'test.txt' no fue encontrado en el directorio.")