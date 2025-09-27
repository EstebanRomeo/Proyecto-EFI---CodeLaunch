#                                                          | PROYECTO EFI |
                            
                                
class Usuario: # CLASE USUARIO.
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = [] # Tareas completadas
    
    def __str__(self):
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

        
class Administrador(Usuario): #CLASE ADMINISTRADOR  --> HEREDA ATRIBUTOS DE LA CASE "USUARIO"
    
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def crear_proyecto(self, plataforma, nombre, descripcion, objetivos, duracion, cupo):
        proyecto = Proyecto(nombre, descripcion, objetivos, duracion, cupo) #Creamos un objeto con su nombre, descripcion, objetivos, duración y cupo.
        plataforma.proyectos.append(proyecto) #Lo agregamos a la lista proyectos, de la clase "Plataforma".
        print(f'Proyecto "{nombre}" creado por {self.nombre}')
        
    def agregar_tarea(self, proyecto, nombre, descripcion):
        tarea = Tarea(nombre, descripcion) #Creamos un objeto con su nombre, y descripcion.
        proyecto.tareas.append(tarea) #Agregamos la tarea creada a la lista tareas de la clase Proyecto.
        print(f'Trea "{nombre} agregada al proyecto {proyecto.nombre}')
    
    def eliminar_proyecto(self, plataforma, proyecto):
        if proyecto in plataforma.proyectos:
            plataforma.proyectos.remove(proyecto) #Si se encuentra el proyecto, lo eliminamos.
            print(f'Proyecto "{proyecto.nombre}" fue eliminado.')

class Proyecto: #CLASE PROYECTO
    def __init__(self, nombre, descripcion, objetivos, duracion, cupo):
        self.nombre = nombre
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.duracion = duracion
        self.cupo = cupo
        self.tareas = []
        self.usuarios = []
        
    def __str__(self):
        return f'{self.nombre} ({len(self.tareas)} tareas, {len(self.usuarios)}/{self.cupo} usuarios)'
        
    def tiene_cupo(self):
        return len(self.usuarios) < self.cupo #Devuelve True o False.
    
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
            
class Tarea: #CLASE TAREA
    def __init__(self,nombre,descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = "pendiente"
        self.usuario_asignado = None
    def __str__(self):
        asignada = self.usuario_asignado.nombre if self.usuario_asignado else "Nadie"
        return f'Tarea: {self.nombre} || Estado: {self.estado} || Asignada a: {asignada}'

class Plataforma: #CLASE PLATAFORMA
    def __init__(self):
        self.proyectos = []
        self.usuarios = []
        
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario) #Agregamos al usuario a la lista usuarios.
        print(f'Usuario {usuario.nombre} registrado en la plataforma.')
        
    def listar_proyectos(self):
        print('\nProyectos en la plataforma:')
        for proyecto in self.proyectos:
            print(f'- {proyecto.nombre} || {len(proyecto.tareas)} tareas || {len(proyecto.usuarios)} || {proyecto.cupo} usuarios.')


#                                                      | PRUEBA |

plataforma = Plataforma() # Creamos una plataforma.
admin = Administrador('Dios supremo') # Creamos un administrador.
user1 = Usuario('Salvador') # Creamos un usuario.
user2 = Usuario('Pablo') # Creamos un usuario.
user3 = Usuario('Daniel') # Creamos un usuario.
plataforma.registrar_usuario(admin) # Registramos al administrador.
plataforma.registrar_usuario(user1) # Registramos al usuario 1.
plataforma.registrar_usuario(user2) # Registramos al usuario 2.
plataforma.registrar_usuario(user3) # Registramos al usuario 3.


#ADMIN CREA UN PROYECTO:
admin.crear_proyecto(plataforma, "App de Tareas", "Gestionar tareas", "Laburen negros", "2 meses", 3)

#ADMIN CREA OTRO PYOTECTO:
admin.crear_proyecto(plataforma, "Pagina Web", "Diseño responsive", "Laburen negros", "1 mes", 5)

#AGREGAR TAREA:
proyecto = plataforma.proyectos[0]
admin.agregar_tarea(proyecto, "Diseñar clases", "Definir clases y atributos")

#USUARIO SE POSTULA Y TOMA LA TAREA:
user1.postularse(proyecto)
tarea = proyecto.tareas[0]
user1.tomar_tarea(tarea)
user1.completar_tarea(tarea)

#GUARDAR HISTORIAL:
user1.generar_historial()

#VER ESTADO DE PROYECTO:
proyecto.mostrar_estado()