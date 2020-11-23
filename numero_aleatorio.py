# python posee muchas librerías listas para utilizarse.
# A dichas librerías les da el nombre de módules (module)
# Para utilizar in módulo en un programa, primero debe
# importarse, usando la instrucción import
import random

# Se define una variable float, y se le asigna un valor.
numero1=float(10.5)

# En python, una función es un conjunto de instrucciones que
# procesan una tarea específica, como una unidad de ejecución.
# Se declaran con def. Todo el código posicionado a la derecha
# de la definición, forma parte de la función.
def miFuncion():
    # Se convierte a float el número aleatorio generado por
    # random.randrange() (sólo está disponible si se importa
    # el módulo random)
    numero2=float(random.randrange(1,10))
    # Se utilizan meta sustituciones para mostrar resultados.
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

# Se ejecuta la función definida en el código.
miFuncion()
