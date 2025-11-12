"""Escriba un programa que calcula el salario neto semanal de un trabajador en función del
número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
• Las primeras 35 horas se pagan a tarifa normal.
• Las horas que pasen de las 35 horas se pagan a 1,5 veces la tarifa normal.
• Las tasas de impuesto son:
o Los primeros 500€ son libres de impuestos.
o Los siguientes 400€ tiene un 25% de impuesto.
o Los restantes un 45% de impuesto.
Escribe el nombre del trabajador, salario bruto, tasas y salario neto."""

nombre = input("Ingrese el nombre del trabajador: ")
horas = float(input("Ingrese el número de horas trabajadas en la semana: "))
tarifa = float(input("Ingrese la tarifa normal por hora (€): "))

if horas <= 35:
    sueldo = horas * tarifa
    
else:
    horas = horas - 35
    sueldo = horas * (1.5 * tarifa) + (35 * tarifa)
    
if sueldo <= 500:
    sueldo_neto = sueldo
    sueldo_bruto = sueldo
else:
    sueldo = sueldo - 500
    if sueldo <= 400:
        impuesto = sueldo * 25/100
        sueldo_neto = (sueldo + 500) - impuesto
        sueldo_bruto = sueldo + 500
    else:
        sueldo = sueldo - 400
        impuesto = (400 * 25/100) + (sueldo * 45/100)
        sueldo_neto = (sueldo + 400) - impuesto
        sueldo_bruto = sueldo + 900
    
print("Nombre del trabajador:", nombre)
print("Salario bruto: " , sueldo_bruto, "€")
print("Salario neto: " , sueldo_neto, "€")