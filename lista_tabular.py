# Muestra tablulada

# Lista gobal
lista_objetos=[]

# Clase a utilizar
class Persona:
    Nombre=""
    Apellido=""
    Edad=0
    def __init__(self,Nombre,Apellido,Edad):
        self.Nombre=Nombre
        self.Apellido=Apellido
        self.Edad

def poblar_lista():
    # Poblar la lista
    lista_objetos.append(Persona("Juan","Pérez",20))
    lista_objetos.append(Persona("Olga","Díaz",21))
    lista_objetos.append(Persona("Angélica","Lagos",27))
    lista_objetos.append(Persona("Pedro","Valle",30))

def muestra_tabular():
    # Tabular
    print("{:>20} {:>20} {:>20}".format( 
        "NOMBRE",
        "APELLIDOS",
        "EDAD"))
    print("{:>20} {:>20} {:>20}".format( 
        "-----------------",
        "-----------------",
        "-----------------"))
    for elemento in lista_objetos:
        print("{:>20} {:>20} {:>20}".format( 
        elemento.Nombre, elemento.Apellido, elemento.Edad))

def main():
    # Point Entry
    # De aquí se ejecuta todo lo demás
    poblar_lista()
    muestra_tabular()

main()