class Usuario: # CLASE USUARIO.
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
        if tarea.usuario_asignado is None:  # Si no se le asignó a nadie
            tarea.usuario_asignado = self  # Se le asigna
            tarea.estado = "En progreso..."
            print(f'{self.nombre} tomó la tarea: {tarea.nombre}')
        else:
            print(f'La tarea "{tarea.nombre}" ya está asignada.')
    
    def completar_tarea(self, tarea): #Completar una tarea
        if tarea.usuario_asignado == self: #Si fué asignada a alguien
            tarea.estado = "completada"
            self.historial.append(tarea) #Se agrega a la lista historial, donde van las tareas completadas.
            print(f'{self.nombre} completó la tarea: {tarea.nombre}')
        else:
            print('No podés completar esta tarea.')
            
    def generar_historial(self): # Con with se cierra solo el archivo.
        with open(f'{self.nombre}_historial.txt',"w") as f: #Abre y escribe en un archivo, si el archivo existe, lo sobrescribe, sino lo crea de nuevo.
            for tarea in self.historial:
                f.write(f'{tarea.nombre} - {tarea.estado}\n')
        print(f'Historial guardado en {self.nombre}_historial.txt')





class Proyecto:  
    def __init__(self, nombre, descripcion, objetivos, duracion,usuarios: list, cupo, lider=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.duracion = duracion
        self.usuarios = []
        self.cupo = cupo
        self.lider = lider

    
    def guardar_txt(self, archivo="proyectos.txt"): #Guarda los datos del proyecto cargado por el admin, y los guarda en proyectos.txt
        with open(archivo, "a", encoding="utf-8") as f:
            f.write("----------- Proyecto -----------\n")
            f.write(f"Nombre: {self.nombre}\n")
            f.write(f"Descripcion: {self.descripcion}\n")
            f.write(f"Objetivos: {self.objetivos}\n")
            f.write(f"Duracion: {self.duracion}\n")
            f.write(f"Integrentes: {self.usuarios}\n")
            f.write(f"Cupo: {self.cupo}\n")
            f.write(f"Lider: {self.lider}\n")
            f.write("-------------------------------\n\n")
    
    def agregar_usuario(self, usuario): 
        if self.tiene_cupo():
            self.usuarios.append(usuario)
            print(f'{usuario.nombre} se unio al proyecto "{self.nombre}".')
        else:
            print(f'No hay cupos disponibles en este proyecto')

    
    def mostrar_estado(self): #Muestra estado del proyecto.
        print(f'\nProyecto: "{self.nombre}"')
        print(f'Descripción: {self.descripcion}')
        print(f'Objetivos: {self.objetivos}')
        print(f'Duración: {self.duracion}')
        print(f'Usuarios inscriptos:')
        for u in self.usuarios:
            print(f'- {u}')
        print('Tareas: ')
        for tarea in self.tareas:
            print(f'- {tarea}')

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
                            nombre = datos.get("Nombre"),
                            descripcion = datos.get("Descripción"),
                            objetivos = datos.get("Objetivos"),
                            duracion = datos.get("Duración"),
                            usuarios = datos.get("Integrantes"),
                            cupo = int(datos.get("Cupo", 0)),
                            lider = datos.get("Líder")
                        )
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