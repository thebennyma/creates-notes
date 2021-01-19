import notas.nota as modelo


class Acciones:

    def crear(self, usuario):
        print(f"\nOk {usuario[1]}!! Vamos a crear una nueva nota ...")

        titulo = input("\nIntroduce el titulo de tu nota : ")
        descripcion = input("Mete el contenido de tu nota : ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)

        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto, has guardado la nota : {nota.titulo}")
        else:
            print(f"\nNo se ha guardadlo la nota, lo siento")

    def mostrar(self, usuario):
        print(f"\nVamos a mostrarte tus notas {usuario[1]}")

        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.listar()

        for nota in notas:
            print("\n************************************")
            print(f"Titulo de la nota: {nota[2]}")
            print(f"Contenido de la nota: {nota[3]}")

    def borrar(self, usuario):
        print(f"Perfecto {usuario[1]}, vamos a eliminar una nota")

        titulo = input(
            "Introduce el titulo de la nota que quieres eliminar : ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(
                f"\nPerfecto, borramos correctamente la nota : {nota.titulo}")
        else:
            print(f"\nNo se ha borrado la nota, intentalo de nuevo")
