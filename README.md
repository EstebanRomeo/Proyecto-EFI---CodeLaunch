Sistema de registro y login con roles (admin/usuario)
En el proyecto implementamos un sistema basico de registro e inicio de sesion utilizando archivos .txt como base de datos.

Caracteristicas Principales:
- Registro de miembros con:
  - Nombre y apellido
  - Rol dentro del equipo
  - Contraseña
  - Generacion automatica de usuario
  - Diferentes acciones entre "Usuario comun" y "Administrador"

  **main.py** → Punto de entrada del programa
  **usuarios.py** → Contiene las funciones "registrar_miembro()" y "login()"
  **menus.py** → Define los menús para admin y usuario (funciones "menu_admin()" y "menu_usuario()")
  **funciones.py** → Contiene las funciones lanzar_proyecto() y postularse_proyecto()
  **postulantes.txt** → Archivo donde se almacenan los usuarios registrados
  **proyectos.txt** → Archivo donde se almacenan los proyectos creados por los administradores, estos no los pueden ver los usuarios ya que no fueron lanzados
  **proyectos_aprobados.txt** → Archivo donde se almacenan los proyectos aprobados y lanzados por un administrados, estos si los pueden ver los usuarios como tambien postularse

  Futuras mejoras:
  - Validar que los campos no estén vacíos
  - Evitar duplicados usando el "usuario_id" en lugar del nombre
  - Reemplazar "-" por "|" como separador para mayor estabilidad
  - Agregar funciones como:
    - Agregar tarea a un usuario especifico
    - Generar historial de tareas
    - Ver proyectos
    - Marcar por completa una tarea
    - Tomar tarea
