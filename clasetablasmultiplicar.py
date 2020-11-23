# Elabora una clase llamada TablaMultiplicacion.
# Debe tener una propiedad llamada NumeroBase, que es el número
# a tomar como base para la generación de una tabla de multiplicar.
# Se debe incluir un método llamado GenerarTabla, que se encargue
# de imprimir en consola la tabla del número que se tenga en ese
# momento en la propiedad NumeroBase.

# Declarar la clase.
class TablaMultiplicacion():
    # Declarar la propiedad.
    # Es importante el valor que se asigna, porque le da
    # identidad a la propiedad.
    # Si es str, asignar ""
    # Si es int, asignar 0
    # Si es float, asignar 0.0
    NumeroBase = 0
    # Declaración del método
    def GenerarTabla(self):
        for i in range(1,10):
            print(self.NumeroBase,"x",i,"=",self.NumeroBase*i)

# Instanciar la clase TablaMultiplicar, en un objeto llamado tm
tm = TablaMultiplicacion()
# Asignarle valor a la propiedad NumeroBase del objeto tm
tm.NumeroBase=10
# Ejecutar el método GenerarTabla() del objeto tm
tm.GenerarTabla()

# Cada objeto maneja su juego de valores en propiedades.
obj=TablaMultiplicacion()
obj.NumeroBase=3
obj.GenerarTabla()
# Asignar un valor a una propiedad de otro objeto, no modifica
# los valores de las mismas propiedades en otro objeto.
tm.GenerarTabla()
