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
        print("1. Subir proyecto") #Ya esta listo
        print("2. Lanzar proyecto") #Tambien diria que esta listo
        print("3. Asignar tareas") #Diria de sacarlo, no le veo mucho sentido
        print("4. Ver postulaciones")#Falta
        print("5. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            Proyecto.crear_proyecto(usuario)
        elif opcion == "2":
            lanzar_proyecto()


def menu_usuario(usuario):
    while True:
        print("\n--------- MODO USUARIO ---------------")
        print("1. Postularse a proyecto")#Falta
        print("2. Ver tareas asignadas")#Falta
        print("3. Ver objetivos")#Falta
        print("4. Ver proyectos disponibles")#Falta
        print("5. Salir")
        opcion = input("Opción: ")
        if opcion == "1":
            postularse_proyecto(usuario)
        
