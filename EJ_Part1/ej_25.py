"""La universidad ha categorizado las matrículas de acuerdo a la facultad que va a estudiar el
postulante. Ingrese por teclado el nombre del postulante y la facultad que va a estudiar, muestre
el importe, la mensualidad, el IGV 18% (importe + mensualidad) y el monto final a pagar. (Use el
control switch)."""

nombre = input("Ingrese el nombre del postulante: ")

while True:
    print("Elija la facultad a la que va a postular:")
    print("1. Ingeniería de Sistemas")
    print("2. Derecho")
    print("3. Ingeniería Naviera")
    print("4.Ingeniería Pesquera")
    print("5.Contabilidad")
    print("6.Administración")
    print("7.Salir")
    opcion = input("Seleccione una opción (1-7): ")
    
    
    match opcion:
        case "1":
            igv=(350 + 650) * 0.18
            suma_final=350 + 650 + igv
            print("Nombre del postulante:", nombre)
            print("Facultad: Ingeniería de Sistemas")
            print("Importe: 350 €")
            print("Mensualidad: 650 €")
            print("IGV (18%):", igv, "€")
            print("Suma final a pagar:", suma_final, "€")
            break
        
        case "2":
            igv=(300 + 550) * 0.18
            suma_final=300 + 550 + igv
            print("Nombre del postulante:", nombre)
            print("Facultad: Derecho")
            print("Importe: 300 €")
            print("Mensualidad: 550 €")
            print("IGV (18%):", igv, "€")
            print("Suma final a pagar:", suma_final, "€")
            break
        
        case "3":
            igv=(300 + 500) * 0.18
            suma_final=300 + 500 + igv
            print("Nombre del postulante:", nombre)
            print("Facultad: Ingeniería Naviera")
            print("Importe: 300 €")
            print("Mensualidad: 500 €")
            print("IGV (18%):", igv, "€")
            print("Suma final a pagar:", suma_final, "€")
            break
        
        case "4":
            igv=(310 + 460) * 0.18
            suma_final=310 + 460 + igv
            print("Nombre del postulante:", nombre)
            print("Facultad: Ingeniería Pesquera")
            print("Importe: 310 €")
            print("Mensualidad: 460 €")
            print("IGV (18%):", igv, "€")
            print("Suma final a pagar:", suma_final, "€")
            break
        
        case "5":
            igv=(280 + 490) * 0.18
            suma_final=280 + 490 + igv
            print("Nombre del postulante:", nombre)
            print("Facultad: Contabilidad")
            print("Importe: 280 €")
            print("Mensualidad: 490 €")
            print("IGV (18%):", igv, "€")
            print("Suma final a pagar:", suma_final, "€")
            break
        
        case "6":
            igv=(360 + 520) * 0.18
            suma_final=360 + 520 + igv
            print("Nombre del postulante:", nombre)
            print("Facultad: Administración")
            print("Importe: 360 €")
            print("Mensualidad: 520 €")
            print("IGV (18%):", igv, "€")
            print("Suma final a pagar:", suma_final, "€")
            break
        
        case "7":
            print("Saliendo del programa.")
            break
        
        case _:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
        