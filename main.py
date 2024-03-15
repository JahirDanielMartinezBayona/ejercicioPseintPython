print("""
PROGRAMA QUE PIDE DOS NÚMEROS ENTEROS Y QUE CALCULE LA DIVISIÓN,
 INDICANDO SI LA DIVISIÓN ES EXACTA O NO
      """)
dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
resultadoCociente = int(dividendo) / int(divisor)
resultadoResto = dividendo % divisor
print("")
if resultadoResto == 0:
      print("La división es exacta")
else:
      print("La división no es exacta")
print("Cociente: " + str(int(resultadoCociente)))
print("Resto: " + str(resultadoResto))
