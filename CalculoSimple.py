# Importa la librería random
import random

# Declara una variable global llamada baseTriangulo, de tipo string
baseTriangulo=""

# Crea una funcion llamada MiFuncion. Dentro de la función, muestra "Base del triangulo:"
# y pregunta el dato, asignándo el valor a baseTriangulo. Muestra el datatype de la variable.
# Haz la conversión específica de lo capturado  a tipo float, asígnaselo a la variable misma.

def miFuncion():
    global baseTriangulo
    baseTriangulo=input("Base del triangulo:")
    baseTriangulo=float(baseTriangulo)

# Continúa la parte general del programa. Ejecuta miFunción. Declara una variable llamada alturaTriangulo.
# Asígnale un valor aleatorio entre 1 y 20. Muestra el resultado de multiplicar baseTriangulo y alturaTriangulo.
miFuncion()

alturaTriangulo=random.randrange(1,20)
alturaTriangulo=float(alturaTriangulo)
print("Base capturada:" + str(baseTriangulo))
print("Altura obtenida aleatoriamente: " + str(alturaTriangulo))
print("Area calculada: " + str(baseTriangulo*alturaTriangulo))