from modelos import Proyecto


def lanzar_proyecto():
    proyectos = Proyecto.cargar_proyectos("proyectos.txt") 

    
    if not proyectos: #Si no hay proyectos muestra un mensaje y termina la vaina
        print("No hay proyectos pendientes para lanzar")
        return
    
    print("\nProyectos disponibles para lanzar:") #Muestra los proyectos disponibles
    for i, p in enumerate(proyectos, start=1):
        print(f"{i}. {p.nombre} (Cupo: {p.cupo}, Líder: {p.lider})")

    try:
        eleccion = int(input("\nSelecciona un proyecto por número: ")) - 1 #Pide que elija un proyecto para lanzar

        if 0 <= eleccion < len(proyectos):
            proyecto = proyectos[eleccion]

            proyecto.guardar_txt("proyectos_aprobados.txt") #Guarda el proyecto elegido en el archivo de proyectos aprobados
            print(f"Proyecto '{proyecto.nombre}' lanzado correctamente")

            proyectos.pop(eleccion) #Elimina el proyecto de proyectos.txt
            
            with open("proyectos.txt", "w", encoding="utf-8") as f: #Reescribe el archivo proyectos.txt sin el proyecto lanzado
                for p in proyectos:
                    p.guardar_txt("proyectos.txt")
        else:
            print("Opción inválida.")
    except ValueError:  #Lo puse para que no se rompa cuando ponga alguna otra cosa, pero como el viejo es medio medio hay que ver si lo podemos usar
        print("Ingresa un número valido")




def mostrar_menu():
    print("\n------------- Bienvenido a CodeLaunch -------------")
    print("1. Registrar nuevo miembro")
    print("2. Iniciar sesión")
    print("3. Salir")

def menu_admin(usuario):
    while True:
        print("\n------------ MODO ADMIN -------------")
        print("1. Subir proyecto") #Ya esta listo
        print("2. Lanzar proyecto") #Tambien diria que esta listo
        print("3. Asignar tareas") #Diria de sacarlo, no le veo mucho sentido
        print("4. Asignar objetivos")#No se como encararlo, si asignar a los usuarios o proyectos
        print("5. Ver postulaciones")#Falta
        print("6. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            Proyecto.crear_proyecto(usuario)
        elif opcion == "2":
            lanzar_proyecto()

def menu_usuario(usuario):
    while True:
        print("\n--------- MODO USUARIO ---------------")
        print("1. Ver tareas asignadas")#Falta
        print("2. Ver objetivos")#Falta
        print("3. Ver proyectos disponibles")#Falta
        print("4. Postularse a proyecto")#Falta
        print("5. Salir")
        opcion = input("Opción: ")
        if opcion == "5":
            break
