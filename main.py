from time import localtime
print("""
PROGRAMA QUE PERMITE TRABAJAR 
CON LAS POTENCIAS FRACCIONALES DE DOS
""")
print("""
CABE MENCIONAR QUE 
EL NUMERADOR DEBE SER
MENOR AL DENOMINADOR
PARA QUE EL PROGRAMA FINALICE Y
OPERE CORRECTAMENTE
""")
numerador = 0
denominador = 0

numerador = float(input("Ingrese un numerador: "))
denominador = float(input("Ingrese un denominador: "))

potencia = 1
resultado = 0
suma = 0
print("Potencia    Fracción    Suma")
resultado = (float(numerador)**potencia)/(float(denominador)**potencia)
while(resultado >= 0.000001):
    suma = suma + resultado
    print(f"{potencia}           {resultado}         {suma}")
    resultado = (float(numerador)**potencia)/(float(denominador)**potencia)
    potencia += 1