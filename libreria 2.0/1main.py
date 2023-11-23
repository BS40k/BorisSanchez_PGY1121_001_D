import random
from funciones import *

while True:
    op=mostrar_menu()
    try:
        if op==1:
            agregar_libro()
        elif op==2:
            libros()
        elif op==3:
            imprimir_etiqueta()
        elif op==4:
            print("Gracias por visitar Libro Magico")
            break
        else:
            print("Eliga una opcion valida")
    except ValueError:
        print("El menu funciona solo con NUMEROS")
        