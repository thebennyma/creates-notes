import usuarios.usuario as modelo
import notas.acciones
import getpass


class Acciones:

    def registro(self):
        print("\nOk!! Vamos a registrarte en el sistema ... ")

        nombre = input("\n¿Cual es tu nombre? : ")
        apellidos = input("¿Cuales son tus apellidos? : ")
        email = input("Introduce tu email : ")
        password = getpass.getpass("Introduce tu contraseña : ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:
            print(
                f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}\n")
        else:
            print("\nNo te has registrado correctamente\n")

    def login(self):
        print("\nVale!! Identificate en el sistema ... ")

        try:
            email = input("\nIntroduce tu email : ")
            password = getpass.getpass("Introduce tu contraseña : ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(
                    f"\nBienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(e)
            print(f"Login incorrecto!! Intentalo más tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles 
            - Crear nota (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        """)

        accion = input("¿Que quieres hacer? : ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"\nNos vemos, hasta la proxima {usuario[1]}!!")
            exit()

        return None
