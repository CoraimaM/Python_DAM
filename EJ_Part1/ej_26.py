"""En un casino de juegos se desea mostrar los mensajes respectivos por el puntaje obtenido
en el lanzamiento de tres dados de un cliente, de acuerdo a los siguientes resultados:
Si los tres dados son seis, mostrar el mensaje “Excelente”
Si dos dados se obtienen seis, mostrar el mensaje “Muy bien”
Si un dado se obtiene seis, mostrar el mensaje “Regular”
Si ningún dado se obtiene seis, mostrar el mensaje “Pésimo”
(Use el control switch)."""

print("Ingrese el puntaje de los tres dados:")
dado1 = int(input("Dado 1: "))
dado2 = int(input("Dado 2: "))
dado3 = int(input("Dado 3: "))

match (dado1, dado2, dado3):
    case (6, 6, 6):
        print("Excelente")
    case (6, 6, _ ) | (6, _, 6) | (_, 6, 6):
        print("Muy bien")
    case (6, _, _) | (_, 6, _) | (_, _, 6):
        print("Regular")
    case (_, _, _):
        print("Pésimo")
    case _:
        print("Error en la entrada de datos.")

    