# Escriba un programa que dado el precio de un artículo y el precio de venta real nos muestre el porcentaje de descuento realizado.
print("Dime el precio del producto:") 
precio = float(input()) 

print("Dime el precio de venta real")
precio_venta = float(input())

descuento = ((precio - precio_venta) / precio) * 100
print("El descuento aplicado es de:", descuento, "%")   