from time import localtime
print("""
PROGRAMA QUE SIMULA UNA CALCULADORA BÁSICA, 
ESTE PUEDE REALIZAR OPERACIÓN DE SUMA, RESTA, 
MULTIPLICACIÓN Y DIVISIÓN
""")

operando1 = int(input("Operando: "))
operador = str(input("Operador: "))
operando2 = int(input("Operando: "))

if operador == "+":
    resultado = float(operando1) + float(operando2)
    print(str(operando1)+"+"+str(operando2)+"="+str(resultado))
elif operador == "-":
    resultado = float(operando1) - float(operando2)
    print(str(operando1)+"-"+str(operando2)+"="+str(resultado))
elif operador == "*":
    resultado = float(operando1) * float(operando2)
    print(str(operando1)+"*"+str(operando2)+"="+str(resultado))
elif operador == "/":
    resultado = float(operando1) / float(operando2)
    print(str(operando1)+"/"+str(operando2)+"="+str(resultado))
elif operador == "**":
    resultado = float(operando1) ** float(operando2)
    print(str(operando1)+"**"+str(operando2)+"="+str(resultado))