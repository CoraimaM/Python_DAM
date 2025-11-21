# Programa que lea un número positivo N y calcule y visualice su factorial N! Siendo el factorial

print ("Dame un número positivo para calcular su factorial")
N = int(input())
factorial = 1

if N == 1 or N == 0:
    print ("El factorial de", N, "es 1")

for i in range(1, N + 1):
    factorial *= i
    
print("El factorial de", N, "es" , factorial)
    
    

    