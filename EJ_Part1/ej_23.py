"""Una farmacia desea un programa para ingresar el valor de compra y calcular lo siguiente: si
el pago se efectúa al “contado”, calcular un descuento del 5%; pero si el pago es con “tarjeta”
se incrementa un recargo del 3% al valor de compra. Calcular y visualizar el descuento o recargo
según sea el caso y el total a pagar de la compra"""

print("Ingrese el valor de compra:")
valor_compra = float(input())
print("Ingrese el método de pago (contado/tarjeta):")
metodo_pago = input().lower()
if metodo_pago == "contado":
    descuento = valor_compra * 5 / 100
    total_a_pagar = valor_compra - descuento
    print("La cuenta a pagar es de:", total_a_pagar)
    
elif metodo_pago == "tarjeta":
    recargo = valor_compra * 3 / 100
    total_a_pagar = valor_compra + recargo
    print("La cuenta a pagar es de:", total_a_pagar)
    
else:
    print("Método de pago no válido.")