usuarios = {
    "admin": {"contraseña": "admin123", "rol": "admin"},
    "deus": {"contraseña": "admin1234", "rol": "admin"},
    "esteban": {"contraseña": "user123", "rol": "usuario", "tareas": [], "objetivos": []},
    "marcos": {"contraseña": "user1234", "rol": "usuario", "tareas": [], "objetivos": []}
}

def registrar_miembro(miembros):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    usuario = input("Nombre de usuario: ")
    rol = input("Rol asignado (Diseño, Desarrollo, Comunicación, etc.): ")
    contraseña = input("Contraseña: ")
    print("¿Se registra como user o admin?")
    admin_user = input("1. Usuario 2. admin: ")
    if admin_user == "1":
        with open("postulantes.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Usuario - {nombre} {apellido} - {usuario} - {rol} - {contraseña}\n")
    elif admin_user == "2":
        contraseña_admin = input("Ingrese contraseña administradora: ")
        if contraseña_admin == "admin9898":
            with open("postulantes.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"Admin - {nombre} {apellido} - {usuario} - {rol} - {contraseña}\n")
        else:
            print("Error - Contraseña invalida - Registrese como user")
    

    miembros.append({"nombre": nombre, "apellido": apellido, "rol": rol})
    print(f"{nombre} ha sido registrado como {rol}.")

def login():
    from menus import menu_admin, menu_usuario  #evita ciclos

    with open('postulantes.txt', 'r') as archivo:
        usuarios_registrados = archivo.readlines()
        

    print("\n------------------Iniciar sesión----------------------")
    usuario_solicitado = input("Usuario: ")
    contraseña_solicitada = input("Contraseña: ")
    
    for linea in usuarios_registrados:
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