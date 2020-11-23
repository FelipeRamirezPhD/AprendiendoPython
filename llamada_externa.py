# Yo puedo mandar llamar otros programas de forma externa.
# Vas a ir al progrma procedimientosfunciones.py y vas a
# importar el procedimiento norecibeargumentos.

from procedimientos_funciones import norecibeargumentos

# Se manda a ejecutar un procedimiento no codificado en este programa
# realmente está en procedimientosfunciones.
# Si el programa desde el cual estamos importando tiene un entry point
# éste se ejecutará. Si no tiene entry point, sólo se ejecutará el elemento
# importado de forma específica.
norecibeargumentos()
