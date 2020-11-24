# Módulo para trabajar con CSV
import csv

# Clase de trabajo
class  Contacto:
      def __init__(self,USUARIO, NOMBRE, CORREO):
            self.USUARIO = USUARIO
            self.NOMBRE = NOMBRE
            self.CORREO = CORREO

# Elaboro la lista de trabajo
Contactos = []

# Abrimos CSV y cargamos datos, usando separador |
# Se cargan en una lista de obetos (Contactos)
with open('contactos.csv', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    for e in lector_csv:
        Contactos.append(Contacto(e[0],e[1],e[2]))

# Podemos barrer Contactos, leyendo propiedades.
for o in Contactos:
    print(o.USUARIO)
    print(o.NOMBRE)
    print(o.CORREO)

# Aquí podría capturar nuevos datos, que agregaría a un objeto de tipo Contacto
# y ese objeto, podría cargarlo a la colección, y al final, pasar a un CSV.
