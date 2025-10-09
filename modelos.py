class Usuario:
    def __init__(self, nombre, apellido, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol
        self.historial = [] # Tareas completadas
    
    def get_usuario(self):
        return self.nombre
        
    def ver_proyectos(self,plataforma): # Ver proyectos
        for proyecto in plataforma.proyectos:
            print(f'- {proyecto.nombre} - N° de tareas: {len(proyecto.tareas)}')
            
    def postularse(self, proyecto): # Postularse a un proyecto
        if proyecto.tiene_cupo():
            proyecto.usuarios.append(self)
            print(f'{self.nombre} se unió al proyecto "{proyecto.nombre}".')
        else:
            print(f'No hay cupos disponibles en este proyecto.')

    def tomar_tarea(self, tarea):  # Tomar una tarea
        if tarea.usuario_asignado is None:  # Si no se le asigno a nadie
            tarea.usuario_asignado = self  # Se le asigna
            tarea.estado = "En progreso..."
            print(f'{self.nombre} tomó la tarea: {tarea.nombre}')
        else:
            print(f'La tarea "{tarea.nombre}" ya está asignada.')
    
    def completar_tarea(self, tarea): #Completar una tarea
        if tarea.usuario_asignado == self: #Si fue asignada a alguien
            tarea.estado = "completada"
            self.historial.append(tarea) #Se agrega a la lista historial, donde van las tareas completadas
            print(f'{self.nombre} completó la tarea: {tarea.nombre}')
        else:
            print('No podés completar esta tarea.')
            
    def generar_historial(self): # Con with se cierra solo el archivo.
        with open(f'{self.nombre}_historial.txt',"w") as f: #Abre y escribe en un archivo, si el archivo existe, lo sobrescribe, sino lo crea de nuevo.
            for tarea in self.historial:
                f.write(f'{tarea.nombre} - {tarea.estado}\n')
        print(f'Historial guardado en {self.nombre}_historial.txt')





class Proyecto:  
    def __init__(self, nombre, descripcion, objetivos, duracion, cupo: int, lider=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.duracion = duracion
        self.usuarios = []      
        self.cupo = int(cupo)
        self.lider = lider

    
    def guardar_txt(self, archivo="proyectos.txt"): 
        with open(archivo, "a", encoding="utf-8") as f:
            f.write("----------- Proyecto -----------\n")
            f.write(f"Nombre: {self.nombre}\n")
            f.write(f"Descripcion: {self.descripcion}\n")
            f.write(f"Objetivos: {self.objetivos}\n")
            f.write(f"Duracion: {self.duracion}\n")
            f.write(f"Integrantes: {','.join(self.usuarios)}\n") #guarda usuarios como string
            f.write(f"Cupo: {self.cupo}\n")
            f.write(f"Lider: {self.lider}\n")
            f.write("-------------------------------\n\n")
    
    def agregar_usuario(self, usuario): 
        if self.cupo > 0:
            self.usuarios.append(usuario)
            self.cupo -= 1
            print(f'{usuario} se unió al proyecto "{self.nombre}".')
        else:
            print(f'No hay cupos disponibles en este proyecto')

    def mostrar_estado(self): 
        print(f'\nProyecto: "{self.nombre}"')
        print(f'Descripción: {self.descripcion}')
        print(f'Objetivos: {self.objetivos}')
        print(f'Duración: {self.duracion}')
        print(f'Cupo disponible: {self.cupo}')
        print(f'Líder: {self.lider}')
        print(f'Usuarios inscriptos:')
        for u in self.usuarios:
            print(f'- {u}')

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
                        if "Nombre" in datos:
                            proyecto = cls(
                                nombre = datos.get("Nombre"),
                                descripcion = datos.get("Descripcion"),
                                objetivos = datos.get("Objetivos"),
                                duracion = datos.get("Duracion"),
                                cupo = int(datos.get("Cupo", 0)),
                                lider = datos.get("Lider")
                            )
                            if datos.get("Integrantes"):
                                proyecto.usuarios = datos.get("Integrantes").split(",") if datos.get("Integrantes") != "[]" else []
                            proyectos.append(proyecto)
        except FileNotFoundError:
            pass
        return proyectos



class Tarea:
    def __init__(self,nombre,descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = "pendiente"
        self.usuario_asignado = None
    def get_tarea(self):
        asignada = self.usuario_asignado.nombre if self.usuario_asignado else "Nadie"
        return f'Tarea: {self.nombre} || Estado: {self.estado} || Asignada a: {asignada}'