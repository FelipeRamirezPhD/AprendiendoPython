# Pregunta diferentes tipos de datos, sin validación.

# Importa el módulo requerido para usar datos de tipo Date.
import datetime
# Los datos se tienen, se preguntan o se calculan.
# y pueden ser de diferente tipo.
# Notación húngara utilizada:
#   str   string
#   i     int
#   f     float
#   dt    date


def main():
 # Los datos string se preguntan y procesan sin intermediación.
 strDato = input("Dame un dato string: ")
 # Los datos numéricos se preguntan por intermediación.
 _iDato = input("Dame un dato entero: ")
 iDato = int(_iDato)
 _fDato = input("Dame un dato float: ")
 fDato =float(_fDato)
 # Los datos date se preguntan por intermediación.
 _dtDato = input("Dame una fecha yyyy/mm/dd: ")
 # [n,m] Extrae de la posición n a la posición m,sin incluir m.
 # [-m:] Extrae desde la posición m, de atrás para adelante, hasta el final.

 anio=_dtDato[0:4]
 mes=_dtDato[5:7]
 dia=_dtDato[-2:]
 print(anio)
 print(mes)
 print(dia)

 dtDato = datetime.datetime(int(anio), int(mes), int(dia))

 print(strDato)
 print(type(strDato))
 print(iDato)
 print(type(iDato))
 print(fDato)
 print(type(fDato))
 print(dtDato)
 print(type(dtDato))
 
