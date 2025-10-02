from modelos import Proyecto
from modelos import Usuario

def subir_proyecto():
    print("--------------Datos del nuevo proyecto-------------------------")
    nombre_proyecto = input("Nombre del proyecto: ")
    descripcion_proyecto = input("Descripcion del proyecto: ")
    cant_integrantes = int(input("Cantindad maxima de integrantes: "))
    lider = input("Nombre del lider: ")
    

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
            print("Opción invalida")
    except ValueError:  #Lo puse para que no se rompa cuando ponga alguna otra cosa, pero como el viejo es medio medio hay que ver si lo podemos usar
        print("Ingresa un número valido")



def postularse_proyecto(usuario):
    proyectos = Proyecto.cargar_proyectos("proyectos_aprobados.txt")

    if not proyectos:
        print("No hay proyectos disponibles para postularse.")
        return

    print("\nProyectos disponibles:")
    for i, p in enumerate(proyectos, start=1):
        print(f"{i}. {p.nombre} (Cupo: {p.cupo}, Líder: {p.lider})")

    try:
        eleccion = int(input("\nSelecciona un proyecto por número: ")) - 1

        if 0 <= eleccion < len(proyectos):
            proyecto = proyectos[eleccion]

            try:
                with open("postulaciones.txt", "r", encoding="utf-8") as f: 
                    postulaciones = f.readlines()
                    for linea in postulaciones: #Lee del archivo las lineas, y si aparece el nombre del usuario no le permite postularse
                        if f'Usuario: {usuario} || Proyecto: {proyecto.nombre}' in linea:
                            print(f"Ya estas postulado al proyecto '{proyecto.nombre}'")
                            return
            except FileNotFoundError:
                pass 
            
            if proyecto.cupo > 0:
                proyecto.cupo -= 1

                if not hasattr(proyecto, "integrantes"):
                    proyecto.integrantes = []

                proyecto.usuarios.append(usuario)
                
                with open("postulaciones.txt", "a", encoding="utf-8") as f:
                    f.write(f'Usuario: {usuario} || Proyecto: {proyecto.nombre}\n')

                print(f"Te postulaste al proyecto '{proyecto.nombre}' correctamente.")

                # Reescribir el archivo con todos los proyectos actualizados
                with open("proyectos_aprobados.txt", "w", encoding="utf-8") as f:
                    for p in proyectos:
                        p.guardar_txt("proyectos_aprobados.txt")  

            else:
                print("Este proyecto ya no tiene cupos disponibles.")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Ingresa un número válido.")
