# Implementación de datos de tipo fecha.
import datetime

# Declaración de una clase.
# Nombre utiliza Pascal Casing
class Pais:
      # Constructor. Método que se encarga de generar un objeto
      # parametrizado. Esta clase tiene 5 propiedades, mismas que
      # están descritas entre paréntesis (argumentos). self no es
      # una propiedad, porque es la referencia que hace el objeto
      # a sí mismo.
      def __init__(self,NombreIng,NombreEsp,Fallecidos,
                Contagiados, PDC):
            # NombreIng: Nombre del país, en inglés (str)
            # NombreEsp: Nombre del país, en español (str)
            # Fallecidos: Total de fallecidos registrados en el país (int)
            # Contagiados: Total de contagiados registrados en el país (int)
            # PDC: Primer día de contagio (datetime)
            self.NombreIng = NombreIng
            self.NombreEsp = NombreEsp
            self.Fallecidos = Fallecidos
            self.Contagiados = Contagiados
            self.PDC = PDC

class  Incidente:
      def __init__(self,Pais,Fecha,NContangios,NFallecidos):
            # Fecha: Fecha de los datos (datetime)
            # Pais: Nombre del país que reporta los datos (str)
            # NContagios: Nuevos contagios presentados en País y Fecha (int)
            # NFallecidos: Nuevos fallecimiento presentados en País y Fecha (int)
            self.Fecha = Fecha
            self.Pais = Pais
            self.NContangios = NContangios
            self.NFallecidos = NFallecidos

# Probar el funcionamiento de nuestras clases.

# Instanciar la clase Pais (creamos un objeto de tipo Pais).
miPais = Pais(str("Mexico"),str("México"),int(1000),int(5000), datetime.datetime(2020, 5, 18) )
print(miPais.PDC)

# Instanciar la clase Incidente. Generación de 2 objetos.
incidenteAyer = Incidente(datetime.datetime(2020, 5, 17), str("Mexico"), int(1500), int(18))
incidenteHoy = Incidente(datetime.datetime.now(), str("Mexico"), int(1400), int(12))
print(incidenteAyer.Pais)
