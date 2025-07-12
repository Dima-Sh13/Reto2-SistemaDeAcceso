"""
Desarrollar un sistema de autenticación en Python que permita registrar,
autenticar y gestionar usuarios con diferentes roles (como administradores y
clientes). El sistema debe ofrecer distintos niveles de acceso y funcionalidades
dependiendo del rol del usuario.

Registro de Usuarios:
•El sistema debe permitir registrar nuevos usuarios ingresando un nombre de usuario, contraseña y un rol (por ejemplo:
"admin" o "cliente").
•No se debe permitir registrar dos usuarios con el mismo nombre de usuario.
Autenticación (Login):
•Los usuarios deben poder iniciar sesión ingresando su nombre de usuario y contraseña.
•Si el usuario no existe o la contraseña es incorrecta, se debe mostrar un mensaje de error adecuado.
Roles de Usuario:
•Existen al menos dos tipos de usuarios:
•Admin: puede ver la lista de usuarios, crear nuevos usuarios y eliminar usuarios (estas funcionalidades pueden ser
simuladas inicialmente).
•Cliente: puede acceder a un menú con opciones limitadas, como ver productos o realizar compras (también pueden ser
simuladas).
•El sistema debe mostrar un menú diferente según el tipo de usuario que haya iniciado sesión.
Gestión de Sesiones:
•Tras iniciar sesión, el usuario debe ver las acciones disponibles según su rol.
•El sistema debe permitir cerrar sesión o salir.

-Uso de clases para representar:
•Un usuario base (Usuario)
•Roles específicos mediante herencia (Admin, Cliente)
-Almacenar los usuarios en un diccionario interno del sistema ({username: objeto_usuario})
-Uso de condicionales para controlar el flujo de autenticación y los menús por rol
-Uso de métodos polimórficos (menu() definido de forma distinta en cada clase)
-Validación de entrada por parte del usuario (por ejemplo, verificar si el usuario ya existe o si la contraseña es incorrecta)
"""
admins = {"admin1": "1234" }

users= {}

from utils.functions import *
#from utils.clases import *




usuario_activo = input("Introduzca su nombre de usuario: ")

if usuario_activo in admins or usuario_activo in users:
    pass_usuario_activo = input("Introduzca su contraseña.")
    if pass_usuario_activo == admins[usuario_activo]:
        print(f"Bienvenido{usuario_activo}")
        if usuario_activo in admins:
            menu_de_admin()
        elif usuario_activo in users:
            menu_de_cliente()    
else:
    print("Nombre de Usuario incorrecto, pruebe otra vez.")
