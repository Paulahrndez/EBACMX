#Clase anterior: Actividad_13

print('Funcion CATCH:')
def catch():
    try: #se intenta abrir el archivo pero no se encuentra y se salta a except
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError: #ocupa el except y hace print
        print('No puedo abrir el file.log')

catch()

