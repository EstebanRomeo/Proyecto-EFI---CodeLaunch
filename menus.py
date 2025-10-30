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
    from funciones import postularse_proyecto
    from modelos import Proyecto

    while True:
        print("\n--------- MODO USUARIO ---------------")
        print("1. Postularse a proyecto")
        print("2. Ver proyectos disponibles")
        print("3. Salir")
        opcion = input("Opcion: ")

        if opcion == "1":
            postularse_proyecto(usuario)
        elif opcion == "2":
            proyectos = Proyecto.cargar_proyectos("proyectos_aprobados.txt")
            if not proyectos:
                print("No hay proyectos disponibles en este momento.")
            else:
                print("\n--- Proyectos disponibles ---")
                for p in proyectos:
                    print(f"- {p.nombre} | Cupo: {p.cupo} | Líder: {p.lider}")
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")