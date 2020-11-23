# Uso de expresiones regulares.
# Sirven para verificar si una cadena string cumple con un patrón
# en formato de expresión regular.
# Apoyarse en: https://regexr.com/

# Módulo que permite usar expresiones regulares.
import re

# Ciclo infinito.
while True:
    rfc=input("Dame el RFC: ")
    # Si el valor capturado en rfc hace match con la expresion regular (re.search)...
    if (re.search(r'^[A-Z]{4}-[0-9]{6}-[A-Z0-9]{3}$',rfc)):

        # usar r'expresion_regular' es muy efectivo.
        # la r indica Raw String, lo que causa que no se interpreten
        # \ como secuencias de escape.

        # anuncia que es válido
        print("Es un RFC válido.")
        # se sale del ciclo
        break
    else:
        # De lo contrario, anuncia que no es válido, y vuelve a preguntar
        print("No es un RFC válido. Intenta de nuevo.")