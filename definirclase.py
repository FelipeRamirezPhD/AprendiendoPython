# Define una clase.

# En una aplicacioón de tipo Agenda Personal, se tiene una entidad de datos
# llamada Contacto, mismo que será manejado a través de una clase. 
# La clase tiene las siguientes propiedades.
# telefono: Es el número telefónico del contacto, y actúa como PK.
# nombre: Es el nombre completo del Contacto.
# correo: Es el correo electrónico del contacto.
# registro: Es la fecha de registro en que el contacto se registró.

# Debido a que la clase maneja un dato de tipo date, se importa la librería requerida.
import datetime

# Se declara una clase para el manejo del dato.
# Por lo pronto, solo maneja propiedades.
class Contacto:
  # Se declara un procedimiento constructor.
  # Incluye todas las propiedades como argumentos.
  # La propiedad registro es opcional, porque toma la informción de la
  # fecha del sistema al momento de la instanciación de la clase.
  def __init__(self, telefono, nombre,correo,registro=datetime.datetime.now(),UIValido=False):
    self.telefono=telefono
    self.nombre=nombre
    self.correo=correo
    self.registro=registro
    self.UIValido=UIValido
