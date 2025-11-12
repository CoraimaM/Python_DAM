# Escriba un programa que pida la edad por teclado y nos muestra el mensaje de “Eres mayor de edad”, si y solamente si lo somos.

print("¿Cual es tu edad?")
edads = int(input())

if edads >= 18:
    print("Eres mayor de edad")

else:
    print("Eres menor de edad")
    
