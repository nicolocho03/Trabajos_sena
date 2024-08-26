cantidad = float(input("Ingrese la cantidad de productos: "))
precio_unitario = float(input("Ingrese el valor unitario del producto: "))

total_sin_descuento = cantidad * precio_unitario

if cantidad >= 10:
    descuento = 0.20
elif 5 <= cantidad <= 9:
    descuento = 0.10
else: 
    descuento = 0.0

total_con_descuento = total_sin_descuento * (1-descuento)

print(f"Total sin descuento ${total_sin_descuento:.2f}")
print(f"Descuento aplicado {descuento * 100}%")
print(f"Total a pagar con descuento ${total_con_descuento:.2f}")

