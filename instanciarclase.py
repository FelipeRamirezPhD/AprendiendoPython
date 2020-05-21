# Comprueba la importación de una clase, y su uso.

# Se pide importar la clase Contacto, que está definida en definirclase.py
from definirclase import Contacto

# Función que recibe un objeto de tipo Contacto, y muestra sus valores.
def MostrarContenido(objeto):
 print(objeto.telefono)
 print(objeto.nombre)
 print(objeto.correo)
 print(objeto.registro)

 # Se genera una instancia de la clase.
primercontacto=Contacto(1234567890,"Felipe Ramírez","ramirez123@hotmail.com")
MostrarContenido(primercontacto)