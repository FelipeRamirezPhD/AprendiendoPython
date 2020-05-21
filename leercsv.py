# Programa que lea archivos CSV

# Librería para acceder a archivos CSV
import csv

# En el programa usaremos snake_notation (palabras en minúsculas, separadas
# por guiones bajos)

# with genera un bloque de código con referencia.
# "Tengo un bloque de código donde cuando diga archivo_csv, estoy
# hablando de lo que contiene el archivo AnálisisCOVID.csv"
with open('AnálisisCOVID.csv') as archivo_csv:
    # Habilito un objeto que me permitirá leer de forma secuencial
    # el contenido del archivo. En este caso archivo_csv es el puente
    # que me hace llegar de mi programa a mi archivo. lector_csv es el
    # flujo de datos entre el programa y el archivo.
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    # Inicializo el contador de líneas, para poderlas mostrar al final.
    contador_lineas = 0
    # Voy a leer secuencialmente el archivo, usando el flujo de datos
    # (lector_csv) y la línea la voy a colocar en el elemento linea.
    # Cuando trabajemos con <<linea_datos>> estaremos trabajando con la línea
    # del archivo y sus datos.
    for linea_datos in lector_csv:
        # Si el contador vale cero, entonces quiere decir, que nos encontramos
        # en la primera línea del archivo, es decir, donde están los encabezados
        # o nombres de campo. Recuerda que las colecciones son base cero (0,1,2...)
        if contador_lineas == 0:
            # Genero una lista de todos los datos contenidos en linea_datos
            # separados por coma.
            print(f'Los nombres de columna son {", ".join(linea_datos)}')
        else:
            # Mostrar, dato por dato, los contenidos en linea_datos.
            print(f'\tFECHA: {linea_datos[0]}.')
            print(f'\tNUEVOS CONTAGIOS: {linea_datos[1]}.')
            print(f'\tNUEVOS FALLECIMIENTOS: {linea_datos[2]}.')
            print(f'\tPAÍS {linea_datos[3]}.')
            print(f'\t--------------------------------------------')
        # Se incrementa el número de líneas, pase lo que pase.
        contador_lineas += 1

    print(f'Procesadas {contador_lineas} líneas.')