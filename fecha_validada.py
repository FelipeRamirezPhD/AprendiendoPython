# validarfecha.py
# No se debe omitir
# Preguntar por una fecha, en formato YYYY-MM-DD
# Debe ser una fecha válida.

# Módulo para usar expresiones regulares.
import re
# Módulo para usar objetos fecha
import datetime

# Queremos capturar información de voluntarios para un causa social.
# Debemos saber, para cada voluntario, la siguiente infomación. Ninguno
# de los datos debe omitirse. Además, aplican las siguientes validaciones
# específicas.

# Correo electronico
#       - Debe tener formato de correo válido
#       - Debe tener un máximo de 50 posiciones
# Apellidos
#       - Todas deben ser mayúsculas
#       - Sólo admite letras, espacios, y caracteres acentuados
#       - Debe tener una longitud entre 3 y 50 posiciones
# Nombre
#       - Todas deben ser mayúsculas
#       - Sólo admite letras, espacios, y caracteres acentuados
#       - Debe tener una longitud entre 3 y 50 posiciones
# Sexo
#       - Debe ser "M" o "F"
# Teléfono
#       - Debe tener el formato (99)9999-9999
# Fecha de nacimiento
#       - Debe tener el formato aaaa-mm-dd
#       - Debe ser una fecha válida



while True:
    # SEH: Structured Exception Handling (manejo estructurado de excepciones)
    # Encerramos cierto bloque de código entre try y except; todo lo que esté
    # entre try y except se considera "protegido". Por "protegido" nos refermos
    # a que el programa no mandará error al usuario final, sino que nosotros
    # le decimos al progrma qué debe ocurrir cuando suceda un error.
    try:
        _FechaNacimiento = input("Fecha de nacimiento (aaaa-mm-dd): ")
        if (_FechaNacimiento==""):
            print("La fecha de nacimiento no se puede omitir.")
        else:
            if (re.match(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", _FechaNacimiento)):
                # Lo capturado debe tener un formato
                # "2020-11-08"
                # Los str son arreglos de caracteres, de base cero.
                # Si empezamos en la posición 0 y extraemos 4, sería "2020"
                # Si empezamos en la posición 5 y extraemos 2, sería "11"
                # Si empezamos de atrás hacia adelante, -2, y tomamos todo
                # hasta concluir, sería "08"
                anio=int(_FechaNacimiento[0:4])
                mes=int(_FechaNacimiento[5:7])
                dia=int(_FechaNacimiento[-2:])
                FechaNacimiento = datetime.datetime(anio, mes, dia)
                break
            else:
                print("El dato no está en formato aaaa-mm-dd.")
    except ValueError:
        print("La fecha no es una fecha válida.")