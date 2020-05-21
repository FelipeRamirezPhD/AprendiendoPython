# Un colegio tiene programado un pago para el dia 
# 15 de febrero de 2020. Si el pago es realizado
# despues de la fecha, se cobran $8 pesos por cada 
# dia transcurrido. El pago es por $5,500.00.

# Modulo que permite trabajar regular expressions
import re
# Modulo que permite trabajar con datos fecha
import datetime

# Funcion que recibe argumentos y retorna valores.
# esFecha(fechaentexto) donde fechaentexto es YYYY/MM/DD.
# Retorna True si la fecha es valida, y False si no.
def esFecha(expFecha):
    # Manejo estructurado de excepciones.
    try:
        # Extrae el año, mes y día del valor proporcionado
        anio=int(expFecha[0:4])
        mes=int(expFecha[5:7])
        dia=int(expFecha[-2:])
        # Intenta generar una fecha a partir del
        # anio mes y dia proporcionados.
        datetime.date(anio,mes,dia)
    except ValueError:
        # Si se provoca un error, el programa pasa el
        # control a este bloque.
        return False
    
    # Si no hubo error, se retorna True
    return True

# Funcion que convierte una cadena YYYY/MM/DD a su valor
# equivalente datetime.
def strtodate(expFecha):
        anio=int(expFecha[0:4])
        mes=int(expFecha[5:7])
        dia=int(expFecha[-2:])
        return datetime.date(anio,mes,dia)

def main():
    # Se establece el valor del pago.
    colegiatura=5500.00
    # Declaro variable de trabajo para capturar la fecha real de pago
    _fechapago=""
    # Inicializo una variable para que contenga la fecha compromiso
    # de pago.
    fechacomprimiso=strtodate("2020/02/15")
    # Ciclo infinito, que no deja de preguntar la fecha sino hasta
    # que es una fecha valida.
    while True:
        _fechapago=input("Cuándo hiciste el pago YYYY/MM/DD: ")
        if re.search("^[0-9]{4}/[0-9]{2}/[0-9]{2}$", _fechapago):
            if esFecha(_fechapago):
                fechapago=strtodate(_fechapago)
                break
            else:
                print("No es una fecha calendario valida.")
        else:
            print("El formato no es YYYY/MM/DD")

    cargodiario=8.00
    # Cuando hacemos una operacion con fechas, se obtiene lo que se 
    # conoce como "datetime delta" que es un periodo de tiempo
    # como podria ser x minutos, x horas o dias. NO es un numero.
    # En este caso diferencia es el datetime delta que indica
    # la diferencia en tiempo de la fecha compromiso y la fecha real
    diferencia=fechapago-fechacomprimiso
    pagofinal=0.00
    # Si la diferencia en tiempo, expresada en terminos de dias, es
    # mayor a 0, quiere decir que se pago fuera de tiempo y hay recargo.
    if diferencia.days>0:
        # Colegiatura mas los dias de desfase por el costo diario
        pagofinal=colegiatura+(diferencia.days*cargodiario)
    else:
        # Si no hay diferencia, se paga lo que es
        pagofinal=colegiatura

    #txt = "Pago ${:0,.0f}"
    #print(txt.format(pagofinal))

    print("Pago ${:0,.2f}".format(pagofinal))
