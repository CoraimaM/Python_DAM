"""Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
con el siguiente menú de opciones:
Bienvenido a su Cajero Virtual
1. Ingresar dinero en cuenta
2. Retirar dinero de la cuenta
3. Salir"""



saldo = 1000
while True:
    print("\nBienvenido a su Cajero Virtual")
    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        ingreso = float(input("¿Cuánto dinero desea ingresar?"))
        saldo = saldo + ingreso
        print("Has ingresado:", ingreso, "euros. Tu saldo actual es:", saldo, "euros.")
        
    elif opcion == "2":
        retirar = float(input("¿Cuánto dinero desea retirar?"))
        if retirar > saldo:
            print("No tienes suficiente saldo para retirar esa cantidad.")
        else:
            saldo = saldo - retirar
            print("Has retirado:", retirar, "euros. Tu saldo actual es:", saldo, "euros.")    
            
    elif opcion == "3":
        print("Gracias por usar el Cajero Virtual. ¡Hasta luego!")
    else:
        print("Error: Opción no válida.")