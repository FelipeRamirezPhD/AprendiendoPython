# Módulo para poder ejecutar tareas directas en el sistema operativo.
import os
# Módulo para trabajar con expresione regulares
import re

# Se establece una función para borrar pantalla.
# Se usa, expresión lambda, que es equivalente a:
# def clear():
#   os.system('cls')
LimpiarPantalla = lambda: os.system('cls') #on Windows System

# Validador de expresiones regulares
# _txt es el texto a vlidar.
# _regex es el patrón de expresión regular a validar.
# Retorna True si _txt cumple con el patrón definido en _regex
# Retrona False si no es así.
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

def principal():
    while (True):
        LimpiarPantalla()
        print("LISTA DE COTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="2":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")

principal()

# Se tendría que codificar un procedimiento adecuado, en cada una de
# las opciones válidas.
