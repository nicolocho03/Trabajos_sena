total_compra = float(input("Ingrese el valor total de la compra: "))

if total_compra >= 100:
    descuento = total_compra * 0.10
    total_a_pagar = total_compra - descuento
    print("Se aplica el descuento del 10%")
else: 
    total_a_pagar = total_compra
    print("No se aplica el descuento")

print(f"El total a pagar despues del descuento es de: ${total_a_pagar:.2f}")