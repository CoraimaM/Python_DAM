# Programa que calcula y escribe la suma y el producto de los 10 primeros números naturales.

suma = 0
producto = 1

for numero in range(1, 11):
    suma += numero
    producto *= numero

print("La suma de los 10 primeros números naturales es:", suma)
print("El producto de los 10 primeros números naturales es:", producto)
