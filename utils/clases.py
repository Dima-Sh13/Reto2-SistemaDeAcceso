
   


class Admin:
    nUsuario = ""
    password = ""
    


    def __init__(self,username, passw):
        self.nUsuario = username
        self.password = passw
    def menu(self):
        print(f"--SESION INICIADA COMO ADMINISTRADOR--\n1.Añadir o Eliminar Usuarios.\n2. Ver usuarios\n3.Otras opciones.\n4.Cerrar Sesion")    




class Cliente:
    nUsuario = ""
    password = ""
    def __init__(self, username, passw):
        self.nUsuario = username
        self.password = passw
    def menu(self):
        print(f"--SESION INICIADA COMO CLIENTE--\n1.Añadir pedido.\n2.Ver usuarios\n3.Cerrar Sesion")    
