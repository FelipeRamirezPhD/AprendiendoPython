# Formatos especiales en Python

# Texto con 2 placeholders.
txt="Este es un mensaje con 2 datos: {0} {1}"
print(txt.format("A","B"))
print("Este es otro ejemplo: {0} {1}".format("C","D"))

# Relleno

print ("CENTRADO 1".center(40, '#'))

# Es lo mismo que...

texto="EJEMPLO"
print (texto.center(40, '#'))

# Left justification... el texto se pone a la izquierda
print (texto.ljust(40, '-'))

# Right justification... el texto se pone a la derecha
print (texto.rjust(40, '-'))

# Investigación... ¿Cómo se otienen las siguientes salidas en Python?...
n=1234.12

# 1234.12
print(n)
# 1,234.12
print("{:,}".format(n))
# 001,234.12
# ##1,234.12
# $1,234.12
print("${:,}".format(n))
# 001,234.1200

