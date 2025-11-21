"""
Programa que calcule el valor A elevado a B (A^B) sin hacer uso del operador de potencia
(^), siendo A y B valores introducidos por teclado, y luego muestre el resultado por pantalla.
"""
A = int(input("Introduce el primer numero: "))
B = int(input("Introduce el segundo numero: "))

resultado = 1

for i in range (B):
    resultado *= A

print(A, "elevado a " ,B, "es: " ,resultado)
    