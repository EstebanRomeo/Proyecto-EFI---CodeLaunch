def registrar_miembro(miembros):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    usuario_id = f"{nombre.lower()}_{apellido.lower()}"  # identificador único

    # Verificar si ya existe en memoria
    if usuario_id in usuarios:
        print("¡Este usuario ya está registrado en memoria!")
        return

    # Verificar si ya existe en archivo
    try:
        with open("postulantes.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if f"UsuarioID: {usuario_id}" in linea:
                    print(f"¡{nombre} {apellido} ya está registrado en el CodeLaunch, intente nuevamente.")
                    return
    except FileNotFoundError:
        pass  # Si no existe el archivo, sigue

    rol = input("Rol asignado (Diseño, Desarrollo, Comunicación, etc.): ")
    contraseña = input("Contraseña: ")
    print(f'¡Usuario registrado con exito!\nUsuario: {usuario_id}\nContraseña: {contraseña}')

    # Guarda en memoria
    usuarios[usuario_id] = {
        "contraseña": contraseña,
        "rol": "usuario",
        "tareas": [],
        "objetivos": []
    }

    # Guarda en archivo
    with open("postulantes.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} {apellido} || UsuarioID: {usuario_id} || Rol: {rol} || Contraseña: {contraseña}\n")