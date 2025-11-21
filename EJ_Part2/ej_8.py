# Programa que lea 100 números no nulos y luego muestre un mensaje indicando cuántos son positivos y cuantos negativos.

contador_positivos = 0
contador_negativos = 0
contador = 0

while contador != 100:
    numero = int(input("Ingrese un número no nulo:"))

    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1
    else:
        contador -= 1
        print("El número no debe ser nulo. Intente de nuevo.")

print("Se han leído", contador_positivos, "números positivos y", contador_negativos, "números negativos.")
