from modelos import Proyecto
from funciones import lanzar_proyecto, postularse_proyecto

def mostrar_menu():
    print("\n------------- Bienvenido a CodeLaunch -------------")
    print("1. Registrar nuevo miembro")
    print("2. Iniciar sesión")
    print("3. Salir")

def menu_admin(usuario):
    while True:
        print("\n------------ MODO ADMIN -------------")
        print("1. Subir proyecto")
        print("2. Lanzar proyecto")
        print("3. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            Proyecto.crear_proyecto(usuario)
        elif opcion == "2":
            lanzar_proyecto()
        elif opcion == "3":
            break


def menu_usuario(usuario):
    while True:
        print("\n--------- MODO USUARIO ---------------")
        print("1. Postularse a proyecto")
        print("2. Salir")
        opcion = input("Opcion: ")
        if opcion == "1":
            postularse_proyecto(usuario)
        elif opcion == "2":
            break
