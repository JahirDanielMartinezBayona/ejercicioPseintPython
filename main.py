print("""
PROGRAMA QUE ENTREGA LA PARTE DECIMAL DE UN NÚMERO REAL INGRESADO POR EL USUARIO
      """)
numero = float(input("Ingresa tu número: "))
if(numero > 0): 
      numeroDecimal = float(numero - int(numero))      
else: 
      numeroDecimal = float(int(numero) - numero)

print("La parte decimal es: "+str(numeroDecimal))