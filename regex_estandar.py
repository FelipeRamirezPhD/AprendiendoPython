# Permite capturar datos de un contacto, de forma validada.

# Importar código para tener acceso a un módulo
# re es el módulo que me permite tener acceso a las clases para
# validar expresiones regulares.
import re
# Se usará el método re.match(regex,texto)
# Retorna True si texto cumple con el patrón definido en regex
# Retorna False si texto no cumple con el patrón definido en regex

# Expresiones regulares comunes:
# Números enteros
INT_re=r"^[-+]?\d*$"
# Números float
FLOAT_re=r"^([-+]?(\d+\.?\d*|\d*\.?\d+))$"
# Fecha dd-mm-aaaa
DATE_re=r"^(\d+(/|-){1}\d+(/|-){1}\d{2,4})$"
# Correo electrónico
EMAIL_re=r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
# Ancho hasta 100
HASTA100_re = r"^[A-Za-z_.@]{1,100}$"
# Sólo mayúsculas y espacios
MAYUSCESP_re = r"[A-Z ]"
# Sólo mayúsculas y espacios
ENTRE3Y50_re = r"^[A-Z ]{3,50}$"

# La "r" antes del str implica raw mode; no interpreta nada

# Captura de correo
# Utilizo un ciclo infinito, para preguntar hasta que el dato sea correcto.
while True:
    correo_electronico = input("Correo electrónico:")
    # Validación de no omitir
    if (correo_electronico==""):
        print("El dato no se puede omitir.")
    else:
        # Si no se omitió el dato, valida si es correo
        if (bool(re.match(EMAIL_re,correo_electronico))):
            # Si es correo, valida que no sea mayor a 100 caracteres
            if (bool(re.match(HASTA100_re,correo_electronico))):
                break
            else:
                print("No puede ser mayor de 100 caracteres.")
        else:
            print("Lo capturado no es un correo electrónico.")

print("El correo electrónico capturado es {0}".format(correo_electronico))

# Captura de nombre
while True:
    nombre = input("Nombre: ")
    if (nombre==""):
        print("El dato no se puede omitir.")
    else:
        # Si no se omitió el dato, valida si es mayúsculas y espacios
        if (bool(re.match(MAYUSCESP_re,nombre))):
            # Si es mayúsculas y espacios, valida que la longitud sea 3-50
            if (bool(re.match(ENTRE3Y50_re,nombre))):
                break
            else:
                print("La longitud debe ser entre 3 y 50")
        else:
            print("Sólo se admiten MAYÚSCULAS y espacios.")

print("El nombre capturado es {0}".format(nombre))
