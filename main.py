import math
radio = input("Ingrese el radio: ")
area = math.pi * float(radio) * float(2)
perimetro = math.pi * float(radio) ** 2
print("Perímetro: " + str(perimetro))
print("Área: " + str(area))