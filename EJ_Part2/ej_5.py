"""
Programa que muestre en líneas separadas lo siguiente:
ZYWXVUTSRQPONMLKJIHGFEDCBA, YWXVUTSRQPONMLKJIHGFEDCBA,
WXVUTSRQPONMLKJIHGFEDCBA, ...., DCBA, CBA, BA, A.
"""

cadena = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
for i in range(len(cadena)):
    print(cadena[i:])