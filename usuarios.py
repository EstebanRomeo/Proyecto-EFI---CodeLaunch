from validaciones import ftry, validar_nombre, validar_rol, validar_contraseña
import random

import random
from validaciones import ftry, validar_nombre, validar_rol, validar_contraseña

def registrar_miembro(miembros):
    print("\n--------- Registro de nuevo miembro ---------")

    # NOMBRE
    while True:
        nombre = input("Nombre: ")
        if ftry(validar_nombre, nombre):
            break

    # APELLIDO
    while True:
        apellido = input("Apellido: ")
        if ftry(validar_nombre, apellido):
            break

    # GENERAR USUARIO
    usuario_id = f"{nombre.lower()}_{apellido.lower()}{random.randint(1000,9999)}"

    # VERIFICAR DUPLICADOS
    try:
        with open('postulantes.txt', 'r', encoding="utf-8") as archivo:
            for linea in archivo:
                if usuario_id in linea:
                    print("Ya existe un usuario con ese nombre, intenta nuevamente.")
                    return
    except FileNotFoundError:
        pass

    # ROL
    while True:
        rol = input("Rol asignado (Diseño, Desarrollo, Comunicación, etc.): ")
        if ftry(validar_rol, rol):
            break

    # CONTRASEÑA
    while True:
        contraseña = input("Contraseña: ")
        if ftry(validar_contraseña, contraseña):
            break

    # GUARDAR USUARIO
    with open("postulantes.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Usuario - {nombre} {apellido} - {usuario_id} - {rol} - {contraseña}\n")

    miembros.append({"usuario": usuario_id, "nombre": f"{nombre} {apellido}", "rol": rol})

    print(f"\nUsuario '{usuario_id}' registrado correctamente.")


def login():
    from menus import menu_admin, menu_usuario  # evitar ciclos si es necesario

    with open('postulantes.txt', 'r') as archivo:
        usuarios_registrados = archivo.readlines()

    print("\n------------------Iniciar sesión----------------------")
    usuario_solicitado = input("Usuario: ")
    contraseña_solicitada = input("Contraseña: ")

    encontrado = False  # bandera

    for linea in usuarios_registrados:
        partes = linea.strip().split(' - ')
        if len(partes) < 5:
            continue  # línea mal formada, la salteamos

        tipo, nombre_completo, usuario, area, contraseña = partes

        if usuario_solicitado == usuario and contraseña_solicitada == contraseña:
            encontrado = True
            print("-----------------------------------------")
            print(f"Hola, {nombre_completo}")
            if tipo.lower() == "admin":
                menu_admin(usuario)
            elif tipo.lower() == "usuario":
                menu_usuario(usuario)
            else:
                print("Tipo incorrecto")
            return  # corta la función al iniciar sesión

    if not encontrado:
        print("Usuario o contraseña incorrecta")