""" Escriba un programa que recibe como datos de entrada una hora expresada en horas,
minutos y segundos que nos calcula y escribe la hora, minutos y segundos que serán,
transcurrido un segundo"""

horas = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))
segundos += 1
if segundos == 60:
    segundos = 0
    minutos += 1
    if minutos == 60:
        minutos = 0
        horas += 1
        if horas == 24:
            horas = 0

print("Hora:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)