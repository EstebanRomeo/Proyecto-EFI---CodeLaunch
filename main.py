from menus import mostrar_menu
from usuarios import registrar_miembro, login

def main():
    miembros = []  # lista en memoria
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ")
        
        if opcion == "1":
            registrar_miembro(miembros)
        elif opcion == "2":
            login()
        elif opcion == "3":
            print("¡Gracias por usar CodeLaunch!")
            break
        else:
            print("Opcion invalida - Intenta de nuevo")

if __name__ == "__main__":
    main()
