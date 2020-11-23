# Pregunta y valida un dato, de acuerdo a un patrón regex

# Módulo requerido para la validación de expresiones regulares
import re
# Módulo para trabajar con datos de tipo datetime
import datetime

# Se declara una variable de paso, que permitirá preguntar y validar información.
captura=""

# Función que valida un dato, y si es correcto, lo coloca en captura, si no,
# se mantiene preguntando. Los argumentos que acepta una función, simplemente se
# enumeran entre los paréntesis.
def askandcheck(_patron,_pregunta="Dame un dato: "):
    # Se especifica que captura es global, para que el programa no asuma que es
    # local para esta función.
    global captura
    while True:
        _fxvalor = input(_pregunta)
        coincide = re.search(_patron, _fxvalor)
        if (coincide):
            captura= _fxvalor
            break
        else:
            print("El dato no es correcto. Intenta de nuevo.")

# Función que convierte una expresión YYYY-MM-DD a datetime
def strtodate(_dtoconv):
    return datetime.datetime(int(_dtoconv[0:4]), int(_dtoconv[5:7]), int(_dtoconv[-2:]))


def main():
    # Sólo acepta un código de 4 dígitos
    askandcheck("^[0-9]{4}$", "ID (4 dígitos): ")
    numeroID=captura
    # Nombre, de 1 a 20 letras mayúsculas, o espacio.
    askandcheck("^([A-Z ]){1,20}$", "Nombre: ")
    nombre=captura
    # S o N
    askandcheck("^[S|N]$", "Acepta (S/N): ")
    acepta=captura
    # Fecha
    askandcheck("^(19|20)\d\d[-](0[1-9]|1[012])[-](0[1-9]|[12][0-9]|3[01])$", "Dame una fecha (YYYY-MM-DD): ")
    fecha=captura

    print(numeroID)
    print(nombre)
    print(acepta)
    print(fecha)
