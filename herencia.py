class Persona:
    nombre=""
    apellidos=""
    def __init__(self, nombre, apellidos):
        self.nombre=nombre
        self.apellidos=apellidos
    def muestraInfo(self):
        print("Clase Base")
        print(self.nombre)
        print(self.apellidos)

class Estudiante(Persona):
    aniograduacion=0
    def muestraInfo(self):
        print("Clase Derivada")
        print(self.nombre)
        print(self.apellidos)
        print(self.aniograduacion)
    def derivadoInfo(self):
        print(self.aniograduacion)

print("----------------------------------------------")
unaPersona=Persona("Felipe","Ramirez")
unaPersona.muestraInfo()
print("----------------------------------------------")
unEstudiante=Estudiante("Alejandro","Jodorowski")
unEstudiante.aniograduacion=2019
unEstudiante.muestraInfo()
print("----------------------------------------------")
unEstudiante.derivadoInfo()


