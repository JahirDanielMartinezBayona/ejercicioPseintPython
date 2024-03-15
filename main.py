print("""
PROGRAMA QUE PREGUNTA AL USUARIO LAS NOTAS 
DE LOS DOS PRIMEROS CERTAMEN Y LA NOTA DE LABORATORIO, 
Y MUESTRA LA NOTA QUE NECESITA EL ALUMNO PARA APROBAR 
EL RAMO CON NOTA FINAL 60.
      """)
notaCertamen1 = float(input("Ingrese nota certamen 1: "))
notaCertamen2 = float(input("Ingrese nota certamen 2: "))
notaLabotatorio = float(input("Ingrese nota laboratorio: "))


notaCertamen3 = ((60 - 0.3*notaLabotatorio)/0.7)*3 - notaCertamen1 - notaCertamen2
if notaCertamen3 > 0:
      print("Necesita nota "+str(notaCertamen3)+" en el certamen 3") 

else:
      print("No necesitas nota alta en el certamen 3") 