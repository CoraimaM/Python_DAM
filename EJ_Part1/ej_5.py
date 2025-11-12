"""Escriba un programa que toma como dato de entrada un número que corresponde a la longitud de un radio 
(La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la esfera
que corresponde con dicho radio."""
import math

print("Introduce la longitud del radio:")
radio = int(input())

diametro = radio * 2
longitud_circunferencia = math.pi * diametro
print("La longitud de la circunferencia es:", longitud_circunferencia)
area_circulo = math.pi * (radio ** 2)
print("El área del círculo es:", area_circulo)
volumen_esfera = (4/3) * math.pi * (radio ** 3)
print("El volumen de la esfera es:", volumen_esfera)
0