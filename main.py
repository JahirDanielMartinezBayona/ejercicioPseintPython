from time import localtime
print("""
PROGRAMA QUE MUESTRA LA TABLA DE MULTIPLICAR DEL 
1 AL 10 DEL NÚMERO INGRESADO POR EL USUARIO
""")

numero = int(input("Ingrese un numero: "))

multiplicador = 1
while(multiplicador <= 10):
    resultado = numero * multiplicador 
    print(f"{numero} * {multiplicador} = {resultado}")
    multiplicador+=1