# Definición de clase
# Una clase que se llame GestionNumerica
# Debe tener dos propiedades, operador1, y operador2
# y debe tener dos métodos, uno que muestre la suma
# de las propiedades, y otro que muestre la multiplicación.

# Los elementos de una clase (propiedades, métodos, eventos) se les
# llama miembros (members). Tanto la clase como los miembros de la clase
# tienen su nombre usando notación PascalCasing (palabras juntas, sin líneas 
# intermedias, donde todas las palabras inician en mayúsculas)

class GestionNumerica():
    # Se generan las propiedades con la simple definición
    # de variables, dentro del alcance del bloque de código de
    # la clase.

    # Primera propiedad
    Operador1 = 0

    # Segunda propiedad
    Operador2 = 0
    # Para declarar métodos, se declaran funciones dentro del alcance
    # del bloque de la clase.

    # Primer método
    def Sumar(self):
        # En los métodos, al menos se especifica un argumento.
        # El primer argumento es self, que indica la referencia
        # que el objeto hace de sí mismo.
        return self.Operador1 + self.Operador2

    # Segundo método
    def Multiplicar(self):
        return self.Operador1 * self.Operador2

    # La clase tiene en total 4 miembros (members)

# Para instanciar una clase en Python, basta con asignarle la clase
# a una variable, que en ese momento se convierte en una variable de 
# objeto.
mi_objeto = GestionNumerica()

# Los miembros son accesibles a través del objeto
# usando dot notation.

mi_objeto.Operador1 = 10
mi_objeto.Operador2 = 5

print(mi_objeto.Operador1)
print(mi_objeto.Operador2)

print(mi_objeto.Sumar())
print(mi_objeto.Multiplicar())

