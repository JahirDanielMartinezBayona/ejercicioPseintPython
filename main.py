from time import localtime
print("""
PROGRAMA QUE ENTREGA LA EDAD DEL USUARIO A PARTIR DE SU FECHA DE NACIMIENTO
      """)
print("Ingrese su fecha de nacimiento.")
localTime = localtime()
diaPersona = int(input("Dia: "))
mesPersona = int(input("Mes: "))
anioPersona = int(input("Año: "))

anio= int(localTime.tm_year) - int(anioPersona)
if mesPersona == localTime.tm_mon and diaPersona == localTime.tm_mday:
    print("Usted tiene "+str(anio)+" años")
else:
    anio2 = int(anio)-int(1)
    print("Usted tiene "+str(anio2)+" años")