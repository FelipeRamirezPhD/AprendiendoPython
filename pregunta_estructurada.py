# Módulos requeridos
import re
import datetime

# askandckeck(pregunta[,tipo[,regexp]])
# pregunta: es lo que se desea preguntar.
# tipo: es el tipo que se desea. Puede ser: 
#   "int", para integer; 
#   "float", para float;
#   "date", para fecha;
#   "email", para correo electrónico.
def askandcheck(_ask,_type="int",_check="^([+-]?[1-9]\d*|0)$"):
    _captura=""
    # Procesamiento para int
    if _type=="int":
        while True:
            _captura=input(_ask)
            if re.search(_check,_captura):
                return int(_captura)
                break
            else:
                print("El dato no tiene el tipo correcto")
    # Procesamiento para float
    if _type=="float":
        _check="^[-+]?\d*\.?\d*$"
        while True:
            _captura=input(_ask)
            if re.search(_check,_captura):
                return float(_captura)
                break
            else:
                print("El dato no tiene el tipo correcto")
    # Procesamiento para date
    if _type=="date":
        _check="^[0-9]{4}/[0-9]{2}/[0-9]{2}$"
        while True:
            _captura=input(_ask)
            if re.search(_check,_captura):
                    try:
                        anio=int(_captura[0:4])
                        mes=int(_captura[5:7])
                        dia=int(_captura[-2:])
                        return datetime.date(anio,mes,dia)
                    except ValueError:
                        print("El dato no es una fecha calendario correcta")
            else:
                print("El dato no tiene formato correcto AAAA/MM/DD")
    # Procesamiento para email
    if _type=="email":
        _check="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        while True:
            _captura=input(_ask)
            if re.search(_check,_captura):
                return _captura
                break
            else:
                print("El dato no tiene formato de correo")
    # Procesamiento para email
    if _type=="custom":
        _check=_check
        while True:
            _captura=input(_ask)
            if re.search(_check,_captura):
                return _captura
                break
            else:
                print("El dato no tiene formato de correo")

def main():
    personal=askandcheck("Dame tu RFC:","custom","^[A-Z]{3,4}-[0-9]{6}-[A-Z0-9]{3}")
    print(personal)
    print(type(personal))

    correo=askandcheck("Dame tu correo:","email")
    print(correo)
    print(type(correo))

    edad=askandcheck("Dame tu edad:")
    print(edad)
    print(type(edad))

    dinero=askandcheck("Cuánto dinero tienes:","float")
    print(dinero)
    print(type(dinero))

    fechanacimiento=askandcheck("Qué fecha naciste:","date")
    print(fechanacimiento)
    print(type(fechanacimiento))
