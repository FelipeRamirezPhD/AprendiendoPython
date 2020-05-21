# Demostracion de los diferentes tipos de funciones
# Argumentos utilizados
#   No recibe argumentos
#   Recibe argumentos
#   Tiene argumentos opcionales
# Retorno de valores
#   No retorna valores
#   Retorna valores
# Se pueden dar combinaciones de ambos aspectos

# Para declarar funciones se utiliza def

# def nombredefuncion():
#       codigo

# El codigo de la funcion es obligatorio. Si no hay 
# hay codigo por el momento, usar pass

# Si una variable se declara fuera de procedimiento
# se dice que es global 
variableglobal="Soy global"
# Dentro de las funciones, si se quiere usar la
# variable global, debe anteponerse la palabra
# reservada global

def pendiente():
    pass

def norecibeargumentos():
    # Si se comenta la siguiente linea, usar la variable 
    # equivale a declarar una version local de la 
    # variable; si no se comenta, usar la variable 
    # implica usar la global 
    # global variableglobal
    variableglobal=4
    print("No recibe argumentos")
    print(variableglobal)

# Los argumentos se dentro de parentesis en forma
# de lista separada por comas.
def recibeargumentos(fname, lname):
    print(fname + " " + lname)
    print(variableglobal)

# Un argumento es opcional cuando le asignas un valor 
# al momento de su declaracion.
# Los argumentos opcionales siempre van al final de la 
# lista de argumentos.
def argumentosopcionales(city, country = "Mexico"):
    print("I am from " + city + ", " + country)

# Si se especifica return, la funcion retorna valores 
# Cuidar que el flujo del programa siempre los retorne
# Se debe utilizar como expresion, atendiendo el 
# retorno correspondiente
def elevoalcuadrado(x):
  return x * x

def main():
    # norecibeargumentos()
    # recibeargumentos("Felipe", "Ramirez")
    # argumentosopcionales("Monterrey")
    # argumentosopcionales("New York", "USA")
    print(elevoalcuadrado(4))