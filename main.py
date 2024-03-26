print("""
PROGRAMA QUE PIDE AL USUARIO DOS
NÚMEROS ENTEROS, Y LUEGO ENTREGA 
LA SUMA DE TODOS LOS NÚMEROS 
QUE ESTÁN ENTRE ELLOS
""")

primerNumero = int(input("Ingrese num: "))
segundoNumero = int(input("Ingrese num: "))


global sumaTotal
if(primerNumero > segundoNumero):
    sumaTotal = 0
    segundoNumero += 1
    while segundoNumero < primerNumero:
        sumaTotal = int(sumaTotal) + int(segundoNumero)
        segundoNumero += 1

elif(segundoNumero > primerNumero):
    sumaTotal = 0
    primerNumero += 1
    while primerNumero < segundoNumero:
        sumaTotal = int(sumaTotal) + int(primerNumero)
        primerNumero += 1

elif(segundoNumero == primerNumero):
    sumaTotal = 0

print("La suma es "+str(sumaTotal))