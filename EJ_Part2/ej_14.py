"""
Crea una aplicación que dibuje una pirámide de asteriscos. Nosotros le pasamos la altura
de la pirámide por teclado. Este es un ejemplo, si introducimos 5 de altura:
"""

altura = int(input("Ingrese la altura de la pirámide: "))
for i in range(1, altura + 1):
    espacios=' ' * (altura - i - 1)
    asteriscos='*' * (2 * i + 1)
    print(espacios + asteriscos)
    