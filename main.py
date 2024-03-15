from time import localtime
print("""
PROGRAMA QUE RECIBE COMO ENTRADA LA ESTATURA, 
EL PESO Y LA EDAD DE UNA PERSONA, 
Y LE ENTREGA SU CONDICIÓN DE RIESGO
""")

estatura = float(input("Estatura (metros): "))
peso = float(input("Peso (kilogramo): "))
edad = int(input("Edad: "))

IMC = peso/((estatura)**2)

if IMC < 22 and edad <45:
    print(" RIESGO DE ENFERMEDADES CORONARIAS (Pronóstico): BAJO")
elif IMC < 22 and edad >= 45:
    print(" RIESGO DE ENFERMEDADES CORONARIAS (Pronóstico): MEDIO")
elif IMC >= 22 and edad < 45:
    print(" RIESGO DE ENFERMEDADES CORONARIAS (Pronóstico): MEDIO")    
elif IMC >= 22 and edad >= 45:
    print(" RIESGO DE ENFERMEDADES CORONARIAS (Pronóstico): ALTO")