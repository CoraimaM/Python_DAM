"""
Programa que suma independientemente los pares y los impares de los números
comprendidos entre 100 y 200, y luego muestra por pantalla ambas sumas.
"""

cont_pares = 0
cont_impares = 0

for numero in range (100, 200+1):
    if numero % 2 == 0:
        cont_pares += numero
    else:
        cont_impares += numero

print("la suma de los numero pares es: " ,cont_pares)
print("la suma de los numero impares es: " ,cont_impares)


