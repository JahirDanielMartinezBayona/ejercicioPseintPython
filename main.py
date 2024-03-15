print("""
PROGRAMA QUE PREGUNTE AL USUARIO LA HORA ACTUAL t 
DEL RELOJ Y UN NÚMERO ENTERO DE HORAS h, 
QUE INDIQUE QUÉ HORA MARCARÁ EL RELOJ DENTRO DE h HORAS
      """)
horaActual = int(input("Hora actual: "))
horaCantidad = int(input("Cantidad de horas: "))
if (int(horaActual) + int(horaCantidad)) > 12:
      resultado = (int(horaActual) + int(horaCantidad)) % 12
else:
      resultado = int(horaActual) + int(horaCantidad)

print("En "+ str(horaCantidad) +" horas, el reloj marcara las "+str(resultado))