# Se declaran las variables de trabajo, con tipo explícito.
acumulado=int(0)
numero=str("")

# Al colocar True como condición de while, se forma un
# ciclo infinito que no se romperá hasta que de forma
# explícita se utilice la instrucción break.
while True:
    numero=input("Dame un número entero: ")
    if numero=="":
        # Si el número es vacío, reporta la situación y sale.
        print("Vacío. Salida del programa.")
        break
    else:
        # Si se proporcionó valor, acumulado = acumulado + numero
        # Se realiza el cálculo usndo suma incluyente (+=)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))
