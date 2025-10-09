import random
from funciones import traer_usuarios

def registrar_miembro(miembros):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    usuario_id = f"{nombre.lower()}_{apellido.lower()}{random.randint(1000, 9999)}"
    
    try:
        with open('postulantes.txt', 'r', encoding="utf-8") as archivo:
            for linea in archivo:
                if f"- {nombre} {apellido} -" in linea: #en caso que el nombre que ingrese al registrarse este entre los postulados, automaticamente le tira un mensaje terminando la accion
                    print("Ya estas registrado en el sistema")
                    return #si no pongo return la funcion sigue
    except FileNotFoundError:
        pass
    
    rol = input("Rol asignado (Diseño, Desarrollo, Comunicación, etc.): ")
    contraseña = input("Contraseña: ")
    print("¿Se registra como user o admin?")#Aca elige si es admin o user
    admin_user = input("1. Usuario 2. admin: ")
    if admin_user == "1": #Si elige usuario lo guarda sin ningun problema
        with open("postulantes.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Usuario - {nombre} {apellido} - {usuario_id} - {rol} - {contraseña}\n")
            print(f'Usuario registrado con exito!\nUsuario: {usuario_id}\nContraseña: {contraseña}')
    elif admin_user == "2": #Si elige admin tiene que poner una clave global para que autorice que va a ser admin
        contraseña_admin = input("Ingrese contraseña administradora: ")
        if contraseña_admin == "admin9898":#Clave para ser admin
            with open("postulantes.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"Admin - {nombre} {apellido} - {usuario_id} - {rol} - {contraseña}\n")#Lo guarda en postulantes.txt
            print(f'Administrador registrado con exito!\nUsuario: {usuario_id}\nContraseña: {contraseña}')
        else:
            print("Error - Contraseña invalida - Registrese como user")#Si no tiene la clave para ser admin le salta el error




def login():
    from menus import menu_admin, menu_usuario  #evita ciclos

    with open('postulantes.txt', 'r') as archivo:
        usuarios_registrados = archivo.readlines()
        

    print("\n------------------Iniciar sesión----------------------")
    usuario_solicitado = input("Usuario: ")
    contraseña_solicitada = input("Contraseña: ")
    
    for linea in usuarios_registrados: #aca iria la funcion traer_usuarios pero hay que arreglarla
        linea = linea.strip()
            
        partes = linea.split(' - ')
            
        tipo = partes[0]
        nombre_completo = partes[1]
        usuario = partes[2]
        area = partes[3]
        contraseña = partes[4]
    
        if usuario_solicitado == usuario and contraseña_solicitada == contraseña:
            print("-----------------------------------------")
            print(f"Hola, {nombre_completo}")
            if tipo.lower() == "admin":
                menu_admin(usuario)
            elif tipo.lower() == "usuario":
                menu_usuario(usuario)
            else:
                print("Tipo incorrecto")
        else:
            print("Usuario o contraseña incorrecta")