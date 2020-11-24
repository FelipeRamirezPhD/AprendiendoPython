# Escritura.py
# Escritura en un archivo plano.

# Importar módulo para trabajar con CSV
import csv

# Importar módulo para el trabajo con archivos
import os

ruta_archivo=os.path.abspath(os.getcwd())
archivo_respaldo=ruta_archivo+"\\contactos.bak"
archivo_normal=ruta_archivo+"\\contactos.csv"

print(archivo_respaldo)
print(archivo_normal)

# Si hay archivo de datos.
if os.path.exists(archivo_normal):
    # verifica si hay respaldo, y lo elimina
    if os.path.exists(archivo_respaldo):
        os.remove(archivo_respaldo)
    # Pasa el archivo normal, para que sea archivo de respaldo
    os.rename(archivo_normal,archivo_respaldo)

# Genera el archivo CSV.
f = open(archivo_normal,"w+")
# Escribir el encabezado.
f.write("USUARIO|NOMBRE|CORREO")
# Cierro el archivo.
f.close()
