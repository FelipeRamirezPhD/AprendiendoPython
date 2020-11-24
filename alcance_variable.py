# Este programa demuestra el alcance de las variables

# Una variable global es aquella que se declara fuera de
# cualquier bloque o procedimiento, y está disponible
# en todo el programa, a partir de que se define

# Estas dos variables son globales, y están
# disponibles para todo el programa.
g_dato = "Esta es una variable global"
g_dato2 = "Esta es una variabe global 2"

# Se imprime g_dato, y tiene el contenido asignado.
print (g_dato)

def mi_procedimiento():
    # Esta variable es local. Sólo existe dentro
    # de este procedimiento.
    l_dato = "Esta es una variable local"
    # Si hacemos una asignación de valor a una
    # variable con el mismo nombre de una variable
    # global, lo que sucede es que se declara una
    # variable local del mismo nombre.
    g_dato = "Esta es una variable local, remplaza a la global"
    print(l_dato)
    print(g_dato)

def mi_procedimiento2():
    # Si queremos asignarle un valor a la variable
    # g_datos2 y que no se defina como variable
    # local, hay que declarar que deseamos usar 
    # la variable en su contexto global usando 
    # la palabra global.
    global g_dato2
    g_dato2="Nuevo valor"
    print(g_dato2)

mi_procedimiento()
mi_procedimiento2()
# Esta línea produciría un error, porque la variable
# l_dato no existe en este contesto. Como se definió
# en mi_procedimiento(), sólo existe dentro de ese
# procedimiento.
#       print(l_dato)
print(g_dato)
print(g_dato2)