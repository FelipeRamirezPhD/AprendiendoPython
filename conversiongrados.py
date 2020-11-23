# Módulo para usar expresiones regulares
import re

# Ciclo infinito de cuestionamiento
while True:
    _gcentigrados=input("Dame los grados centígrados: ")
    # Se usa re, en conjunto con raw string expression
    if (_gcentigrados==""):
        print("El dato no se puede omitir.")
    else:
        if (re.search(r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?',_gcentigrados)):
            gcentigrados=float(_gcentigrados)
            # Se hace el cálculo
            gfahrenheit=(gcentigrados*1.8)+32
            # Se muestra con formato.
            print("Conversión: {:.2f}F".format(gfahrenheit))
            # Si la búsqueda del patrón es verdadera, deja de preguntar.
            break
        else:
            print("El dato no es de tipo float.")

print("Fin del programa.")
