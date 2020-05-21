# Librería que permite utilizar listas de objetos
from typing import List
# Librería que permite serializar a JSON
import json

# Se declara una clase para almacenar una entidad general
# de persona, con dos propiedades: nombre, apelidos.
class Persona:
    # Las variables dentro de una clases son propiedades.
    nombre=""
    apellidos=""
    # Método constructor, permite instanciar proporcionando
    # valores a las propiedades. self refiere al objeto mismo.
    def __init__(self, nombre, apellidos):
        # Las propiedades de igualan a los argumentos proporcionados.
        self.nombre=nombre
        self.apellidos=apellidos
    # Los procedimientos dentro de una clases son métodos.
    # Este método muestra los valores contenidos en las propiedades.
    # la referencia self indica que se trata del objeto instanciado.
    def muestraInfo(self):
        print("Clase Base")
        print(self.nombre)
        print(self.apellidos)

# Clase Estudiante hereda la funcionalidad de la clase Persona.
class Estudiante(Persona):
    # La clase Estudiante agrega una propiedad adicional a las que
    # proporciona Persona.
    aniograduacion=0
    # Estudiante tiene su propio método constructor, pero hereda
    # todos los elementos de su clase base, en este caso Persona.
    def __init__(self, nombre, apellidos, aniograduacion=2015):
        super().__init__(nombre, apellidos)
        self.aniograduacion=aniograduacion
    def muestraInfo(self):
        print("Clase Derivada")
        print(self.nombre)
        print(self.apellidos)
        print(self.aniograduacion)
    def derivadoInfo(self):
        print(self.aniograduacion)

# Uso de clases.
print("----------------------------------------------")
unaPersona=Persona("Felipe","Ramirez")
unaPersona.muestraInfo()
print("----------------------------------------------")
unEstudiante=Estudiante("Alejandro","Jodorowski")
unEstudiante.aniograduacion=2019
unEstudiante.muestraInfo()
print("----------------------------------------------")
unEstudiante.derivadoInfo()

# Lista de objetos.
Estudiantes=[]
Estudiantes.append(Estudiante("Juan", "Hernández",2022))
Estudiantes.append(Estudiante("María", "Gómez",2023))
Estudiantes.append(Estudiante("Nidia", "Márquez",2021))

# Serialización.
print(Estudiantes)
# Serialization
json_data = json.dumps(Estudiantes, default=lambda o: o.__dict__, indent=4)
print(json_data)
