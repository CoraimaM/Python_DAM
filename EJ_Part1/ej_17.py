"""Escriba un programa que simule un inicio de sesión solicitando el nombre de usuario y
contraseña, y mostrar un mensaje en pantalla, inicio de sesión correcto/ nombre de usuario
incorrecto"""

usuario = "Seiry"
contraseña = "12345"
entrar=False
entrar2=False

usuaruio = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")

if usuaruio == usuario:
    entrar=True
else:
    print("Nombre de usuario incorrecto.")

if contraseña == contraseña:
    entrar2=True
else:
    print("Contraseña incorrecta.")
    
if entrar and entrar2:
    print("Inicio de sesión correcto.")

