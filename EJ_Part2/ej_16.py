"""
Programa que lee una secuencia de notas (con valores que van de 0 a 10) que termina con
el valor -1 y nos dice si hubo o no alguna nota con valor 10.
"""
contador_diez = 0
notas = None
hay_diez = False

while notas !=-1:
    notas = int(input("Introduzca la nota: "))
    if notas == 10:
        hay_diez = True
        contador_diez += 1

if hay_diez:
    print("Hay", contador_diez, "dieces en total")
        




