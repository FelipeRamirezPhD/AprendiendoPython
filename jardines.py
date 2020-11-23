# Datos que se tiene
costo_ml=400.00
PI=3.1416

# Datos que se preguntan
_diametro=input("Dame el diámetro: ")
diametro=float(_diametro)

# Datos que se calculan
diametro_ajustado=diametro-3
costo=costo_ml*(PI*diametro_ajustado)
print("{0} metros de jardin, a {1} suma {2}".format(PI*diametro_ajustado,costo_ml,costo))