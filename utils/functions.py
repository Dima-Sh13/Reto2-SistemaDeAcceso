
from clases import Admin, Usuarios, Cliente

def addUser(name, password, role):
    
    

    if role == "admin":
        name1 = Admin(name, password)
        admins[name] = name1
    elif role == "user":
        name1 = Cliente(name, password)
        users[name] = name1  



def menu_de_admin():
    seleccion = input((f"--SESION INICIADA COMO ADMINISTRADOR--\n1. Añadir Usuarios.\n2. Ver usuarios\n3. Otras opciones.\n4. Cerrar Sesion"))
    if seleccion == "1":
        nombre = input("Introduzca un nombre para el nuevo usuario. ")
        password = input("Introduzca una contraseña para el nuevo usuario. ")
        rol = input("Introduzca un rol para el nuevo usuario. admin/cliente. ")
        addUser(nombre, password, rol)
    elif seleccion == "2":
        print( admins, users)


def menu_de_cliente():
    seleccion = input(f"--SESION INICIADA COMO CLIENTE--\n1. Añadir pedido.\n2. Ver usuarios\n3. Cerrar Sesion")      