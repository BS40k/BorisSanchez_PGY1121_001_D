import random
import os
list_libro=[]
list_autor=[]
list_genero=[]
list_precios=[]
list_paginas=[]
list_etiquetas=[]

def mostrar_menu():
    print("Bienvenido a Libro Mágico")
    print("-------------------------")
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Imprimir etiquetas")
    print("4. Salir")
    print("-------------------------")
    opcion=int(input("Seleccione una opcion"))
    return opcion
mostrar_menu()

def agregar_libro():
        lib1=0
        while lib1==0:
                try:
                        libro=(input("¿Como se llama el libro que va a agregar?"))
                        len(libro)
                        if len(libro)<15 or len(libro)>50:
                                print("El nombre del libro debe tener mas de 15 y menos de 50 caracteres ")
                                lib1=0
                        else:
                                list_libro.append(libro)
                                print("El libro se agrego exitosamente")
                                break
                except ValueError:
                        print("NO se admite numeros en el nombre del libro ")
                        lib1=0
        else:
                lib11=0
                while lib11==0:
                        try:
                                libro_precio=int(input("¿Cual es el precio del libro?"))
                                if libro_precio<4500:
                                        print("El libro debe de costar MAS QUE $4500")
                                        lib11=0
                                else:
                                        list_precios.append(libro_precio)
                                        print("El precio se fijo exitosamente")
                                        break
                        except ValueError:
                                print("NO se admiten letras en el precio")
                                lib11=0
                        lib12=0
                        while lib12==0:
                                try:
                                        autor=(input("¿Quien es el autor?"))
                                        if len(autor)<=1:
                                                print("Este campo no puede estar VACIO")
                                        else:
                                                print("Autor registrado")
                                                list_autor.append(autor)
                                                break
                                except ValueError:
                                        print("no se admite numeros para determinar un nombre de autor")
                lib112=0
                while lib112==0:
                        try:
                                genero=(input("Ingrese el genero del libro"))
                                if  len(genero)<=1:
                                        print("Este campo no puede estar VACIO")
                                        lib112=0
                                else:
                                        print("Genero del libro registrado")
                                        list_genero.append(genero)                                        
                                        lib112=1
                        except ValueError:
                                print("NO se admite numeros en el genero del libro")
                                lib112=0
                lib212=0
                while lib212==0:
                        try:
                                paginas=int(input("Ingrese el numero de paginas del libro"))
                                if paginas<=1:
                                        print("Este campo no puede estar VACIO")
                                        lib212=0
                                else:
                                        os.system("cls")
                                        print("Numero de paginas resgistrado")
                                        print("Registro de libro exitoso")
                                        list_paginas.append(paginas)
                                        etiquetas=random.randint(10000,99999)
                                        list_etiquetas.append(etiquetas)
                                        break
                        except ValueError:
                                print("NO se admiten letras en el numero de paginas")
                                lib212=0
agregar_libro()

def libros():
        os.system("cls")
        if (list_libro,list_autor,list_genero,list_precios,list_paginas)==0:
                print("No hay libros registrados")
        else:
                print("-------------------------------------------------")
                print("Nombre\t   autor\t   genero\t   precio\t   numero de paginas")
                return(print(f'{list_libro},{list_autor},{list_genero},{list_precios},{list_paginas}'))
libros()

def imprimir_etiqueta():
        os.system("cls")
        if (list_libro,list_autor,list_genero,list_precios,list_paginas,list_etiquetas)==0:
                print("No hay libros registrados")
        else:
                print("-------------------------------------------------")
                print("Nombre\tautor\tgenero\tprecio\tnumero de paginas\tetiquetas")
                return(print(list_libro,list_autor,list_genero, list_precios, list_paginas,list_etiquetas))
imprimir_etiqueta()
