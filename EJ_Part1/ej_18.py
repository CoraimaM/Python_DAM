# Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de 10.

numero = int(input("Por favor, ingrese un número: "))

if numero % 10 == 0:
    print("El número" ,numero, "es múltiplo de 10.")
else:
    print("El número" ,numero, "no es múltiplo de 10.")
    