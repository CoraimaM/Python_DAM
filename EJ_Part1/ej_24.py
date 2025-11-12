"""Tiendas Don Pepe desea un programa para ingresar por teclado el monto de compra y el día
de la semana; si el día es martes o jueves, se realizará un descuento del 15% por la compra.
Visualizar el descuento y el total a pagar por la compra."""

print("Ingrese la suma de la compra:")
suma_compra = float(input())
print("Ingrese el día de la semana:")
dia_semana = input().lower()

if dia_semana == "martes" or dia_semana == "jueves":
    descuento = suma_compra * 15 / 100
    total_a_pagar = suma_compra - descuento
    print("La cuenta a pagar es de:", total_a_pagar)
else:
    print("La cuenta a pagar es de:", suma_compra)
    