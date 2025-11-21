"""
Programa que lea una secuencia de números no nulos hasta que se introduzca un 0, y luego
muestre si ha leído algún número negativo, cuantos positivos y cuantos negativos.
"""

contador_positivos = 0
contador_negativos = 0

hay_negativo = False
numero = None

while numero != 0:
    numero = int(input("Ingrese un número no nulo: "))  
    if numero > 0:
         contador_positivos += 1
    elif numero < 0:
        hay_negativo = True
        contador_negativos += 1
        


if hay_negativo:
    print("Se ha leído al menos un número negativo.")

print("Números negativos leídos:", contador_negativos)
print("Números positivos leídos:", contador_positivos)
        