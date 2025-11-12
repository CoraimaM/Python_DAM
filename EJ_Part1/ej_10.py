"""Escriba un programa que lea dos números, calcule y muestre el valor de sus suma, resta,
producto y división (Ten en cuenta la división por cero)."""

print("Dime el primer número:")
num1 = float(input())

print("Dime el segundo número:")
num2 = float(input())

suma = num1 + num2
print("La suma es:", suma)

resta = num1 - num2
print("La resta es:", resta)

producto = num1 * num2
print("El producto es:", producto)

if num2 != 0:
    division = num1 / num2
    print("La división es:", division)
else:
    print("No se puede dividir por cero")
