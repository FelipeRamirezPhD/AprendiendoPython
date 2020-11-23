# voluntarios.py
# Manejo de información de voluntarios.

# Módulo para usar expresiones regulares.
import re
# Módulo para usar objetos fecha
import datetime

# Queremos capturar información de voluntarios para un causa social.
# Debemos saber, para cada voluntario, la siguiente infomación. Ninguno
# de los datos debe omitirse. Además, aplican las siguientes validaciones
# específicas.


# Correo electronico (correo_electronico)
#       - Debe tener formato de correo válido
#       - Debe tener un máximo de 50 posiciones
while True:
    correo_electronico=input("Dame el correo electrónico: ")
    if (correo_electronico==""):
        print("El correo electrónico no se puede omitir.")
    else:
        if not (re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",correo_electronico)):
            print("Sólo se permiten correos válidos")
        else:
            break

# Apellidos (apellidos)
#       - Todas deben ser mayúsculas
#       - Sólo admite letras, espacios, y caracteres acentuados
#       - Debe tener una longitud entre 3 y 50 posiciones
while True:
    apellidos=input("Dame los apellidos: ")
    if (apellidos==""):
        print("Los apellidos no se pueden omitir.")
    else:
        if not (re.match("^[A-Z ÁÉÍÓÚÜÑ]{3,50}$",apellidos)):
            print("Sólo se permiten de 3 a 50 mayúsculas.")
        else:
            break

# Nombre (nombre)
#       - Todas deben ser mayúsculas
#       - Sólo admite letras, espacios, y caracteres acentuados
#       - Debe tener una longitud entre 3 y 50 posiciones
while True:
    nombre=input("Dame el nombre: ")
    if (nombre==""):
        print("El nombre no se puede omitir.")
    else:
        if not (re.match("^[A-Z ÁÉÍÓÚÜÑ]{3,50}$",nombre)):
            print("Sólo se permiten de 3 a 50 mayúsculas.")
        else:
            break

# Sexo (sexo)
#       - Debe ser "M" o "F"
while True:
    sexo=input("Dame el sexo: ")
    if (sexo==""):
        print("El dato sexo no se puede omitir.")
    else:
        if not (re.match("^[MF]{1}$",sexo)):
            print("Sólo se permite M o F")
        else:
            break

# Teléfono (telefono)
#       - Debe tener el formato (99)9999-9999
while True:
    telefono=input("Dame el teléfono: ")
    if (telefono==""):
        print("El teléfono no se puede omitir.")
    else:
        if not (re.match("^[(]{1}[0-9]{2}[)]{1}[0-9]{4}-[0-9]{4}$",telefono)):
            print("Sólo se permite el formato (99)9999-9999")
        else:
            break

# Fecha de nacimiento (_fecha_nacimiento, _fecha_nacimiento)
#       - Debe tener el formato aaaa-mm-dd
#       - Debe ser una fecha válida
while True:
    # SEH: Structured Exception Handling (manejo estructurado de excepciones)
    # Encerramos cierto bloque de código entre try y except; todo lo que esté
    # entre try y except se considera "protegido". Por "protegido" nos refermos
    # a que el programa no mandará error al usuario final, sino que nosotros
    # le decimos al progrma qué debe ocurrir cuando suceda un error.
    try:
        _fecha_nacimiento = input("Fecha de nacimiento (aaaa-mm-dd): ")
        if (_fecha_nacimiento==""):
            print("La fecha de nacimiento no se puede omitir.")
        else:
            if (re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", _fecha_nacimiento)):
                # Lo capturado debe tener un formato
                # "2020-11-08"
                # Los str son arreglos de caracteres, de base cero.
                # Si empezamos en la posición 0 y extraemos 4, sería "2020"
                # Si empezamos en la posición 5 y extraemos 2, sería "11"
                # Si empezamos de atrás hacia adelante, -2, y tomamos todo
                # hasta concluir, sería "08"
                anio=int(_fecha_nacimiento[0:4])
                mes=int(_fecha_nacimiento[5:7])
                dia=int(_fecha_nacimiento[-2:])
                fecha_nacimiento = datetime.datetime(anio, mes, dia)
                break
            else:
                print("El dato no está en formato aaaa-mm-dd.")
    except ValueError:
        print("La fecha no es una fecha válida.")

# Aportación incial voluntaria (_aportacion, aportacion)
#       - Debe ser un número decimal (flotante)
while True:
    _aportacion=input("Dame la aportación voluntaria inicial: ")
    if (_aportacion==""):
        print("La aportación no se puede omitir.")
    else:
        if not (re.match("^\d+\.\d+$",_aportacion)):
            print("Sólo se permiten números con décimales")
        else:
            aportacion=float(_aportacion)
            break
