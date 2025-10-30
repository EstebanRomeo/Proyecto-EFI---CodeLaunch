import re
from typing import Callable, Any

# -------------------- VALIDACIONES --------------------

def ftry(funcion: Callable[..., Any], *args: Any) -> bool:
    try:
        funcion(*args)
        return True
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return False


def validar_nombre(nombre: str) -> None:
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre solo puede contener letras.")


def validar_rol(rol: str) -> None:
    if not rol or not rol.strip():
        raise ValueError("El rol no puede estar vacío.")
    if len(rol) < 3:
        raise ValueError("El rol debe tener al menos 3 caracteres.")


def validar_contraseña(contraseña: str) -> None:
    if len(contraseña) < 6:
        raise ValueError("La contraseña debe tener al menos 6 caracteres.")
    if not re.search(r"[A-Z]", contraseña):
        raise ValueError("La contraseña debe incluir al menos una letra mayúscula.")
    if not re.search(r"[a-z]", contraseña):
        raise ValueError("La contraseña debe incluir al menos una letra minúscula.")
    if not re.search(r"\d", contraseña):
        raise ValueError("La contraseña debe incluir al menos un número.")


# -------------------- REGISTRO --------------------

def registrar_usuario():
    print("\n--------- Registro de nuevo miembro ---------")

    while True:
        nombre = input("Nombre: ")
        if ftry(validar_nombre, nombre):
            break

    while True:
        rol = input("Rol (ej: usuario o admin): ")
        if ftry(validar_rol, rol):
            break

    while True:
        contraseña = input("Contraseña: ")
        if ftry(validar_contraseña, contraseña):
            break

    print(f"\nUsuario '{nombre}' registrado correctamente.")

    with open("postulantes.txt", "a") as archivo:
        archivo.write(f"{rol} - {nombre} - {nombre.lower().replace(' ', '_')} - N/A - {contraseña}\n")