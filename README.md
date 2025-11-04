Sistema de registro y login con roles (admin/usuario)
En el proyecto implementamos un sistema basico de registro e inicio de sesion utilizando archivos .txt como base de datos.

Caracteristicas Principales:
- Registro de miembros con:
  - Nombre y apellido
  - Rol dentro del equipo
  - Contraseña
  - Generacion automatica de usuario
  - Diferentes acciones entre "Usuario comun" y "Administrador"
  ---------Nuevo--------
    -Validaciones

  **main.py** → Punto de entrada del programa
  **usuarios.py** → Contiene las funciones "registrar_miembro()" y "login()"
  **menus.py** → Define los menús para admin y usuario (funciones "menu_admin()" y "menu_usuario()")
  **funciones.py** → Contiene las funciones lanzar_proyecto() y postularse_proyecto()
  **postulantes.txt** → Archivo donde se almacenan los usuarios registrados
  **proyectos.txt** → Archivo donde se almacenan los proyectos creados por los administradores, estos no los pueden ver los usuarios ya que no fueron lanzados
  **proyectos_aprobados.txt** → Archivo donde se almacenan los proyectos aprobados y lanzados por un administrados, estos si los pueden ver los usuarios como tambien postularse


  Mejoras 29/10
  Agregamos validaciones en lo que es el registro. El usuario no podra poner un espacio vacio en el registro, la contraseña tiene que ser unicamente de 6 caracteres, tiene que tener al menos una letra mayuscula y algun numero.
  Tambien se implemento la funcion de ver los proyectos disponibles


  ULTIMAS MEJORAS ESPERADAS
  Agregar al sistema una gestión de tareas por proyecto donde:
    Cada proyecto tiene N tareas definidas al momento de su creacion.
    Cada tarea tiene:
    Un nombre
    Un estado:
      "Sin asignar"
      "Asignada a usuario"
      "Completada por usuario"
      "Incompleta por usuario" si alguien la tomO pero no la completo
    Los usuarios pueden:
      Ver las tareas del proyecto
      Tomar una tarea (la asignan a su nombre)
      Marcarla como completada (se guarda en su historial)
      Ver su historial de tareas completadas
