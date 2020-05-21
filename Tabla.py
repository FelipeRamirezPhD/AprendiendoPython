numero=input("Dame un número del 1 al 9: ")
numero=int(numero)
# for ejecuta un bloque de código un número determinado
# de veces, cuando se pide que recorra un rango de
# valores. El segundo parámetro de range no se incluye
# en la serie de valores. Aquí sería del 1 al 10.
for i in range(1,11):
    # i va variando a cada iteración.
    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))