print("""
PROGRAMA QUE INDIQUE SI UN AÑO ES BISIESTO O NO, 
TENIENDO EN CUENTA CUÁL ERA EL CALENDARIO VIGENTE EN ESE AÑO
      """)
anio = int(input("Ingrese un año: "))
anioBisiesto = anio % 4
if anioBisiesto == 0:
      print(str(anio)+" es bisiesto")
else:
      print(str(anio)+" no es bisiesto")