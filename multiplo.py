# Se captura un número y se almacena una vez que es
# convertido a int
numero=int(input("Dame un número entero: "))
# Se almacenan en valores booleanos la evaluación
# de residuales. Si el residual es cero, quiere decir
# que el número es múltiplo.
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
# Cuando se usa and, se resuelve por verdadero si todas
# las condiciones son verdaderas. Cuando se usa or, se
# resuelve por verdadero si al menos una condición es
# verdadera. Los paréntesis le dicen a python que
# las primeras dos condiciones son juntas, y la tercera
# es independiente.
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")
