"""
Crea una aplicación que dibuje una pirámide invertida de asteriscos. Nosotros le pasamos
la altura de la pirámide por teclado.
"""

altura = int(input("Ingrese la altura de la pirámide invertida: "))
for i in range(altura):
    espacios=' ' * i
    asteriscos='*' * (2 * (altura - i) - 1)
    print(espacios + asteriscos)