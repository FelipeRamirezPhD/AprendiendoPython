numero1=input("Número 1:")
numero2=input("Número 2:")
salida="Números proporcionados: {} y {}. {}."
if (numero1==numero2):
    # Entra aquí si los números capturados son iguales.
    print(salida.format(numero1, numero2,"Los números son iguales"))
else:
    # Condicionales anidadas, if dentro de otro if.
    # Si los números no son iguales.
    if numero1>numero2:
        # Reporta si el primer número es mayor al segundo.
        print(salida.format(numero1, numero2,"El mayor es el primero"))
    else:
        # O de lo contrario, si el primero no es mayor al segundo.
        print(salida.format(numero1, numero2,"El mayor es el segundo"))
