ingreso_anual = float(input("Ingrese el valor del ingreso anual: "))
calculo_mayor_100 = ingreso_anual * 0.30
calculo_mayor_50 = ingreso_anual * 0.20
calculo_menor_50 = ingreso_anual * 0.10

monto_pagar_100 = ingreso_anual + calculo_mayor_100
monto_pagar_50 = ingreso_anual + calculo_mayor_50
monto_pagar_menos_50 = ingreso_anual + calculo_menor_50


if ingreso_anual >= 100000:
    print (f"EL impuesto sobre la renta es de: {monto_pagar_100}")
elif ingreso_anual > 50000:
    print (f"EL impuesto sobre la renta es de: {monto_pagar_50}")
elif ingreso_anual <= 50000:
    print (f"EL impuesto sobre la renta es de: {monto_pagar_menos_50}")
else: print("")