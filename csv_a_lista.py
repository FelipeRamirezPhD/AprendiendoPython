# Programa que lea archivos CSV, y lo carga en un objeto, y lo almacena en una lista.

# Librería para acceder a archivos CSV
import csv
# Librería para manejar datos de tipo datetime
import datetime

# Clase para almacenar los incidentes
class  Incidente:
      def __init__(self,FECHA,CASOS,MUERTES, PAIS):
            self.FECHA = FECHA
            self.CASOS = CASOS
            self.MUERTES = MUERTES
            self.PAIS = PAIS

# Lectura secuencial del archivo
with open('AnálisisCOVID.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    contador_lineas = 0
    # Creando una lista vacía.
    lista_incidentes = []
    # Lectura secuencial.
    for linea_datos in lector_csv:
        if contador_lineas == 0:
            # Si es la primer línea, muestro los nombres de campo y no guardo nada
            # en la lista.
            print(f'Los nombres de columna son {", ".join(linea_datos)}')
        else:
            # Si son datos (línea uno y posteriores)...
            # Genero una instancia de la clase Incidente, y le proporciono al constructor
            # los valores leidos del archivo.
            # RETO: Aquí se convierte el primer valor a su equivalente datetime
            objeto_temporal = Incidente({linea_datos[0]},{linea_datos[1]},{linea_datos[2]},{linea_datos[3]})
            lista_incidentes.append(objeto_temporal)

        # Se incrementa el número de líneas, pase lo que pase.
        contador_lineas += 1

    print(f'Procesadas {len(lista_incidentes)} líneas.')

    # RETO: Modificar la clase para que la propiedad FECHA sea datetime, y no string. Proporcionar
    # la información contenida en {linea_datos[0]} como fecha al objeto. Todo lo demás queda igual.
