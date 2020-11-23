# Primero se colocan los datos que ya tengo.
dinero=float(500.00)

# Después, siguen los datos que se preguntan
_rendimiento=input("Cuántos kilómetros entrega por litro: ")
rendimiento=float(_rendimiento)
_precio_litro=input("Cuál es el precio de litro de gasolina: ")
precio_litro=float(_precio_litro)

# Después siguen los datos calculados
litros_comprados=(dinero/precio_litro)
distancia=(rendimiento*litros_comprados)

# Mostrar el resutado
print(distancia)