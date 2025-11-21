# Programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído algún número negativo o no.

contador = 0 
negativo = False

while contador != 100:
    numero = int(input("Ingrese un número no nulo: "))
    if numero < 0:
        negativo = True
    elif numero == 0:
        contador -= 1
        print("El número no debe ser nulo. Intente de nuevo.")

    contador += 1
        

if negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")  