from modelos import Proyecto

def lanzar_proyecto():
    proyectos = Proyecto.cargar_proyectos("proyectos.txt") 

    if not proyectos:
        print("No hay proyectos pendientes para lanzar")
        return
    
    print("\nProyectos disponibles para lanzar:")
    for i, p in enumerate(proyectos, start=1):
        print(f"{i}. {p.nombre} (Cupo: {p.cupo}, Líder: {p.lider})")

    try:
        eleccion = int(input("\nSelecciona un proyecto por número: ")) - 1

        if 0 <= eleccion < len(proyectos):
            proyecto = proyectos[eleccion]

            proyecto.guardar_txt("proyectos_aprobados.txt")
            print(f"Proyecto '{proyecto.nombre}' lanzado correctamente")

            proyectos.pop(eleccion)  # elimino de pendientes
            
            with open("proyectos.txt", "w", encoding="utf-8") as f:
                for p in proyectos:
                    p.guardar_txt("proyectos.txt")
        else:
            print("Opcion invalida")
    except ValueError:
        print("Ingresa un numero valido")



def postularse_proyecto(usuario):
    proyectos = Proyecto.cargar_proyectos("proyectos_aprobados.txt")

    if not proyectos:
        print("No hay proyectos disponibles para postularse.")
        return

    print("\nProyectos disponibles:")
    for i, p in enumerate(proyectos, start=1):
        print(f"{i}. {p.nombre} (Cupo: {p.cupo}, Líder: {p.lider})")

    try:
        eleccion = int(input("\nSelecciona un proyecto por numero: ")) - 1

        if 0 <= eleccion < len(proyectos):
            proyecto = proyectos[eleccion]

            # verifica si ya estaba postulado
            try:
                with open("postulaciones.txt", "r", encoding="utf-8") as f: 
                    postulaciones = f.readlines()
                    for linea in postulaciones:
                        if f'Usuario: {usuario} || Proyecto: {proyecto.nombre}' in linea:
                            print(f"Ya estas postulado al proyecto '{proyecto.nombre}'")
                            return
            except FileNotFoundError:
                pass 
            
            if proyecto.cupo > 0:
                proyecto.agregar_usuario(usuario)

                with open("postulaciones.txt", "a", encoding="utf-8") as f:
                    f.write(f'Usuario: {usuario} || Proyecto: {proyecto.nombre}\n')

                print(f"Te postulaste al proyecto '{proyecto.nombre}' correctamente")

                # reescribe proyectos aprobados actualizados
                with open("proyectos_aprobados.txt", "w", encoding="utf-8") as f:
                    for p in proyectos:
                        p.guardar_txt("proyectos_aprobados.txt")
            else:
                print("Este proyecto ya no tiene cupos disponibles.")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Ingresa un numero valido")
