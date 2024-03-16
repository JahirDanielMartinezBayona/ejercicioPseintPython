from time import localtime
print("""
PROGRAMA QUE ENTREGA TODOS LOS DIVISORES 
DEL NÚMERO ENTERO INGRESADO
""")

numero = int(input("Ingrese numero: "))

divisor = 1
listaDivisores = []
resultado = ""
while divisor <= numero:
    
    resultado = numero % divisor
    if resultado == 0:
        listaDivisores.append(divisor)
    divisor+=1

for variableDivisor in listaDivisores:
    resultado = str(resultado) + " "+ str(variableDivisor)
print(resultado)