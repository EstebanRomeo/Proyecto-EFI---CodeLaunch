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
        print("3. Asignar tareas")
        print("4. Asignar objetivos")
        print("5. Ver postulaciones")
        print("6. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            nombre_proyecto = input("Nombre del proyecto: ")

def menu_usuario(usuario):
    while True:
        print("\n--------- MODO USUARIO ---------------")
        print("1. Ver tareas asignadas")
        print("2. Ver objetivos")
        print("3. Ver proyectos disponibles")
        print("4. Postularse a proyecto")
        print("5. Salir")
        opcion = input("Opción: ")
        if opcion == "5":
            break
