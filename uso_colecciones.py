# Implementación de datos de tipo fecha.
import datetime

# Declaración de una clase.
class  Incidente:
      def __init__(self,Fecha,Pais,NContangios,NFallecidos):
            # Fecha: Fecha de los datos (datetime)
            # Pais: Nombre del país que reporta los datos (str)
            # NContagios: Nuevos contagios presentados en País y Fecha (int)
            # NFallecidos: Nuevos fallecimiento presentados en País y Fecha (int)
            self.Fecha = Fecha
            self.Pais = Pais
            self.NContangios = NContangios
            self.NFallecidos = NFallecidos

# Instanciar la clase Incidente. Generación de 2 objetos.
incidenteAyer = Incidente(datetime.datetime(2020, 5, 17), str("Mexico"), int(1500), int(18))
incidenteHoy = Incidente(datetime.datetime.now(), str("Mexico"), int(1400), int(12))

# Creación de una lista. Se usa snake_notation. La lista está vacía.
mi_lista = []

# Podemos agregar elementos con append.
mi_lista.append(incidenteAyer)
mi_lista.append(incidenteHoy)

# Mostrar el número de elementos de la lista.
print(len(mi_lista))

# Barrido secuencial de la lista
for elemento in mi_lista:
    print(elemento.Fecha)


# Para el PIA, agregar la clase Pais (del otro programa), instanciar 5 países, y cargarlos
# en una lista llamada mis_paises.