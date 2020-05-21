# Demuestra el uso de expresiones regulares

# Librería para poder validar expresiones regulares en  Python
import re

def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

print(RegEx("HOLA","^[A-Z]{1,20}$"))