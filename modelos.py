class Proyecto:  
    def __init__(self, nombre, descripcion, objetivos, duracion, cupo, lider=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.duracion = duracion
        self.cupo = cupo
        self.tareas = []
        self.usuarios = []
        self.lider = lider

    
    def guardar_txt(self, archivo="proyectos.txt"):
        with open(archivo, "a", encoding="utf-8") as f:
            f.write("----------- Proyecto -----------\n")
            f.write(f"Nombre: {self.nombre}\n")
            f.write(f"Descripcion: {self.descripcion}\n")
            f.write(f"Objetivos: {self.objetivos}\n")
            f.write(f"Duracion: {self.duracion}\n")
            f.write(f"Cupo: {self.cupo}\n")
            f.write(f"Lider: {self.lider}\n")
            f.write("-------------------------------\n\n")

    @classmethod
    def crear_proyecto(cls, usuario):
        print("\n----------------- Datos del nuevo proyecto ----------------")
        nombre = input("Nombre del proyecto: ")
        descripcion = input("Descripcion del proyecto: ")
        objetivos = input("Objetivos del proyecto: ")
        duracion = input("Duracion estimada: ")
        cupo = int(input("Cantidad maxima de integrantes: "))

        proyecto = cls(nombre, descripcion, objetivos, duracion, cupo, lider=usuario)
        proyecto.guardar_txt()
        print(f"Proyecto '{proyecto.nombre}' guardado en proyectos.txt")
        return proyecto


    @classmethod
    def cargar_proyectos(cls, archivo="proyectos.txt"):
        proyectos = []
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = f.read().strip().split("-------------------------------")
                for bloque in contenido:
                    if bloque.strip():
                        lineas = bloque.strip().split("\n")
                        datos = {}
                        for linea in lineas:
                            if ":" in linea:
                                key, value = linea.split(":", 1)
                                datos[key.strip()] = value.strip()
                        proyecto = cls(
                            nombre=datos.get("Nombre"),
                            descripcion=datos.get("Descripción"),
                            objetivos=datos.get("Objetivos"),
                            duracion=datos.get("Duración"),
                            cupo=int(datos.get("Cupo", 0)),
                            lider=datos.get("Líder")
                        )
                        proyectos.append(proyecto)
        except FileNotFoundError:
            pass
        return proyectos
