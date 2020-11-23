entrada=input()
print(type(entrada))
# La variable booleana contiene el resultado de verificar
# si lo capturado es dígito, y si no se encuentra un punto
# en lo capturado, lo que indicaría se que trata de un
# número con decimales, es decir, float. Si find retorna -1
# quiere decir que lo buscado, en este caso un punto decimal
# no se encontró. Si esEntero es True, lo capturado es entero.
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if (esEntero):
    # Líneas que se ejecutarán si la condición es verdadera (True)
    print("Dato entero. ¡Muy bien!")
else:
    # Líneas que se ejecutarán si la condición es falsa (False)
    print("Dato no es entero. Intentar nuevamente.")
