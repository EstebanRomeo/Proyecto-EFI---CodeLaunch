usuarios = {
    "admin": {"contraseña": "admin123", "rol": "admin"},
    "esteban": {"contraseña": "user123", "rol": "usuario", "tareas": [], "objetivos": []},
    "marcos": {"contraseña": "user1234", "rol": "usuario", "tareas": [], "objetivos": []}
}

def registrar_miembro(miembros):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    rol = input("Rol asignado (Diseño, Desarrollo, Comunicación, etc.): ")

    
    with open("postulantes.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} {apellido} - Rol: {rol}\n")

    miembros.append({"nombre": nombre, "apellido": apellido, "rol": rol})
    print(f"{nombre} ha sido registrado como {rol}.")

def login():
    from menus import menu_admin, menu_usuario  #evita ciclos

    print("\n------------------Iniciar sesión----------------------")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        print(f"Bienvenido, {usuario}")
        if usuarios[usuario]["rol"] == "admin":
            menu_admin(usuario)
        else:
            menu_usuario(usuario)
    else:
        print("Usuario o contraseña incorrectos")
