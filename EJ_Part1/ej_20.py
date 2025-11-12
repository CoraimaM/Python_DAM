"""Escriba un programa que lea una calificación numérica entre 0 y 10 y la transforme en la
calificación alfabética, escribiendo el siguiente resultado (switch).
• De 0 a < 3 Muy Deficiente.
• De 3 a < 5 Insuficiente.
• De 5 a < 6 Suficiente.
• De 6 a < 7 Bien.
• De 7 a <9 Notable.
• De 9 a 10 Sobresaliente."""

calificacion = float(input("Ingrese una calificación numérica entre 0 y 10: ")) 
match calificacion:
    case calificacion if 0 <= calificacion < 3:
        print("Calificación alfabética: Muy Deficiente")
    case calificacion if 3 <= calificacion < 5:
        print("Calificación alfabética: Insuficiente")
    case calificacion if 5 <= calificacion < 6:
        print("Calificación alfabética: Suficiente")
    case calificacion if 6 <= calificacion < 7:
        print("Calificación alfabética: Bien")
    case calificacion if 7 <= calificacion < 9:
        print("Calificación alfabética: Notable")
    case calificacion if 9 <= calificacion <= 10:
        print("Calificación alfabética: Sobresaliente")
    case _:
        print("Error: La calificación ingresada no es válida.")