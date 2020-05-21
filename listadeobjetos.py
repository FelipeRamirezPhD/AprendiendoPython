# Almacena objetos en una lista, y los muestra de diferentes maneras.

# Se pide importar la clase Contacto, que está definida en definirclase.py
from definirclase import Contacto
# Se importa una clase que permite extraer elementos de un objeto
from operator import attrgetter

# Función para mostrar los elementos que tiene la lisa de ejemplo.
def CuantosElementosHay():
    txt = "El número de elementos de la colección es {}"
    print(txt.format(len(Contactos)))

def BuscarTelefono(telabuscar):
    coincidencia=False
    for contacto in Contactos:
        if (contacto.telefono==telabuscar):
            coincidencia=True
            break
    return coincidencia

def BuscarContacto(telabuscar):
    contador=-1
    indice_retorno=-1
    for contacto in Contactos:
        contador+=1
        if (contacto.telefono==telabuscar):
            indice_retorno=contador
            break
    return indice_retorno

# Se declara una lista que almacenará objetos. Inicia sin elementos.
# Muestra los elementos de la lista.
Contactos = []
CuantosElementosHay()

# Se agregan varios objetos a la lista.
Contactos.append(Contacto(1234567890,"Felipe Ramirez","feli.rmz@hotmail.com"))
CuantosElementosHay()

# Se agregan más elementos a la lista.
Contactos.append(Contacto(1134567890,"Franco Leal","feleal@hotmail.com"))
Contactos.append(Contacto(1114567890,"María Medeiros","mmedeiros@hotmail.com"))
Contactos.append(Contacto(1111567890,"Olga Guerrero","guerroolga@gmail.com"))
CuantosElementosHay()

# Barrido secuencial.
for contacto in Contactos:
    print("------------------------------------------")
    print(contacto.telefono)
    print(contacto.nombre)
    print(contacto.correo)
    print(contacto.registro)
    print(contacto.UIValido)

# Ordenamiento.
Contactos.sort(key=attrgetter("telefono"),reverse=False)

print("Ordenado")
# Barrido secuencial.
for contacto in Contactos:
    print("------------------------------------------")
    print(contacto.telefono)
    print(contacto.nombre)
    print(contacto.correo)
    print(contacto.registro)
    print(contacto.UIValido)

# Búsqueda de elementos, usando la función de búsqueda.
# Retorna falso o verdadero, dependendiendo su se encontró
# o no.
print(BuscarTelefono(1234567890))
print(BuscarTelefono(9999999999))

# Búsqueda de objeto y retorno de índice, usando función de
# búsqueda.
print(BuscarContacto(1234567890))
print(BuscarContacto(9999999999))
# Uso del índice recuperado
indice_obtenido=BuscarContacto(1234567890)
if indice_obtenido==-1:
    print("No se encontró el objeto")
else:
    print(Contactos[indice_obtenido].telefono)
    print(Contactos[indice_obtenido].nombre)
    print(Contactos[indice_obtenido].correo)

indice_obtenido=BuscarContacto(9999999999)
if indice_obtenido==-1:
    print("No se encontró el objeto")
else:
    print(Contactos[indice_obtenido].telefono)
    print(Contactos[indice_obtenido].nombre)
    print(Contactos[indice_obtenido].correo)