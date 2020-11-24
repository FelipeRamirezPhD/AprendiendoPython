for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    # print sin argumentos es un salto de línea.
    print()
    # Dentro de un for, se pone otro for.
    for j in range(1,11):
        # Aquí, i contiene el número base de la tabla
        # y j el elemento de la tabla.
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        # Al concluir con las iteraciones indicadas
        # se ejecuta este código, que es un salto de
        # línea.
        print()
