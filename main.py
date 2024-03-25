from time import localtime
print("""
PROGRAMA QUE PERMITE INGRESAR 
LOS TIEMPOS DE VIAJE DE LOS TRAMOS 
Y ENTREGUA COMO RESULTADO EL TIEMPO 
TOTAL DE VIAJE EN FORMATO HORAS:MINUTOS.

""")

resultado = 0
while True:
    duracionTramo = input("Duración tramo: ")
    resultado = int(resultado) + int(duracionTramo)
    if int(duracionTramo) == 0:
        global horas
        global minutos
        horas = int(resultado) / 60
        minutos = resultado % 60
        break

print(f"Tiempo total de viaje: {int(horas)}:{minutos}")