nota_1 = float(input("Ingrese la primera nota: "))
nota_2 = float(input("Ingrese la segunda nota: "))
nota_3 = float(input("Ingrese la tercera nota: "))

suma_notas = nota_1 + nota_2 + nota_3
promedio = suma_notas / 3

if promedio == 5:
    print("Excelente")
elif 4 <= promedio >= 4.9:
    print("Superior")
elif 3 <= promedio >= 3.9:
    print("Basico")
elif 1 <= promedio >= 2.9:
    print("Bajo")
else: print("Bajo")


print (f"EL promedio es de: {promedio}")
