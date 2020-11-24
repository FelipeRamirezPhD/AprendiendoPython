# Escritura en archivo de Texto Plano
# Importar módulo para trabajar con el sistema operativo.
import os
# Importo el módulo para trabajar con CSV

# Declarar la clase Contacto.
# Esta clase servirá para poblar una lista que me permite manejar
# en memoria los datos. La lista se vacía al CSV al final del programa
class  Contacto:
      def __init__(self,USUARIO, NOMBRE, CORREO):
            self.USUARIO = USUARIO
            self.NOMBRE = NOMBRE
            self.CORREO = CORREO

# Lista en la cual vamos a trabajar con los Contactos
Contactos = []
# Se cargan dos elementos.
Contactos.append(Contacto('master','José Ruiz','jose.ruiz@hotmail.com'))
Contactos.append(Contacto('student','Alma Pérez','almitarules@hotmail.com'))
# En el programa final, realmente la lista se carga a partir del CSV.

# Guardo en una variable la ruta absoluta, del directorio actual de trabajo (cwd)
ruta = os.path.abspath(os.getcwd())
archivo_trabajo=ruta+"\\contactos.csv"
archivo_respaldo=ruta+"\\contactos.bak"

# Determinar si el archivo de trabajo ya existe.
if os.path.exists(archivo_trabajo):
    # Si el archivo existe, entonces verifico si hay respaldo y lo borro.
    if os.path.exists(archivo_respaldo):
        os.remove(archivo_respaldo)

    # Establezco el achivo de datos, como respaldo
    os.rename(archivo_trabajo,archivo_respaldo)

# Genera el archivo CSV
f = open(archivo_trabajo,"w+")
# Escribo los encabezados de mi CSV
f.write("USUARIO|NOMBRE|CORREO\n")
# Escribimos en el CSV, a partir de la lista de objetos.
for elemento in Contactos:
    f.write(f'{elemento.USUARIO}|{elemento.NOMBRE}|{elemento.CORREO}\n')

# Cierro el archivo
f.close()
