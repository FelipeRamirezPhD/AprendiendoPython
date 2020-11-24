# librería para el soporte de fechas
import datetime
# librería para el soporte de expresiones regulares
import re

# Se declara una clase llamada Persona. No hereda de otra clase, por lo cual,
# se refiere sin paréntesis ni parámetros.
# Esta clase actua como clase base de otras clases.
class Producto:
    def __init__(self, Codigo, Descripcion="", PrecioUnitario=0.00):
        self.Codigo=Codigo
        self.Descripcion=Descripcion
        self.PrecioUnitario=PrecioUnitario
        # propiedad Codigo. Es un código de 6 dígitos.
        # propiedad DEscripción. Es una descripción de máximo 40 caracteres.
        # propiedad PrecioUnitario. Es el precio unitario del producto.

class ProductoImportado(Producto):
    def __init__(self, Codigo, Descripcion, PrecioUnitario, FechaImportacion=datetime.datetime.now(),NumeroPedimento="",EsValido=False):
        super().__init__(Codigo, Descripcion, PrecioUnitario)
        self.FechaImportacion=FechaImportacion
        self.NumeroPedimento=NumeroPedimento
        self.EsValido=EsValido
        # propiedad FechaImportacion. Fecha en que se importó el producto.
        # propiedad NumeroPedimento. Número de 10 dígitos.
        # propiedad EsValido. Boolean. Vedadero su cumple, Falso si no cumple.

    def Validar(self):
        if re.search(r"[0-9]{6}",self.Codigo):
            # r"texto" raw-as is
            self.EsValido=True
        else:
            self.EsValido=False

x=ProductoImportado("123","Primer Producto",100.00)
x.NumeroPedimento="1234567890"
x.Validar()
print(x.Codigo)
print(x.PrecioUnitario)
print(x.NumeroPedimento)
print(x.EsValido)
