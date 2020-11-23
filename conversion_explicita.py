# Se declara una variable str, con una cadena de dígitos
numero="1234"
# Se muestra el tipo que tiene la variable. La salida de type()
# no es un str, es un dato type.
print(type(numero))
# Se convierte la cadena a su equivalenci int.
numero=int(numero)
# Se muestra cómo el tipo ha cambiado, aunque se usa la misma
# variable.
print(type(numero))
# Se declara un str con meta sustitución (posiciones donde irán
# valores proporcionados usando format.
salida="El número utilizado es {}"
# Se muestra el resultado. La meta sustitución hará que donde está
# {} se coloque el valor de numero.
print(salida.format(numero))
