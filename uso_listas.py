# Elaborar un programa que pregunte una serie de cantidades monetarias
# de forma indefinida. Cuando ya no desee capturar más números,
# quiero que me informe cuántos números capturé, cuál es la suma
# de los números, y cuál es el promedio, utilizando formato de moneda.

# Para almacenar una serie de datos, defino una lista.
# [] -> Square Brackets - Corchetes
# {} -> Curly Brackets - Llaves
# () -> Rounded Brackets - Paréntesis
serie_datos=[]

# Pra manejar una operación de forma intermitente, utilizo un ciclo infinito.
# while True, que sólo se interrumpe con break
while True:
    _entrada=input("Dame una cantidad: ")
    entrada=float(_entrada)
    # Agregar datos a la lista
    serie_datos.append(entrada)
    # Condicional para saber si sigo.
    salida=input("Deseas salir? (S/N):")
    if salida.upper()=="S":
        break

# Determinando el número de elementos
numero_elementos=len(serie_datos)

# Sumando los elementos. Hacer una lectura secuencial, usando for.
suma=0.0
for x in serie_datos:
    suma+=x # equivale a suma=suma+x

# Mostrado de datos
print("Se capturaron {0} elementos, que suman {1}. El promedio es ${2:,}".format(numero_elementos,suma,suma/numero_elementos))